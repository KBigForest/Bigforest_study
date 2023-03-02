#데이터 전처리

#결측치 확인 제거
checkna <- function(data){
  eNum <- sum(is.na(data))
  rNum <- sum(!complete.cases(data))
  print(paste('원서 NA',eNum,'행 NA',rNum))
}
data <- complete.cases(data)
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
grubbs.flag(iris$Sepal.Length)
outlierfunc(iris$Sepal.Length)
##
regression1 <- lm(formula = Y~X)

iris.cor <- corr.test(iris[-5])
iris.cor
model <- lm(iris$Petal.Length~iris$Petal.Width)
summary(model)

y = coef(model)[1]+ coef(model)[2]*x
mtcars

mtcars
model<- lm(mpg ~ cyl+hp+qsec,data = mtcars)
summary(model)
