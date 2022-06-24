data <- read.csv("/tmp/data.csv")
xdata = seq(0, length(data$x0)-1, by=1)
pdf("/tmp/JugglingBallPosition.pdf")

plot(x=data$x0,y=data$y0,main = "Juggling Ball Position",xlab='Horizontal Position',ylab='Vertical Position',col="orange",type="b",ylim=c(0,300),xlim=c(0,300))
points(x=data$x1,y=data$y1,col="green",type="b")
points(x=data$x2,y=data$y2,col="blue",type="b")

legend(x=5, y=300, legend=c("Ball#1", "Ball#2", "Ball#3"),col=c("orange", "green", "blue"),lty=1:2, cex=0.8)
#dev.off()
system('open /tmp/JugglingBallPosition.pdf')