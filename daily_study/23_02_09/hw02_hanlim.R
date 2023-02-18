#11
titanic<-  read.csv('titanic_data.csv')
#12
head(titanic)
#13
dim(titanic)
#14
gender <-  titanic$Sex
write.table(gender, file = 'gender.txt')
#15
sub_data<- titanic[,2:10]
sub_data
write.table(sub_data, file = 'sub_data.txt')
#16
sub_data2 <- titanic[31:100,]
#17
sum(is.na(titanic))
#18
which(is.na(titanic))
#19
which(is.na(titanic),arr.ind = T)
#20
index = which(is.na(titanic$Age))
titanic$Age[index] = 20
#21
Age<- titanic$Age
Age
ifelse(Age>=10 & Age<20, print('10대'),ifelse(Age>= 20 & Age<30,print('20대'),ifelse(Age>= 30 & Age<40, print('30대'),ifelse(Age>= 40 & Age<50, print('40대'),ifelse(Age>=50& Age<60, print('50대'),ifelse(Age>=60& Age<70, print('60대'),print('노약자 or 애기')))))))


titanic$Age
#22
ifelse(titanic$Cabin == "", 'DELETE', titanic$Cabin)
