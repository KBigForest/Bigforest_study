getwd()
setwd('C:/Users/dddf/Desktop/Bigforest_study/daily_study/23_02_20')
getwd()
taxi <- read.csv('taxis.csv')
str(taxi)
colnames(taxi)
sum(is.na(taxi))

summary(taxi$passengers)

idx


taxi <- taxi[-which(taxi$passengers == 0),]
taxi <- taxi[-which(taxi$distance ==0),]
taxi <- taxi[-which(taxi$payment ==''),]


summary(colnames(taxi))

taxi$passengers
boxplot(taxi$passengers, main = '승객')
taxi$passengers<- as.factor(taxi$passengers)
taxi$passengers



season1 <- heat.colors(8, alpha=1)
season2 <-rainbow(8, s = 1, v = 1, start = 0, end = max(1,8 - 1)/8, alpha = 0.7)

season3 <-terrain.colors(8, alpha = 1)
lab = round(table(taxi$passengers)/sum(table(taxi$passengers))*100,1)
lab1= paste(lab,'%',' ',levels(taxi$passengers),'명')
lab2 = paste(levels(taxi$passengers),'명')
pie(table(taxi$passengers),col = season2,main = '승객 수 분포',xlab ='탑승인원',label = lab1,border=season2)

legend("topright", lab2 ,fill=season2)

pass= plot(taxi$passengers,ylim =c(0,5000),col = season2,main = '승객 수 분포',xlab = '탑승인원')
legend("topright", lab2 ,fill=season2)




plot(taxi$payment)
taxi <- taxi[-which(taxi$payment ==''),]
taxi$payment<- as.factor(taxi$payment)
par(mfrow=c(1,2))
lab = round(table(taxi$payment)/sum(table(taxi$payment))*100,1)
lab= paste(lab,'%')
pie(table(taxi$payment), main = '현금과 신용카드 이용 수 파이그래프',col=rainbow(2),label = lab)
name = c('cash', 'card')
legend("topright", name ,fill=rainbow(2))
paypay2= barplot(table(taxi$payment), main = '현금과 신용카드 이용 수 비교',col=rainbow(2),ylim =c(0,6000))
text(x=paypay2,y=table(taxi$payment),labels=table(taxi$payment),pos=3,col="black")
legend("topright", name ,fill=rainbow(2))

summary(taxi$tip)
table(taxi$tip)


rank2group <- function (y,k=4){
  count=length(y)
  z=rank(y,ties.method="min")
  return(floor((z-1)/(count/k))+1)
}
taxi$tipGroup=rank2group(taxi$tip,5)
plot(table(taxi$tipGroup))

taxi[which.max(taxi$tip),]
par(mfrow = c(1,2))
z = hist(taxi$tip, main = 'Histogram of tip', col = 'lightblue',xlab = 'tip($)',ylim = c(0,4000))
boxplot(taxi$tip, main = 'Boxplot of tip', col = 'pink')
summary(taxi)
  
season3 <-terrain.colors(8, alpha = 1)
season4 <-topo.colors(8, alpha = 1)
par(mfrow = c(1,2))
z = hist(taxi$fare, main = 'Histogram of fare', col = season4,xlab = 'tip($)',ylim = c(0,4000))
boxplot(taxi$fare, main = 'Boxplot of fare', col = season4)


taxi$color<- as.factor(taxi$color)
table(taxi$color)
taxicolor <- c('lightgreen','yellow')
lab = round(table(taxi$color)/sum(table(taxi$color))*100,1)
lab= paste(lab,'%', ' ',levels(taxi$color))
pie(table(taxi$color), main = '택시 색깔',col=taxicolor,label = lab,border = taxicolor,clockwise=TRUE,density = 90)
name = c('green', 'yellow')
legend("topright", name ,fill=taxicolor)
paypay2= barplot(table(taxi$color),border = taxicolor, main = '택시색깔',col=taxicolor,ylim =c(0,7000),density = 90)
text(x=paypay2,y=table(taxi$color),labels=table(taxi$color),pos=3,col="black")
legend("topright", name ,fill=taxicolor)

summary(taxi)
table(taxi$tolls)
taxi
summary(taxi$total)
mean(taxi$total, trim = 0.1)

var(taxi$tip)
mean(taxi$tip)

SU
library(dplyr)
cash <- taxi %>% select(tip, payment) %>% 
  filter(payment =='cash')
summary(cash)
credit_card <- taxi %>% select(tip, payment) %>% 
  filter(payment =='credit card')
summary(credit_card)
hist(table(cash$tip))
plot(cash$tip,credit_card$tip)

t.test(x=cash$tip, y=credit_card$tip, paired=F, alternative="less", var.equal=F)


test2<- taxi %>% select(passengers, fare)
levels(test2$passengers)
model2 = aov(fare~passengers, data = test2)
summary(model2)



test2<- taxi %>% select(passengers, fare)
levels(test2$passengers)
model2 = aov(fare~passengers, data = test2)
summary(model2)


test3<- taxi %>% select(passengers, distance)
levels(test2$passengers)
model3 = aov(distance~passengers, data = test3)
summary(model3)


greenpass <- taxi %>% select(color, passengers) %>% filter(color == 'green')
yellowpass <- taxi %>% select(color, passengers) %>% filter(color == 'yellow')

greenpass$passengers<- as.numeric(greenpass$passengers)
yellowpass$passengers <- as.numeric(yellowpass$passengers)
t.test(x=greenpass$passengers, y=yellowpass$passengers, paired=F, alternative="less", var.equal=F)




greentot <- taxi %>% select(color, total) %>% filter(color == 'green')
yellowtot <- taxi %>% select(color, total) %>% filter(color == 'yellow')

t.test(x=greentot$total, y=yellowtot$total, paired=F, alternative="less", var.equal=FALSE)


greendist <- taxi %>% select(color, distance) %>% filter(color == 'green')
yellowdist <- taxi %>% select(color, distance) %>% filter(color == 'yellow')

t.test(x=yellowdist$distance, y=greendist$distance, paired=F, alternative="less", var.equal=F)



taxi$tollyesno <- ifelse(taxi$tolls > 0, 'yes', 'no')
taxi$tollyesno <- as.factor(taxi$tollyesno)
tollyestotal <- taxi %>% select(tollyesno, total) %>% filter(tollyesno == 'yes')
tollnototal <- taxi %>% select(tollyesno, total) %>% filter(tollyesno == 'no')
t.test(x=tollnototal$total, y=tollyestotal$total, paired=F, alternative="less", var.equal=F)


tollyespassenger <- taxi %>% select(tollyesno, passengers) %>% filter(tollyesno == 'yes')
tollnopassenger <- taxi %>% select(tollyesno, passengers) %>% filter(tollyesno == 'no')
tollyespassenger$passengers<- as.numeric(tollyespassenger$passengers)
tollnopassenger$passengers <- as.numeric(tollnopassenger$passengers)
t.test(x=tollnopassenger$passengers, y=tollyespassenger$passengers, paired=F, alternative="less", var.equal=F)
