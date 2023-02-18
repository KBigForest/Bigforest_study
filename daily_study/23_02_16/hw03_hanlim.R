
#1
for (j in 1:9){
  cat('\n')
  for(i in 1:9){
    cat(i,' * ',j,' = ', i*j,'\t')
    if(i == 5){
      cat('\n')
    }
  }
}


#2
a <- c(1,2,0)
for (z in a){
  for (j in 1:9){
    cat('\n')
    for(i in 1:9){
      if(i%%3==z){
        cat(i,' * ',j,' = ', i*j,'\t')
      }}}}
#3
i = 0
while(i < 6){
  i = i + 1
  if(i <= 2){
    cat('\n',rep('*',2*i-1), rep(' ',8/i),rep('*',2*i-1))}
  else if(i==3){
    cat('\n',rep('*',4*i-2))  
  }else if(i>3 & i<=5){
    cat('\n',rep('*', -2*i +11), rep(' ', 4*i-12), rep('*',-2*i +11))
  }}



#4
sum = 0
for (i in 1:100){
  sum = sum+i
  if(sum>1000){
    cat('\n1000을 넘게하는 수: ',i,', 누적 합: ',sum)
    break}
}

#5
for (i in 50:100){
  if(i %% 2==0){next}
  sum = sum + i
}  
sum

#6
vec <- vector()
cal <- function(x){
  cat('\n벡터의 길이 : ', length(x))
  cat('\n벡터의 원소 합 : ', sum(x))
  cat('\n벡터의 최솟값 : ', min(x))
  cat('\n벡터의 최댓값 : ', max(x))
  cat('\n벡터의 평균 : ',mean(x))
  cat('\n벡터의 분산 : ',var(x))
  
}
x <- 1:10
cal(x)

#7

cal <- function(x, len){
  if(len == 1){
    cat('\n벡터의 길이 : ', length(x))}
  else if(len == 2){
    cat('\n벡터의 원소 합 : ', sum(x))}
  else if(len ==3){
    cat('\n벡터의 최솟값 : ', min(x))}
  else if(len== 4){
    cat('\n벡터의 최댓값 : ', max(x))}
  else if(len == 5){
    cat('\n벡터의 평균 : ',mean(x))}
  else if(len ==6){
    cat('\n벡터의 분산 : ',var(x))}
  else{
    cat('잘못된 파라미터 입력')
  }
}
cal(x,2)

#8
cal <- function(x, len=2){
  if(len == 1){
    cat('\n벡터의 길이 : ', length(x))}
  else if(len == 2){
    cat('\n벡터의 원소 합 : ', sum(x))}
  else if(len ==3){
    cat('\n벡터의 최솟값 : ', min(x))}
  else if(len== 4){
    cat('\n벡터의 최댓값 : ', max(x))}
  else if(len == 5){
    cat('\n벡터의 평균 : ',mean(x))}
  else if(len ==6){
    cat('\n벡터의 분산 : ',var(x))}
  else{
    cat('잘못된 파라미터 입력')
  }
}
cal(x)
#9
googoo <- function(x,y){
  z = c(x,y)
  for(i in z){
    for(j in 1:9){
      cat('\n',i, ' * ', j, ' = ', i*j)}
  }
}
googoo(1,3)