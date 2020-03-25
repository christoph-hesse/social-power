multi_sim(par,1000,'inter_N1-5_N2-5_d1-0_d2-0',False,True)
multi_sim(par,1000,'inter_N1-5_N2-5_d1-0.5_d2-0',False,True)
multi_sim(par,1000,'inter_N1-5_N2-5_d1-1_d2-0',False,True)
multi_sim(par,1000,'inter_N1-5_N2-5_d1-1.5_d2-0',False,True)
multi_sim(par,1000,'inter_N1-5_N2-5_d1-2_d2-0',False,True)
multi_sim(par,1000,'inter_N1-5_N2-5_d1-2.5_d2-0',False,True)
multi_sim(par,1000,'inter_N1-5_N2-5_d1-3_d2-0',False,True)
multi_sim(par,1000,'inter_N1-5_N2-5_d1-3.5_d2-0',False,True)
multi_sim(par,1000,'inter_N1-5_N2-5_d1-4_d2-0',False,True)
multi_sim(par,1000,'inter_N1-5_N2-5_d1-4.5_d2-0',False,True)

multi_sim(par,1000,'both_N1-2_N2-5_N3-3_d1-0_d2-0_d3-4',False,True)
multi_sim(par,10000,'both_N1-2_N2-5_N3-3_d1-0_d2-0_d3-4___1',False,True)
multi_sim(par,100000,'both_N1-2_N2-5_N3-3_d1-0_d2-0_d3-4___2',False,True)
multi_sim(par,100000,'both_N1-2_N2-5_N3-3_d1-0_d2-0_d3-4___3',False,True)
multi_sim(par,100000,'both_N1-2_N2-5_N3-3_d1-0_d2-0_d3-4___4',False,True)
N3 <- read.table("~/Documents/Mihaela/simulations/ich/csv/both_N1-2_N2-5_N3-3_d1-0_d2-0_d3-4.csv",header=TRUE,sep=",")
N3 <- read.table("~/Documents/Mihaela/simulations/ich/csv/both_N1-2_N2-5_N3-3_d1-0_d2-0_d3-4___1.csv",header=TRUE,sep=",")
N3 <- read.table("~/Documents/Mihaela/simulations/ich/csv/both_N1-2_N2-5_N3-3_d1-0_d2-0_d3-4___2.csv",header=TRUE,sep=",")
N3 <- read.table("~/Documents/Mihaela/simulations/ich/csv/both_N1-2_N2-5_N3-3_d1-0_d2-0_d3-4___3.csv",header=TRUE,sep=",")
N3 <- read.table("~/Documents/Mihaela/simulations/ich/csv/both_N1-2_N2-5_N3-3_d1-0_d2-0_d3-4___4.csv",header=TRUE,sep=",")
s <- subset(N3,N3$b_max==0); vioplot(s$b_L, s$b_M, s$b_H, names=c("L", "M", "H"), col="gold")
s <- subset(N3,N3$b_max==1); vioplot(s$b_L, s$b_M, s$b_H, names=c("L", "M", "H"), col="gold")
s <- subset(N3,N3$b_max==2); vioplot(s$b_L, s$b_M, s$b_H, names=c("L", "M", "H"), col="gold")
x <- c(length(N3$b_max[N3$b_max==0])/length(N3$b_max),length(N3$b_max[N3$b_max==1])/length(N3$b_max),length(N3$b_max[N3$b_max==2])/length(N3$b_max))

vioplot(N3$b_L,N3$r_L,N3$b_M,N3$r_M,N3$b_H,N3$r_H,yaxt='n',at=c(1,2,4,5,7,8),col=rep(c("blue",'red'),3),horizontal=TRUE,las=1,main="Frequency of demands L/M/H\nAverage over 100,000 simulations")
legend(45, 8.75, legend=c("Blue group", "Red group"), col=c("blue", "red"), lty=1,lwd=6, cex=0.6)
axis(side=1)
axis(side=2,labels=c('L','M','H'),at=c(1.5,4.5,7.5),las=2)
mtext("Demands / 100 interactions",side=1,line=2.5)

DF2 <- data.frame(
  group = rep(c("Blue", "Red"), each = nrow(N3)),
  L = c(N3$b_L, N3$r_L),
  M = c(N3$b_M, N3$r_M),
  H = c(N3$b_H, N3$r_H)#,
  #z = rep(rep(1:3, each=5), 2),
  #stringsAsFactors = FALSE
)
boxplot(L~group,M~group,H~group,data=DF2)

d0 <- read.table("~/Documents/Mihaela/simulations/ich/csv/inter_N1-5_N2-5_d1-0_d2-0.csv",header=TRUE,sep=",")
d05 <- read.table("~/Documents/Mihaela/simulations/ich/csv/inter_N1-5_N2-5_d1-0.5_d2-0.csv",header=TRUE,sep=",")
d1 <- read.table("~/Documents/Mihaela/simulations/ich/csv/inter_N1-5_N2-5_d1-1_d2-0.csv",header=TRUE,sep=",")
d15 <- read.table("~/Documents/Mihaela/simulations/ich/csv/inter_N1-5_N2-5_d1-1.5_d2-0.csv",header=TRUE,sep=",")
d2 <- read.table("~/Documents/Mihaela/simulations/ich/csv/inter_N1-5_N2-5_d1-2_d2-0.csv",header=TRUE,sep=",")
d25 <- read.table("~/Documents/Mihaela/simulations/ich/csv/inter_N1-5_N2-5_d1-2.5_d2-0.csv",header=TRUE,sep=",")
d3 <- read.table("~/Documents/Mihaela/simulations/ich/csv/inter_N1-5_N2-5_d1-3_d2-0.csv",header=TRUE,sep=",")
d35 <- read.table("~/Documents/Mihaela/simulations/ich/csv/inter_N1-5_N2-5_d1-3.5_d2-0.csv",header=TRUE,sep=",")
d4 <- read.table("~/Documents/Mihaela/simulations/ich/csv/inter_N1-5_N2-5_d1-4_d2-0.csv",header=TRUE,sep=",")
d45 <- read.table("~/Documents/Mihaela/simulations/ich/csv/inter_N1-5_N2-5_d1-4.5_d2-0.csv",header=TRUE,sep=",")
library(vioplot)
s <- subset(multi,multi$b_max==0); vioplot(s$b_L, s$b_M, s$b_H, names=c("L", "M", "H"), col="gold")
s <- subset(multi,multi$b_max==1); vioplot(s$b_L, s$b_M, s$b_H, names=c("L", "M", "H"), col="gold")
s <- subset(multi,multi$b_max==2); vioplot(s$b_L, s$b_M, s$b_H, names=c("L", "M", "H"), col="gold")
title("Violin Plot")

x1 <- c(length(d0$b_max[d0$b_max==0])/length(d0$b_max),length(d0$b_max[d0$b_max==1])/length(d0$b_max),length(d0$b_max[d0$b_max==2])/length(d0$b_max))
x2 <- c(length(d05$b_max[d05$b_max==0])/length(d05$b_max),length(d05$b_max[d05$b_max==1])/length(d05$b_max),length(d05$b_max[d05$b_max==2])/length(d05$b_max))
x3 <- c(length(d1$b_max[d1$b_max==0])/length(d1$b_max),length(d1$b_max[d1$b_max==1])/length(d1$b_max),length(d1$b_max[d1$b_max==2])/length(d1$b_max))
x4 <- c(length(d15$b_max[d15$b_max==0])/length(d15$b_max),length(d15$b_max[d15$b_max==1])/length(d15$b_max),length(d15$b_max[d15$b_max==2])/length(d15$b_max))
x5 <- c(length(d2$b_max[d2$b_max==0])/length(d2$b_max),length(d2$b_max[d2$b_max==1])/length(d2$b_max),length(d2$b_max[d2$b_max==2])/length(d2$b_max))
x6 <- c(length(d25$b_max[d25$b_max==0])/length(d25$b_max),length(d25$b_max[d25$b_max==1])/length(d25$b_max),length(d25$b_max[d25$b_max==2])/length(d25$b_max))
x7 <- c(length(d3$b_max[d3$b_max==0])/length(d3$b_max),length(d3$b_max[d3$b_max==1])/length(d3$b_max),length(d3$b_max[d3$b_max==2])/length(d3$b_max))
x8 <- c(length(d35$b_max[d35$b_max==0])/length(d35$b_max),length(d35$b_max[d35$b_max==1])/length(d35$b_max),length(d35$b_max[d35$b_max==2])/length(d35$b_max))
x9 <- c(length(d4$b_max[d4$b_max==0])/length(d4$b_max),length(d4$b_max[d4$b_max==1])/length(d4$b_max),length(d4$b_max[d4$b_max==2])/length(d4$b_max))
x10 <- c(length(d45$b_max[d45$b_max==0])/length(d45$b_max),length(d45$b_max[d45$b_max==1])/length(d45$b_max),length(d45$b_max[d45$b_max==2])/length(d45$b_max))
L <- c(x1[1],x2[1],x3[1],x4[1],x5[1],x6[1],x7[1],x8[1],x9[1],x10[1])
M <- c(x1[2],x2[2],x3[2],x4[2],x5[2],x6[2],x7[2],x8[2],x9[2],x10[2])
H <- c(x1[3],x2[3],x3[3],x4[3],x5[3],x6[3],x7[3],x8[3],x9[3],x10[3])

plot(L,ylim=c(0,1), xaxt='n',type='b',col="red",xlab="Disagreement point of blue group",ylab="Proportion of demands")
axis(1, at=1:10, labels=seq(0,4.5,0.5))
legend(0.75, 1, legend=c("L", "M", "H"), col=c("red", "blue","green"), lty=1:3,lwd=1, cex=0.8)
lines(M,lty=2,type='b',col='blue')
lines(H,lty=3,type='b',col='green')

vioplot(d0$b_M,d05$b_M,d1$b_M,d15$b_M,d2$b_M,d25$b_M,d3$b_M,d35$b_M,d4$b_M,d45$b_M,at=seq(1,20,2)-0,names=seq(0,4.5,0.5),col=adjustcolor( "blue", alpha.f = 0.5),xlab="Disagreement point of blue group",ylab="Proportion of demands",border=FALSE)
vioplot(d0$b_L,d05$b_L,d1$b_L,d15$b_L,d2$b_L,d25$b_L,d3$b_L,d35$b_L,d4$b_L,0,at=seq(1,20,2)-0.5,xlim=c(0,12),col=adjustcolor( "red", alpha.f = 0.5),border=FALSE,add=TRUE)
vioplot(d0$b_H,d05$b_H,d1$b_H,d15$b_H,d2$b_H,d25$b_H,d3$b_H,d35$b_H,d4$b_H,d45$b_H,at=seq(1,20,2)+0.5,col=adjustcolor( "green", alpha.f = 0.5),border=FALSE,add=TRUE)
legend(18, 67, legend=c("L", "M", "H"), col=c(col=adjustcolor( "red", alpha.f = 0.5), col=adjustcolor( "blue", alpha.f = 0.5),adjustcolor( "green", alpha.f = 0.5)), lty=1,lwd=6, cex=0.8,box.lwd=0,box.col="white",bg="white")

library(ggplot2)
ggplot2.violinplot(d0$b_H,d05$b_H,d1$b_H,d15$b_H,d2$b_H,d25$b_H,d3$b_H,d35$b_H,d4$b_H,d45$b_H, xName='Disagreement point of blue group',yName='Proportion of demands', addDot=TRUE, dotSize=1, dotPosition="center")


DF2 <- data.frame(
  group = rep(c("Blue", "Red"), each = nrow(N3)),
  L = c(N3$b_L, N3$r_L),
  M = c(N3$b_M, N3$r_M),
  H = c(N3$b_H, N3$r_H)#,
  #z = rep(rep(1:3, each=5), 2),
  #stringsAsFactors = FALSE
)

m <- mean(d0$b_L)
error <- qnorm(0.975)*sd(d0$b_L)/sqrt(length(d0$b_L))

sort(d0$b_L)[round(0.025*length(d0$b_L),0):round(0.975*length(d0$b_L),0)]
sort(d0$b_L)[round(0.025*length(d0$b_L),0)]
sort(d0$b_L)[round(0.975*length(d0$b_L),0)]