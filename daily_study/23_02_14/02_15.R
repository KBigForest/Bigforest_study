getwd()
setwd('C:/Users/dddf/Desktop/Study/02_14')
data <- read.csv('주택조사2010.csv')
data
#데이터확인
str(data)
#행열 확인
dim(data)
#행개수 #열개수
x=dim(data)
x[1]
x[2]
nrow(data)
ncol(data)
#행열 이름
colnames(data) <- c('성별', '연령','가구 주관계','교육','남아출생수','여아출생수')
colnames(data)dim(data)



#scatter
cars
plot(cars$dist, cars$speed)

#100년간 나일강의 유속
str(Nile)
Nile

plot(Nile)
#빈도는 barplot
#tabel()
getwd()
setwd('C:/Users/dddf/Desktop/Study/02_14')
data <- read.csv('주택조사2010.csv', header = FALSE)
data
#데이터 백업 save(데이터, 파일경로)
save(data,file = 'C:/Users/dddf/Desktop/Study/02_14/data.RData')
#작업환경 전체를 저장
#데이터 로드 load(파일경로 데이터 이름)
x<- load('C:/Users/dddf/Desktop/Study/02_14/data.RData')
x
data$V1 <- factor(data$V1, levels= 1:2, labels = c('남자','여자'))
data$V4 <-factor(data$V4, levels= 1:8, labels = c('안 받았음', '초등학교', '중학교', '고등학교','대학~4년제 미만','대학~4년제 이상', '석사과정','박사과정'))
data$V3 <- factor(data$V3, levels = 1:14, labels = c('가구주', '가구주의 배우자','자녀','자녀의 배우자','가구주의 부모','배우자의 부모','손자녀, 그 배우자','증손자녀, 그 배우자','조부모','형제자매, 그 배우자', '형제자매의 자녀, 그 배우자', '부모의 형제자매, 그 배우자', '기타 친인척', '그외같이사는사람' ))

str(data)
plot(table(data$V5))
plot(table(data$V6))
table(data$V2)
