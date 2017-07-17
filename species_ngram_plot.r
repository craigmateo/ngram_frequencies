
# Get the input values.
input <- species_ngram_NA_normalized[,c('year','AVG')]

png(file = "scatterplot.png")

plot(x = input$wt,y = input$mpg,
   xlab = "Year",
   ylab = "Relative Frequency",	
   xlim = c(1800,2000),
   ylim = c(0.4,1.6), 
   main = "Frequency"
)
	 
dev.off()