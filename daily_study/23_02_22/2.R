score <- c(52,66,72,83,91,97)
hour <- c(1,2,3,4,5,6)
shDF <- data.frame(score= score, hour= hour)
plot(score, hour)
shDF
shapiro.test(shDF$score)
shapiro.test(shDF$hour)
sMean <- mean(shDF$score)
hMean <- mean(shDF$hour)

