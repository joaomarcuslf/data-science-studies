# This script will retrieve and csv file then generate two computed data row, and then save the csv again
# without computed data
# It will create subsets based on IMC

table = read.csv("../../data-source/data_file.csv")
table = table[,-1]

table$age = 2020-table$birthyear
table$imc = table$weight/(table$height)^2

underweight_imc = table[table$imc < 18.5, ]
good_imc = table[table$imc >= 18.5 & table$imc <= 24.5, ]
overweight_imc = table[table$imc > 24.5 & table$imc <= 29.9, ]
obese_imc = table[table$imc >= 30,]

format_table = table

age_index = - match("age",names(format_table))
format_table = format_table[,age_index]

imc_index = - match("imc",names(format_table))
format_table = format_table[,imc_index]


write.csv(format_table, "../data-source/data_file.csv")