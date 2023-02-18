#1
x <- seq(1,30,2)
#2
y <- rep(c('A','B','C'),10)
#3
z <- rep(c(0,1),15)
z
length(z)
#4
z1 <- as.character(z)
length(z1)
xmat <- matrix(x,6,5,byrow= T)
#5
lst1 <- list(x,y,z)
#6
dat <- data.frame(x,y,z1, stringsAsFactors = F)
#7
dat[,c(2,3)]
#8
dat[,c(1,3)]
#9
sum(x[x>10 & x<20])
#10
#각 행의 합
sum(xmat[1,])
sum(xmat[2,])
sum(xmat[3,])
sum(xmat[4,])
sum(xmat[5,])
sum(xmat[6,])
#각 열의 평균
mean(xmat[,1])
mean(xmat[,2])
mean(xmat[,3])
mean(xmat[,4])
mean(xmat[,5])
#각 열의 분산
var(xmat[,1])
var(xmat[,2])
var(xmat[,3])
var(xmat[,4])
var(xmat[,5])


