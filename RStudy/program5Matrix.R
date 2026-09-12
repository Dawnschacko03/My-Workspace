x<-matrix(data=c(1,2,3,4,5,6),nrow=3,ncol=2, byrow=FALSE)
x
x<-rbind(x,c(3,4))
x
x<-cbind(x,c(7,8,9,10))
x

y<-matrix(seq(10,15,1),3,2,FALSE)
y<-cbind(y,c(16,17,18))
y<-rbind(y,c(19,20,21))
y

sol