inputa = read.csv("species_COHA_normalized.csv")
inputb = read.csv("rural_pop_US.csv")

## data
input1 <- inputa[,c('decade','AVG')]
input2 <- inputb[,c('YEAR','NORMALIZED')]

## add extra space to right margin of plot within frame
par(mar=c(5, 4, 4, 6) + 0.1)

## Plot first set of data and draw its axis
plot(x = input1$decade,y = input1$AVG, pch=16, axes=FALSE, ylim=c(0.2,1.6), xlim=c(1800,2000), xlab="Year", ylab="Frequency", type="b",col="black", main="Frequency and Rural Pop. COHA")
axis(2, ylim=c(0.2,1.6),col="black",las=1)  ## las=1 makes horizontal labels
mtext("",side=2,line=2.5)
box()

## Allow a second plot on the same graph
par(new=TRUE)

## Plot the second plot and put axis scale on right
plot(x = input2$YEAR,y = input2$NORMALIZED, pch=15,  xlab="", ylab="", ylim=c(0,0.65), xlim=c(1800,2000), yaxt="n", type="b", col="red")

## a little farther out (line=4) to make room for labels
mtext("Rural Pop",side=4,col="red",line=4) 
axis(4, ylim=c(0,0.65), col="red",col.axis="red",las=1)

## Add Legend
legend("topleft",legend=c("Frequency","Rural Pop."),
  text.col=c("black","red"),pch=c(16,15),col=c("black","red"))