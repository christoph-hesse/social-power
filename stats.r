# ==============================================================
# Author: Christoph Hesse (Apr 2020)
# ==============================================================

# Merge multiple csv files into one big file, but onlt have one header in the first line of the big file
# In terminal, navigate to directory with csv files and use the command:
# awk '(NR == 1) || (FNR > 1)' *.csv > bigfile.csv

make_plot <- function() {
	fair <- subset(orig,orig$strat1==5.&orig$strat2==5.)
	boxplot(fair$fin_d1,fair$fin_d3,fair$fin_d2,ylim=c(0,6),col=c('#0099FF','#FFAA33','#FF4400'),xaxt='n',yaxt='n',las=1,medcol=c('#0066CC','#CC6633','#CC3300'))
	axis(side=2,labels=FALSE,line=0,at=c(0:6),tck = 0.025,las=1)
	axis(side=4,labels=FALSE,line=0,at=c(0:6),tck = 0.025,las=1)
	lines(x=c(0.5,1.5),y=rep(unique(fair$ini_d1),2),lwd=3,col='#0066CC')
	lines(x=c(1.5,2.5),y=rep(unique(fair$ini_d3),2),lwd=3,col='#CC6633')
	lines(x=c(2.5,3.5),y=rep(unique(fair$ini_d2),2),lwd=3,col='#CC3300')
	text(2,6.2,paste("Fair",round(nrow(fair)/nrow(orig)*100,1),"%"),pos=1,col="black",cex=1)
}

# =================================================================
# update_d.py version 2
# Create boxplots in 3x3 square layout
# proportion of racists ~ slur strength (d1=d2=d3=4,aud_str=0.25)
# =================================================================
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d2/d1-4_d2-4_d3-4_N3-1_aud_str-0.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=2,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=2,line=1.25,outer=FALSE,cex=.5)
legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d2/d1-4_d2-4_d3-4_N3-2_aud_str-0.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d2/d1-4_d2-4_d3-4_N3-4_aud_str-0.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
legend("topright",inset=c(0.5,-0.5),title="Final disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=FALSE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d2/d1-4_d2-4_d3-4_N3-1_aud_str-0.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c(0,0.5,1),at=c(-3.5,3,9.5),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d2/d1-4_d2-4_d3-4_N3-2_aud_str-0.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d2/d1-4_d2-4_d3-4_N3-4_aud_str-0.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d2/d1-4_d2-4_d3-4_N3-1_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d2/d1-4_d2-4_d3-4_N3-2_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c("1/5","2/5","4/5"),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d2/d1-4_d2-4_d3-4_N3-4_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=4,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Proportion of racists",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Slur strength",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label






make_plot <- function() {
	fair <- subset(orig,orig$strat1==5.&orig$strat2==5.)
	boxplot((fair$fin_b1-fair$fin_d1),(fair$fin_b3-fair$fin_d3),(fair$fin_b2-fair$fin_d2),ylim=c(-7,7),col=c('#0099FF','#FFAA33','#FF4400'),xaxt='n',yaxt='n',las=1,medcol=c('#0066CC','#CC6633','#CC3300'))
	axis(side=2,labels=FALSE,line=0,at=c(-6,-4,-2,0,2,4,6),tck = 0.025,las=1)
	axis(side=4,labels=FALSE,line=0,at=c(-6,-4,-2,0,2,4,6),tck = 0.025,las=1)
	abline(h=0)
	#lines(x=c(0.5,1.5),y=rep(unique(fair$ini_d1),2),lwd=3,col='#0066CC')
	#lines(x=c(1.5,2.5),y=rep(unique(fair$ini_d3),2),lwd=3,col='#CC6633')
	#lines(x=c(2.5,3.5),y=rep(unique(fair$ini_d2),2),lwd=3,col='#CC3300')
	text(2,7.2,paste("Fair",round(nrow(fair)/nrow(orig)*100,1),"%"),pos=1,col="black",cex=1)
}

# =================================================================
# update_d.py version 3
# Create boxplots in 3x3 square layout
# proportion of racists ~ slur strength (d1=d2=d3=4,aud_str=0.25)
# =================================================================
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-4_N2-5_N3-1_d1-4_d2-4_d3-4_m-4_sl_str-1_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(-6,-4,-2,0,2,4,6),side=2,line=0.5,at=c(-6,-4,-2,0,2,4,6),las=1,cex=.5); mtext(text="Difference (beliefs - actual)",side=2,line=1.25,outer=FALSE,cex=.5)
#legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-3_N2-5_N3-2_d1-4_d2-4_d3-4_m-4_sl_str-1_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
legend("top",inset=c(0.5,-0.35),title="Beliefs about final disagreement points minus actual disagreement points",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=TRUE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-1_N2-5_N3-4_d1-4_d2-4_d3-4_m-4_sl_str-1_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-4_N2-5_N3-1_d1-4_d2-4_d3-4_m-4_sl_str-0.50_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c(0,0.5,1),at=c(-15,0,15),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-3_N2-5_N3-2_d1-4_d2-4_d3-4_m-4_sl_str-0.50_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-1_N2-5_N3-4_d1-4_d2-4_d3-4_m-4_sl_str-0.50_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-4_N2-5_N3-1_d1-4_d2-4_d3-4_m-4_sl_str-0_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-3_N2-5_N3-2_d1-4_d2-4_d3-4_m-4_sl_str-0_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c("1/5","2/5","4/5"),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-1_N2-5_N3-4_d1-4_d2-4_d3-4_m-4_sl_str-0_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(-6,-4,-2,0,2,4,6),side=4,line=0.5,at=c(-6,-4,-2,0,2,4,6),las=1,cex=.5); mtext(text="Difference (beliefs - actual)",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Proportion of racists",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Slur strength",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label


# Create boxplots in 3x3 square layout
# proportion of racists ~ slur strength (d1=d2=d3=4,aud_str=0.25)
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-4_N2-5_N3-1_d1-4_d2-4_d3-4_m-4_sl_str-0.75_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(-6,-4,-2,0,2,4,6),side=2,line=0.5,at=c(-6,-4,-2,0,2,4,6),las=1,cex=.5); mtext(text="Difference (beliefs - actual)",side=2,line=1.25,outer=FALSE,cex=.5)
#legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-3_N2-5_N3-2_d1-4_d2-4_d3-4_m-4_sl_str-0.75_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
legend("top",inset=c(0.5,-0.35),title="Beliefs about final disagreement points minus actual disagreement points",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=TRUE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-1_N2-5_N3-4_d1-4_d2-4_d3-4_m-4_sl_str-0.75_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-4_N2-5_N3-1_d1-4_d2-4_d3-4_m-4_sl_str-0.50_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c(0.25,0.50,0.75),at=c(-15,0,15),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-3_N2-5_N3-2_d1-4_d2-4_d3-4_m-4_sl_str-0.50_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-1_N2-5_N3-4_d1-4_d2-4_d3-4_m-4_sl_str-0.50_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-4_N2-5_N3-1_d1-4_d2-4_d3-4_m-4_sl_str-0.25_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-3_N2-5_N3-2_d1-4_d2-4_d3-4_m-4_sl_str-0.25_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c("1/5","2/5","4/5"),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/update_d3b/N1-1_N2-5_N3-4_d1-4_d2-4_d3-4_m-4_sl_str-0.25_aud_str-0.25.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(-6,-4,-2,0,2,4,6),side=4,line=0.5,at=c(-6,-4,-2,0,2,4,6),las=1,cex=.5); mtext(text="Difference (beliefs - actual)",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Proportion of racists",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Slur strength",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label







t.test(test$fin_d1,test$fin_d2)# = t = 5.3883, df = 197.83, p-value = 2.01e-07 ***, mean of fin_d1 = 2.971875, mean of fin_d2 = 2.298125, 95% CI = 0.4271689, 0.9203311
t.test(test$fin_d1,test$fin_d3)# t = 2.0685, df = 185.2, p-value = 0.03998 *, mean of fin_d1 = 2.971875, mean of fin_d3 = 2.675, 95% CI = 0.01372606, 0.58002394




















# Create boxplots in 3x3 square layout
# d3 ~ slur strenth
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-4.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=2,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=2,line=1.25,outer=FALSE,cex=.5)
legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-4.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-4.5_sl_str-2.csv",header=TRUE,sep=","); make_plot()
legend("topright",inset=c(0.5,-0.5),title="Final disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=FALSE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-3_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c(1,3,4.5),at=c(-3.5,3,9.5),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-3_sl_str-1.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-3_sl_str-2.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-1_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-1_sl_str-1.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c(0,1,2),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-1_sl_str-2.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=4,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Slur strength",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Racist Blues' initial disagreement point",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label


# Create boxplots in 3x3 square layout
# gap in initial bargaining power between Blues & Reds ~ slur strength
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_sl_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=2,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=2,line=1.25,outer=FALSE,cex=.5)
legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_sl_str-1.csv",header=TRUE,sep=","); make_plot()
legend("topright",inset=c(0.5,-0.5),title="Final disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=FALSE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3.5_d2-2_d3-3.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c("3 - 3 = 0","3.5 - 2 = 1.5","4 - 1 = 3"),at=c(-3.5,3,9.5),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3.5_d2-2_d3-3.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3.5_d2-2_d3-3.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-3_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-3_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c(0,0.5,1),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-3_sl_str-1.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=4,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Slur strength",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Gap in bargaining power between Blues & Reds",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label


# Create boxplots in 3x3 square layout
# gap in initial bargaining power between Blues & Reds ~ audience strength
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=2,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=2,line=1.25,outer=FALSE,cex=.5)
legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.25_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.5.csv",header=TRUE,sep=","); make_plot()
legend("topright",inset=c(0.5,-0.5),title="Final disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=FALSE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3.5_d2-2_d3-3.5_N3-1_aud_str-0_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c("3 - 3 = 0","3.5 - 2 = 1.5","4 - 1 = 3"),at=c(-3.5,3,9.5),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3.5_d2-2_d3-3.5_N3-1_aud_str-0.25_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3.5_d2-2_d3-3.5_N3-1_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3_d2-3_d3-3_N3-1_aud_str-0_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3_d2-3_d3-3_N3-1_aud_str-0.25_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c(0,0.25,0.5),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-3_sl_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=4,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Audience strength",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Gap in bargaining power between Blues & Reds",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label


# Create boxplots in 3x3 square layout
# gap in initial bargaining power between Blues & Reds ~ audience strength
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=2,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=2,line=1.25,outer=FALSE,cex=.5)
legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-1_sl_str-0.csv",header=TRUE,sep=","); make_plot()
legend("topright",inset=c(0.5,-0.5),title="Final disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=FALSE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3.5_d2-2_d3-3.5_N3-1_aud_str-0_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c("3 - 3 = 0","3.5 - 2 = 1.5","4 - 1 = 3"),at=c(-3.5,3,9.5),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3.5_d2-2_d3-3.5_N3-1_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3.5_d2-2_d3-3.5_N3-1_aud_str-1_sl_str-0.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3_d2-3_d3-3_N3-1_aud_str-0_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d3-3_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c(0,0.5,1),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-3_d2-3_d3-3_N3-1_aud_str-1_sl_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=4,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Audience strength",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Gap in bargaining power between Blues & Reds",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label


# Create boxplots in 3x3 square layout
# audience strength ~ slur strength (d1=d2=d3=4)
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-1_sl_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=2,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=2,line=1.25,outer=FALSE,cex=.5)
legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-1_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-1_sl_str-1.csv",header=TRUE,sep=","); make_plot()
legend("topright",inset=c(0.5,-0.5),title="Final disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=FALSE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c(0,0.5,1),at=c(-3.5,3,9.5),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-0.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-0.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-0_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-0_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c(0,0.5,1),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-0_sl_str-1.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=4,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Slur strength",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Audience strength",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label


# Create boxplots in 3x3 square layout
# audience strength ~ slur strength (d1=d3=4,d2=1)
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-1_sl_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=2,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=2,line=1.25,outer=FALSE,cex=.5)
legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-1_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-1_sl_str-1.csv",header=TRUE,sep=","); make_plot()
legend("topright",inset=c(0.5,-0.5),title="Final disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=FALSE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c(0,0.5,1),at=c(-3.5,3,9.5),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c(0,0.5,1),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0_sl_str-1.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=4,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Slur strength",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Audience strength",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label


# Create boxplots in 3x3 square layout
# proportion of racists ~ audience strength (d1=d2=d3=4)
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-1_sl_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=2,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=2,line=1.25,outer=FALSE,cex=.5)
legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-2_aud_str-1.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-4_aud_str-1.csv",header=TRUE,sep=","); make_plot()
legend("topright",inset=c(0.5,-0.5),title="Final disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=FALSE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c(0,0.5,1),at=c(-3.5,3,9.5),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-2_aud_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-4_aud_str-0.5.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_aud_str-0_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-2_aud_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c("1/5","2/5","4/5"),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-4_aud_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=4,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Proportion of racists",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Audience strength",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label


# Create boxplots in 3x3 square layout
# proportion of racists ~ audience strength (d1=d3=4,d2=1)
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-1.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=2,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=2,line=1.25,outer=FALSE,cex=.5)
legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-2_aud_str-1.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-4_aud_str-1.csv",header=TRUE,sep=","); make_plot()
legend("topright",inset=c(0.5,-0.5),title="Final disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=FALSE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.5.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c(0,0.5,1),at=c(-3.5,3,9.5),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-2_aud_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-4_aud_str-0.5.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-2_aud_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c("1/5","2/5","4/5"),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-4_aud_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=4,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Proportion of racists",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Audience strength",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label


# Create boxplots in 3x3 square layout
# proportion of racists ~ slur strength (d1=d2=d3=4,aud_str=0.5)
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-1_aud_str-0.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=2,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=2,line=1.25,outer=FALSE,cex=.5)
legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-2_aud_str-0.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-4_aud_str-0.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
legend("topright",inset=c(0.5,-0.5),title="Final disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=FALSE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-1_aud_str-0.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c(0,0.5,1),at=c(-3.5,3,9.5),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-2_aud_str-0.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-4_aud_str-0.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-1_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-2_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c("1/5","2/5","4/5"),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-4_d3-4_N3-4_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=4,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Proportion of racists",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Slur strength",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label


# Create boxplots in 3x3 square layout
# proportion of racists ~ slur strength (d1=d3=4,d2=1,aud_str=0.5)
par(oma=c(4,6,4,2),mfrow=c(3,3),mar=c(0,0,0,0))
# first row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=2,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=2,line=1.25,outer=FALSE,cex=.5)
legend("topleft",inset=c(0.5,-0.5),title="Initial disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),col=c('#0066CC','#CC6633','#CC3300'),lty=1,lwd=3,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-2_aud_str-0.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-4_aud_str-0.5_sl_str-1.csv",header=TRUE,sep=","); make_plot()
legend("topright",inset=c(0.5,-0.5),title="Final disagreement point",xjust=0,legend=c("Non-racist Blues","Racist Blues","Reds"),fill=c('#0099FF','#FFAA33','#FF4400'),horiz=FALSE,cex=.8,xpd=NA,x.intersp=0.75,y.intersp=0.75)
# second row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
axis(side=2,line=2.5,labels=c(0,0.5,1),at=c(-3.5,3,9.5),xpd=NA,outer=TRUE)# common y-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-2_aud_str-0.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-4_aud_str-0.5_sl_str-0.5.csv",header=TRUE,sep=","); make_plot()
# third row
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-1_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-2_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
axis(side=1,line=1,labels=c("1/5","2/5","4/5"),at=c(-1.25,2,5.25),xpd=NA,outer=TRUE)# common x-axis
orig <- read.table("~/Documents/Mihaela/simulations/ich/csv/d1-4_d2-1_d3-4_N3-4_aud_str-0.5_sl_str-0.csv",header=TRUE,sep=","); make_plot()
mtext(text=c(0:6),side=4,line=0.5,at=c(0:6),las=1,cex=.5); mtext(text="Disagreement point",side=4,line=1,outer=FALSE,cex=.5)
mtext(text="Proportion of racists",side=1,line=3,outer=TRUE,cex=.8)# common x-axis label
mtext(text="Slur strength",side=2,line=4.5,outer=TRUE,cex=.8)# common y-axis label