#메트릭스의 행, 열의 통계량을 구할 수 있는 함수
#apply
#apply(xmat, 1, sum)

x_mat <-matrix(rnorm(100),20,5)
apply(x_mat,2,mean)
apply(x_mat,1,sum)
apply(x_mat,2,var)
apply(x_mat,1,var)
#2 col 1 row
myname <- "Hanlim"
paste('My name is',myname,sep = ' ')
file_id =1533
paste('Dataset_',file_id,'.txt',sep = '')

test <-  c('abcdefg','affy1234153')
nchar(test)
f_name <- 'Affy1245820'
#substr(데이터,시작, 끝)
substr(f_name,5,nchar(f_name))

getwd()
setwd('C:/Users/dddf/Desktop/Study/02_09')

dat = data.frame()
dat = edit(dat)
dat

x= scan(file = 'input_noh.txt', what = numeric())
x= scan(file = 'input_noh.txt', what = character())
x= scan(file = 'input_noh.txt')
x

dat = read.table(file = 'input_noh.txt')
dat= read.table(file = 'input_noh.txt')
dat = read.table(file = 'input_noh.txt',header = T)

dat =read.csv(file = 'test3.txt')
dat =read.csv(file = 'test3.txt', stringAsFactor = F)
dat[1]

dat= read.csv(file = 'info.csv')
dat
info <- dat[,c(2,3)]
info
stat_info <- c('평균','중앙값','분산')
mean_info <- apply(info, 2, mean)
mean_info <- as.vector(c('평균',mean_info))
median_info <- apply(info,2, median)
median_info <- as.vector(c('중앙값',median_info))
var_info <- apply(info,2, var)
var_info <- as.vector(c('분산',var_info))

dat[(nrow(dat)+1),] <- mean_info
dat[(nrow(dat)+1),] <- median_info
dat[(nrow(dat)+1),] <- var_info
dat
write.csv(dat,'작업후info.csv', fileEncoding = 'CP949')


x <- 1:10
cat(x, file= 'x.txt', sep= '\n')
cat(x, sep = '\t')
cat('\n',1,'st element of x =',x[1])

x1 <- 1:20
x2 <- rep(c('a','b','b','a'),5)
x3 <- rep(c(T,F),each =10)
dat <- cbind(x1,x2,x3)
write.table(dat, file ='test1.txt', row.names = T,col.names = T, quote = T, sep= 't')
write.table(dat, file ='test2.txt', row.names = F,col.names = F, quote = F, sep= '\n')
write.table(dat, file ='test3.txt',sep= ',')
#메트릭스는 rowname을 설정가능
#데이터프레임은 인덱스로 고정

dat = read.csv((file = 'text3.txt'))
head(dat)
tail(dat)
length(dat[,1])
dim(dat)[1]
dim(dat)[2]
nrow(dat);ncol(dat)

head(dat,20)
tail(dat,10)

x <- matrix(c(NA,1,3,NA,NA,2),3,2)
a=is.na(x)
sum(a)

which(is.na(x))
which(is.na(x),arr.ind = T)
which(is.na(x),T)


x <- 1:5
y <- -2:2
if(any(x>0)){print(x)}
if(any(y<0)){print(abs(y))}
if(any(y<0)){
  print(abs(y))
  cat('\n y contain negative values')
}

if(pi>3){cat('\n expr(T)')}else{cat('\n expr(F)')}
if(pi<3){cat('\n expr(T)')}else{cat('\n expr(F)')}
x <- 1:5
if(length(x)==5){
  if(sum(x)== 15){
    cat('\n Vector x length =',length(x),',sum =',sum(x))
  }else{cat('\n Vector x length !=',length(x))}
}



a=1; b=2;c=-3
D = b^2-4*a*c
D
if(D<0){
  print('No roots')
}else{
  x1 = (-b-sqrt(D))/2*a
  x2 = (-b+sqrt(D))/2*a
  cat('\n x값은 ',x1,', ', x2)
}

score <- c(80,75,40, 98)
grade= ifelse(score>=50, 'pass','fail')
data.frame(score,grade)


y <- -2:2
ifelse(y>=0,y,-y)
abs(y)
tmp <- c(3,-1,1,-2,0)
sn <- ifelse(tmp>0 ,'pos',ifelse(tmp<0,'neg', 'zero'))
data.frame(tmp,sn)

x <- c(1,3,2,5,2)
i <- 2
switch(i,mean(x),median(x),sd(x),var(x))
type <- 'mean'
switch (i,
        mean = mean(x),
        sd = sd(x),
        var= var(x))
type='mean'
if(type == 'mean'){mean(x)}else if(type =='median'){median(x)}else if(type == 'sd'){sd(x)}else if(type =='var'){var(x)}else{print('포함X')}

#else{print('잘못입력이요')}
#
x <- c(1,3,2,5,2)
if(sum(x)>5){
  cat('\n sum(x) is greater than 5')
}else if(sum(x)<5){
  cat('\n sum(x) is less than 5')
}else{
  cat('\n sum(x) is equal to 5')
}

y =x[x>3] - 3
y
y <- ifelse(x>3, x-3,x)
y
x
i <- 1

switch(i, x+y, x-y, x*y)
score = 10
ifelse(score>=90,'A',
       ifelse(score>= 80, 'B',
        ifelse(score>=70, 'C','D')))

type='sqrt'
score=65
switch(type, sqrt = sqrt(score), square = score^2, log= log(score))

       
