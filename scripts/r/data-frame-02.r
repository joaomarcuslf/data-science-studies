# This script will retrieve and csv file then calculate the arithmetic mean of the weights, and the median of heights

table = read.csv("../../data-source/data_file.csv")

mean(table$weight)
median(table$height)

quantile(table$birthyear)
