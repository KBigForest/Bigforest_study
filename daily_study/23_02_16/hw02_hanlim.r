#1번 문제
df<- data.frame(Var1 = c(1,2,3,4,5,6))
df
df_1 <- data.frame(table(sample(1:6, 12, replace = T, prob = c(1/6,1/6,1/6,1/6,1/6,1/6))))
df_2 <- data.frame(table(sample(1:6, 1200, replace = T, prob = c(1/6,1/6,1/6,1/6,1/6,1/6))))
df_3 <- data.frame(table(sample(1:6, 12000000, replace = T, prob = c(1/6,1/6,1/6,1/6,1/6,1/6))))
mergedf1 <- merge(df,df_1 ,all = T)
mergedf1
mergedf2 <- cbind(mergedf1, df_2) 
mergedf2
mergedf3 <- cbind(mergedf2, df_3) 
mergedf3 <- mergedf3[,c(-1,-3,-5)]
finishdf <- t(mergedf3)
colnames(finishdf) <- c('1의 눈', '2의 눈', '3의 눈', '4의 눈', '5의 눈', '6의 눈')
row.names(finishdf) <- c('12','120','12000000')
finishdf
par(mfrow=c(3,1))
barplot(finishdf[1,], names = colnames(finishdf),main = 'n = 12')
barplot(finishdf[2,], names = colnames(finishdf),main = 'n = 120')
barplot(finishdf[3,], names = colnames(finishdf),main = 'n = 12000000')

# 2번 문제
par(mfrow = c(1,3))
a <- seq(0,10,1)
plot(a,dbinom(a,10,0.5),type= 'l',main = '')
#확률 상 5번을 기록할 확률이 높다는 것을 알 수 있다.
a <- seq(0,10,1)
plot(a,dbinom(a,10,0.1),type= 'l')
#이항분포 상 그래프를 보게되면 성공확률 0.1일때는 1번 성공할 확률이 높은 것으로 보인다. 실제로 E(x) = np 값은 1이다. 평균적으로 한번 성공한다는 의미
a <- seq(0,10,1)
plot(a,dbinom(a,10,0.9),type= 'l')
#반대로 해당 그래프는 성공확률 0.9이므로 그래프도 오른쪽에 치우쳐져 있음을 확인할 수 있다. E(x)값은 9이다. 평균적으로 9번 성공한다는 의미이다.
#

# 3번 정규분포 관련 문제입니다
#국민소득 평균이 표준편차가 인 정규분포 $30,000, $10,000
#확률변수 를 개인의 소득을 나타내는 확률변수라 할 때 X ,
#어떤 사람의 소득이 사이에 있을 확률 계산 및 그래프로 $25,000 ~ $35,000 표현해 주세요.
#어떤 사람의 소득이 사이에 있을 확률
library(ggplot2)
pnorm(35000,30000,10000) - pnorm(25000,30000,10000)
#그래프로 $25,000 ~ $35,000 표현
ggplot(data.frame(x = c(0, 60000)), aes(x=x)) +
    stat_function(fun=dnorm, args=list(mean=30000, sd=10000), colour="black", size=1.5)+
    geom_area(stat='function', fun=dnorm, args=list(mean=30000, sd=10000), xlim=c(25000,35000), fill='gray75')+
  geom_vline(xintercept=25000)+
  geom_vline(xintercept = 35000)+
  ggtitle('소득 그래프 정규분포')
    
  