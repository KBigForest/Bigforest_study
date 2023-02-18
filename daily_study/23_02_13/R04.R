head(iris)
colnames(iris)
plot(iris[,1]~iris[,4])
z <- lm(iris[,1]~iris[,4])
abline(z)
summary(z)

zz <- lm(iris[,1]~iris[,2]+iris[,3]+iris[,4])
zz
install.packages('ROCR') # roc커브를 그리기 위한 패키지
install.packages('e1071')#범주형 로지스틱회귀
install.packages('MASS') #범주형 로지스틱회귀
install.packages('pscl') #
install.packages('car')#데이터전처리용
install.packages('kernlab')
install.packages('nnet')#인공신경망
install.packages('car') #데이터 전처리
install.packages('SparseM')
install.packages('glmnet') # lasso 변수선택방법
install.packages('elasticnet')
install.packages("corrplot") #다중공선성을 알아보기 위해 상관플롯을 그르기위한 패키지
install.packages('rpart')
library('dplyr')
library("corrplot")
library('elasticnet')
library('glmnet')
library('SparseM')
library('car')
#
library('pscl')
#
library('e1071')
# 범주형 로지스틱회귀
library('MASS')
# 범주형 로지스틱회귀
library('caret')#
library('kernlab')
library('nnet')
# 인공신경망
library('ROCR')

library('rpart')
head(training)
m<-rpart(신용평점 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 + 단기차입금.
         총자본,data=training)
plot(m,compress=TRUE,margin=0.1)
text(m,cex=0.8)
#뭔가 보기 불편함
setwd('C:/Users/dddf/Desktop/Study/02_13')
getwd()
data <- read.csv('C:/Users/dddf/Desktop/Study/02_13/company.csv',header = T, fileEncoding = 'cp949')
data
str(data)
head(data)
dim(data)
data <-  rename(data, '신용평점'='KIS.신용평점.0A3010')
colSums(is.na(data))
for (i in 1:dim(data)[2]){
  data[is.na(data[,i]),i]=median(data[,i],na.rm=T)}

data$신용평점 <- ifelse(data$신용평점 <= 5, 0, 1)

data$신용평점 <- as.factor(data$신용평점)
data$신용평점
set.seed(123)
intrain <- createDataPartition(y=data$신용평점, p =0.7,list = FALSE)
intrain
training <- data[intrain,]
training
testing <- data[-intrain,]
testing


colnames(data)
m2<-train(신용평점 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 + 단기차입금.총자본,data=training,method='glm')
summary(m2)

predictions2 <- predict(m2, newdata = testing)
confusionMatrix(prediction2, testing$신용평점)
predictions2

m<-rpart(신용평점 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 + 단기차입금.총자본,data=training)
plot(m,compress=TRUE,margin=0.1)
text(m,cex=0.8)

install.packages('rpart.plot')
library('rpart.plot')

prp(m, type=4, digits=3) # type extra digits 숫자 바꿔보면 더 예쁘게 꾸며짐.
#예측
pre_rpart<-predict(m,newdata=testing)
head(pre_rpart)
head(testing)
pre_rpart<-round(pre_rpart[,2]) # p값을 0.5로 두자.
pre_rpart<-as.vector(pre_rpart)
pre_rpart<-as.factor(pre_rpart)
test_rpart<-testing$신용평점
test_rpart<-as.factor(test_rpart)
confusionMatrix(pre_rpart,test_rpart)

###랜덤포레스트
install.packages('randomForest')
library('randomForest')
head(training)
m2<-randomForest(신용평점 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 +단기차입금.총자본,data=training)
m2
#변수중요도
importance(m2)
#그래프 그리기
varImpPlot(m2)
##인공신경망
m<-nnet(신용평점 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 + 단기차입금.총자본,size=5, #은닉층노드갯수
linout=FALSE, # TRUE이면 활성함수가 선형출력(liner output) FALSE면 로지스틱함수가 적용
MaxNWts=1000, # 가중치의 최대개수로 기본값은 1000, 모델이 복잡하다면 가중치의 수를 증가시켜야함.
data=training)
#나머지 옵션도 있음. 찾아볼 것.
pre_nnet<-predict(m,newdata=testing)
head(pre_nnet)
pre_nnet<-as.factor(round(pre_nnet))
pre_nnet
#예측
confusionMatrix(pre_nnet,testing$신용평점)

KIS <- read.csv('KIS.csv') 
KIS
plot(KIS$Trust, KIS$DeR, type = 'l',main = 'KIS Chart', xlab = '신뢰도', ylab = '부채비율')


op <- par(no.readonly = TRUE)
par(mar = c(0, 2, 2, 2))
theta <- seq(-pi, pi, length = 12)
x <- cos(theta)
y <- sin(theta)
plot(1:6, type = "n", main = "PLOYGON", xlab = "", ylab = "", axes = F)
x1 <- x + 2
y1 <- y + 4.5
polygon(x1, y1)
x2 <- x + 2
y2 <- y + 2
polygon(x2, y2, col = "red", border="blue")
x3 <- x + 5
y3 <- y + 4.5
polygon(x3, y3, density = 10, angle=135)
x4 <- x + 5
y4 <- y + 2
polygon(x4, y4, lty = 2, lwd = 2)
text(2, 5.7, adj = 0.5, "defalut")
text(5, 5.7, adj = 0.5, "density = 10")
text(5, 3.2, adj = 0.5, "lty = 2, lwd = 2")
par(op)


plot(c(1, 8), c(-4, 4), type = "n")
x <- c(1, 2, 3, NA, 4, 4, 6, 6)
y <- c(1, -4, 3, NA, -3, 3, 3, -3)
polygon(x, y, col = c("pink", "blue"), border = c("red", "orange"), lwd = 2,
        lty = c("dotted", "solid"))
lines(c(1,8), c(-2,-2), lty=4, col="green")
arrows(1, 2, 8, 2, length=0.5)
title("Polygons") 
