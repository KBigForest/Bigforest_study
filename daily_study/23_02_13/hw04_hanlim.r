

#2번 자신이 선택한 인포그래픽을 시각화하여 제출
#원생성
theta <- seq(-pi, pi, length=361)# length : 361로 나눈다 (갯수 증가 : 촘촘함 증가)
op <- par(no.readonly = TRUE)
plot(1:30, type = "n", xlab = "", ylab = "", axes = F)
x <- cos(theta)+1.5; y <- sin(theta)+29# x축 및 y축 데이터 할당
x1 <- cos(theta)+2.15; y1 <- sin(theta)+41.5
x_t <- c(1, 1, 2)+2.4
y_t <- c(0, 2, 1)+71.5
rect(0,0,31,31,col ='#f8b307',border = '#f8b307')
polygon(x,y,col='black')# 중심 : (0,0) / 반지름 : 1
polygon(0.7*x1, 0.7*y1,col = 'black',border = '#f8b307')
polygon(0.4*x_t, 0.4*y_t,border = '#f8b307',col = '#f8b307',lwd =1)
x <- c(27, 27.7, 28.4, 27.7)
y <- c(2, 2.2, 10,10)
polygon(x,y,col='#f674a1',border = '#f674a1')
rect(0,3,3,6,border = '#f83604',col = '#f83604')
rect(0,0,14,3.5,border = '#f83604',col = '#f83604')
rect(20,0,23,3,border = '#fc603b',col = '#fc603b')
rect(8,8,31,14,border = '#474745',col = '#474745')
rect(14,14,17.7,16.8,border = '#474745',col = '#474745')
rect(2.5,14,8,17.5,border = '#474745',col = '#474745')

x_t1 <- c(7, 2.25, 7)+1.9
y_t1 <- c(8, 5, 2)+21.7
polygon(0.59*x_t1, 0.59*y_t1,border = '#d8d6cf',col = '#d8d6cf',lwd =1)
x_t1 <- c(7, 2.25, 7)+6.57
polygon(0.59*x_t1, 0.59*y_t1,border = '#d8d6cf',col = '#d8d6cf',lwd =1)

rect(0,21,3,24,border = '#f45933',col = '#f45933')
rect(28,17,31,20,border = '#f45933',col = '#f45933')
rect(26,29,31,31,border = '#fb6bf8',col = '#fb6bf8')
rect(26,27.5,28.5,29,border = '#fb6bf8',col = '#fb6bf8')
text(x=11,y=25,lwd=2,"2",srt=30,cex= 10,col= '#f1655d')
x <- c(0, 0.4,3.4, 3)
y <- c(6, 6,10,10)
polygon(x,y,col='#f1655d',border = '#f1655d')
text(x=20,y=11,lwd=2,"RECAP",cex= 8,col= '#d8d6cf')
x <- c(23.5, 30.5,31, 24)
y <- c(21.5, 22,22.5,22)
polygon(x,y,col='#ef5d3e',border = '#ef5d3e')
x <- c(16, 16.4, 18.4, 18)
y <- c(27.5, 27.55, 31,31)
polygon(x,y,col='#f66f8f',border='#f66f8f')
x <- c(4, 4.5, 6.5, 6)
y <- c(26, 26.4, 24,23.6)
polygon(x,y,col='#ef635f',border = '#ef635f')

