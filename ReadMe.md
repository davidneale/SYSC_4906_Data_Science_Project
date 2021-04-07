*****************************************************
Multiple Regression Modelling
*****************************************************


*****************************************************
Introduction
*****************************************************
In 2020, the world was heavily hit by COVID – 19, and 
it has been more than a year since January 2020. We 
aimed to take statistics with data from open dataset 
from websites to analyse, summarize and introspect the 
effect of COVID-19 on Ottawa citizens. This project 
adopts the multiple regression modelling in machine 
learning, quantifying the happiness index with the 
impact factors of Reproduction number, Confirmed 
Cases, Employment Rate, and Unemployment Rate. 
Results showed that all the independent variables 
have association to the happiness index, with a 
satisfied R-squared of more than 0.79.


*****************************************************
Data obtained
*****************************************************
The daily CC and R value were downloaded from Ottawa 
city Open data (Open Ottawa, n.d.) which are available 
from March of 2020. In particular, R is known as the 
average level of secondary cases per infectious case 
in a population made up of both susceptible and 
non-susceptible hosts (batista, 2020). R greater than 
1 means that the number of cases increases, R smaller 
than 1 means that the number of cases decreases.
However, there was no available data for ER, UR, 
or HI at Ottawa. 

Alternatively, considering that Ottawa is a developed 
city in Ontario with more than 1 million population, 
it is reasonable to use Census metropolitan area and 
census agglomeration at Ontario as the representative 
of Ottawa. It should be mentioned that only the monthly 
data provided (Canada Open Data, n.d.). In the database, 
ER is the number of persons employed expressed as a 
percentage of the population 15 years of age and over. 
ER for a particular group (age, sex, marital status, etc.) 
is the number employed in that group expressed as a 
percentage of the population for that group. Estimates 
are percentages, rounded to the nearest tenth. UR is the 
number of unemployed persons expressed as a percentage of 
the labour force. UR for a particular group (age, sex, 
marital status, etc.) is the number unemployed in that 
group expressed as a percentage of the labour force for 
that group. Estimates are percentages, rounded to the 
nearest tenth. 


*****************************************************
Document illustration
*****************************************************
01.Data_Process.py
the python script for the calculation.


Dataset.xlsx
the cleaned data which will be used as the input
in the 01.Data_Process.py


the other png and csv files are the outputs

*****************************************************
References
*****************************************************
Canada Open Data. (n.d.). https://open.ottawa.ca/
Open Ottawa. (n.d.). https://open.ottawa.ca/search?q=covid-19


*****************************************************
Contact
*****************************************************
there is is anything unclear, please feel free to contact
me.


