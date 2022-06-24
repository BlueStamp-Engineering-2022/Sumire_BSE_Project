data <- read.csv("/tmp/data.csv")
xdata = seq(0, length(data$x0)-1, by=1)
pdf("/tmp/JugglingBallHeight.pdf")

plot(x=xdata,y=data$y0,main = "Juggling Ball Height Across Time",xlab='Capture',ylab='Vertical Position',pch=16,col="orange",type="b",ylim=c(0,300))
points(x=xdata,y=data$y1,col="green",pch=16,type="b")
points(x=xdata,y=data$y2,col="blue",pch=16,type="b")

legend(x=0, y=300, legend=c("Ball#1", "Ball#2", "Ball#3"),col=c("orange", "green", "blue"),lty=1:2, cex=0.8)
#dev.off()
system('open /tmp/JugglingBallHeight.pdf')