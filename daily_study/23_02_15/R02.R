getwd()
setwd('C:/Users/dddf/Desktop/Study/02_15')
cafedata <- read.csv('cafedata.csv',na.strings = 'NA')
summary(cafedata)
#원소단위 검사
sum(is.na(cafedata))

#행단위 검사
complete.cases(cafedata)

cafedata<- cafedata[-34,]
cafedata <- na.omit(cafedata)

#최빈값
coffee <- table(cafedata$Coffees)
names(coffee)[which(coffee==max(coffee))]
data <- c(1,1,2,2,3,3,3,4)
stem(data)

mean(coffee, na.rm = T)
median(coffee)

#표준편차
#(x-xmean)^2/n-1
height <- c(164,166,168,170,172,174)
sum((height - mean(height))**2)/length(height)
data <- airquality
sum(is.na(data))

which(is.na(data)==TRUE)
#삭제
data <- na.omit(data)
#na값이 없는 행만 출력
which(is.na(data)==FALSE)
summary(data)
mean(data)
var(data)
sqrt(var(data))

data2 <- table(data)
data2

names(coffee)[which(coffee==max(coffee))]

cardata <- cars
disdata<- cars$dist
mean(disdata)
Q <- quantile(disdata,probs= seq(0,1,0.25),na.rm =F)
Q



iqr <- IQR(disdata)

#정상 데이터 구간값
iqr
#하위 이상치 상위 이상치 계산
lout <- Q[2]-(1.5*iqr)
lout
uout <- Q[4]+(1.5*iqr)
uout




str(iris)
#1. 데이터기본정보
#   열이름
colnames(iris)
#   차원
dim(iris)
dataF <- iris

#결측치 체크 & 처리
sum(is.na(dataF))
#없음
#꽃받침 이상치
fsl <- iris$Sepal.Length
Q_ver1 <- quantile(fsl,probs= seq(0,1,0.25),na.rm =F)
iqr_ver1 <- IQR(fsl)
lout <- Q_ver1[2] - (1.5*iqr_ver1)
uout <- Q_ver1[4] + (1.5*iqr_ver1)

fsw <- iris$Sepal.Width
Q_ver2 <- quantile(fsw,probs= seq(0,1,0.25),na.rm =F)
#정상데이터 구간값
iqr_ver2 <- IQR(fsw)
iqr_ver2
#이상치 구간값
lout <- Q_ver2[2] - (1.5*iqr_ver2)
uout <- Q_ver2[4] + (1.5*iqr_ver2)
lout
uout
boxplot(Q_ver2)
