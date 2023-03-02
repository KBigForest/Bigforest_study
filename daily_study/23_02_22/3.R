library(MASS)
disInfo <- function(data){
  cat('INFO')
  str(data)
  summary(data)}

disInfo(cats)

checkna <- function(data){
  eNum <- sum(is.na(data))
  rNum <- sum(!complete.cases(data))
  print(paste('원서 NA',eNum,'행 NA',rNum))
}
checkna(cats)

#최빈값
table


checkMode <- function(data){
      for(col in colnames(data))
    {
      max(table(data[col]))
      maxIdx <- which.max(table(data[col]))
      maxValue <- names(which.max(table(data[col])))
      print(paste(col, '최빈값: ', maxValue))
    }
}

#이상치 체크 기능 함수
#-> 과제
#데이터 상관계수


#기술 통계분석 
#
plot(cats$Hwt, cats$Bwt,main= '고양이 무게 심장')
#변수 컬럼의 상관관계 체크
#=> 정규분포 여부 -> 계산방법 선정
#(1-1) 정규성검정
library(car)

shapiro.test(cats$Bwt)
qqPlot(cats$Bwt)
shapiro.test(cats$Hwt)
qqPlot(cats$Hwt)
#(1-2) 상관계수 계산방법 결정 및 계산
cor(cats$Hwt,cats$Bwt)
cor(cats$Hwt,cats$Bwt, method= 'spearman')
cor(cats$Hwt,cats$Bwt, method= 'kendall')


cor.test(cats$Bwt,cats$Hwt, method = 'kendall')

install.packages("psych")
#4개 컬럼들의 상관계수 검정

library(psych)
iris.cor <- corr.test(iris[,-5])
class(iris.cor)
install.packages('gmm')
library(corrgram)

corrgram(iris[-5],upper.panel = panel.conf)

mtcars2 <- with()

mtcars.cor <- cor(mtcars)
mtcars.cor[,'mpg']
class(mtcars.cor[,'mpg'])
library(gmm)
install.packages('ppcor')
library(ppcor)
ppcor.test()
ppcor(mtcars)

source('utils\\util.r')
install.packages('HistData')
library(HistData)

str(GaltonFamilies)
disInfo(GaltonFamilies)
familyDF<- GaltonFamilies
shapiro.test(familyDF$midparentHeight)
shapiro.test(familyDF$childHeight)
cor(familyDF$midparentHeight, familyDF$childHeight)

model<- lm(familyDF$midparentHeight~ familyDF$childHeight)
anova(model)
