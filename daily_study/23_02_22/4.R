#선형회귀 과제
#단순선형회귀

Crime<- USArrests
#인구에 따른 살인율
#데이터 전처리

#결측치 확인 제거
checkna <- function(data){
  eNum <- sum(is.na(data))
  rNum <- sum(!complete.cases(data))
  print(paste('원서 NA',eNum,'행 NA',rNum))
}
checkna(Crime)
#이상치(outlier) 확인
library(psych)
library(outliers)


outlierfunc <- function(data){
  
  #1 IQR을 벗어나는 값
  
  UpperQ = fivenum(data)[4]
  LowerQ = fivenum(data)[2]
  IQR = UpperQ - LowerQ
  upperOutlier = data[ which( data > UpperQ+IQR*1.5) ]
  lowerOutlier = data[ which( data < LowerQ-IQR*1.5) ]
  cat('IQR을 이용한 이상치 검출 upperOutlier : ',upperOutlier, 'lowerOutlier : ', lowerOutlier,'\n')
  
  
  #2  MAD: Median absolute deviation, modified Z-score
  MAD1= data[which(0.6748*(data-median(data))/mad(data) < -1.28)]
  MAD2= data[which(0.6748*(data-median(data))/mad(data) > 1.28)]
  cat('MAD 이용 이상치 검출 :',MAD1,MAD2,'\n')
  
  #3 ESD(Extreme Studentized Deviation) 평균에서 3표준편차 떨어진 값
  #Grubb's Test이용 이상치 검출 True 시 이상치
  cat('Grubb Test')
  print(grubbs.flag(data))
  
  #4 기하평균 사용 이상치 확인
  geo1 = data[which(data > geometric.mean(data)+2.5*sd(data))]
  geo2 = data[which(data < geometric.mean(data)-2.5*sd(data))]
  
  cat('기하평균 사용 이상치', geo1, geo2, '\n')
  
  
}
##퍙퍙
grubbs.flag <- function(x) {
  outliers <- NULL
  test <- x
  grubbs.result <- grubbs.test(test)
  pv <- grubbs.result$p.value
  while(pv < 0.05) {
    outliers <- c(outliers,as.numeric(strsplit(grubbs.result$alternative," ")[[1]][3]))
    test <- x[!x %in% outliers]
    grubbs.result <- grubbs.test(test)
    pv <- grubbs.result$p.value
  }
  return(data.frame(X=x,Outlier=(x %in% outliers)))
}
#폭행 이상치
outlierfunc(Crime$Assault)
#없음
#인구 이상치
outlierfunc(Crime$UrbanPop)
#ESD이용시 32가 이상치
#제거
Crime <- Crime[-which(0.6748*(Crime$UrbanPop-median(Crime$UrbanPop))/mad(Crime$UrbanPop) < -1.28),
]
#폭행과 살인율의 단순선형회귀
model1 <- lm(Murder~Assault, data = Crime)
summary(model1)
#상수가 만족X
#R**2값도 애매함
install.packages('gvlma')
library(gvlma)
summary(gvlma(model1))

#Global stat: 선형성(종속 변인과 독립 변인들 간 선형적 관계가 나타나는가?)
#Skewness, Kurtosis: 왜도와 첨도 -> 잔차의 정규성을 나타내는 지표
#Link Function: 종속변인이 정확히 연속형(continuous) 변수인가?
#Heteroscedasticity: 이분산성(등분산성의 반의어)

#정규성 시각화
qqnorm(model1$residuals)
qqline(model1$residuals)
shapiro.test(model1$residuals)
#0.05보다 크므로 정규성 만족

#등분산성 
library(car)
ncvTest(model1)
#0.05보다 크면 만족


#폭행과 인구에 따른 살인체포율 다중 선형회귀
model2 <- lm(Murder~ Assault+UrbanPop,data= Crime)
summary(model2)
#지레점 찾기
hat.plot=function(fit){
  p=length(coefficients(fit))
  n=length(fitted(fit))
  plot(hatvalues(fit), main="Index Plot of Hat Values")
  abline(h=c(2,3)*p/n, col="red", lty=2)
  identify(1:n, hatvalues(fit), names(hatvalues(fit)))
}
hat.plot(model2)

#영향치
cutoff=4/(nrow(states)-length(model2$coefficients)-2)
plot(model2, which=4, cook.levels=cutoff)]
abline(h=cutoff, lty=2, col="red")

library(car)
#한번에 보기
car::influencePlot(model2, id.method="identity", main="Influence Plot", sub="Circle size is proportional to Cook`s distance")
#영향점은 원의 크기가 큰 Gerogia, Hawaii, North Carolina
#이상치는 2이상인 Georgia
# 