x <- rbinom(10,1,0.5)
x
sum(x)/10

x <- rbinom(100,1,0.5)
x
mean(x)
rbinom()
x <- rbinom(1000,1,0.5)
mean(x)
sample(1:10,3)
sample(1:2,2)

sample(1:2,10,replace = T)
sample(1:2,10,replace = T, prob = c(0.8,0.2))
runif(10)


x <- c(0,1,2)
px <- c(0.25, 0.5, 0.25)
ex <- sum(x*px)
sum((ex-x)^2)/(2)

runif(1)
runif(10,min=1,max=10)

set.seed(2022)
hist(runif(100,0,100))
hist(runif(1000,0,100))
hist(runif(1000000,0,100))

a <- seq(0,50,1)
a
b <- dbinom(a,50,0.2)
par(mfrow=c(1,2))
plot(a,b)
b <- dbinom(a,50,0.6)
plot(a,b)
#
#이항분포 누적확률 분포
pbinom(3,10,0.2)
#동일
1- pbinom(3,10,0.2)
pbinom(3,10,0.2,lower.tail = F)

set.seed(123)
x <- rbinom(0,)
x <- rnorm(1000,172,10)
hist(x,col = 'blue',breaks = 30)
x <- rnorm(1000100,0,1)
hist(x,col = 'blue',breaks = 30)


qnorm(p= 0.05, mean = 172, sd = 1)
