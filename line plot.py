#importing numpy to call functions 
import numpy as np
#To plot graphs we here importing matplotlib 
import matplotlib.pyplot as plt
#To analyze data we import pandas
import pandas as pd
#Define the function 'first' to plot a line graph between the given vales
def first_graph(Yar, pop, full, TOP1, TOP2, TOP3):
    
#values in function:
#Yar=year.
#pop = Total Population in us from 1960 to 2010 .
#full = Total crimes happen.
#TOP1 = Highest number of crime("property").
#TOP2 = Second top crime("Violent").
#TOP3 = third top crime("Larceny_Theft").

#CSV file location which consists of data
  illega_act= pd.read_csv('US_Crime_Rates_1960_2014.csv')
  

   
  #line graph between year and Population
  plt.plot(illega_act[Yar], illega_act[pop], label = pop, color = 'r', linewidth = 1, marker = '.')
  #line graph between year and Total crimes
  plt.plot(illega_act[Yar], illega_act[full], label = full, color = 'b', linewidth = 1, marker = '.')
  #line graph between year and Highest number of crime("property").
  plt.plot(illega_act[Yar], illega_act[TOP1], label = TOP1, color = 'y', linewidth = 1, marker = '.')
  #line graph between year and Second top crime("Violent").
  plt.plot(illega_act[Yar], illega_act[TOP2], label = TOP2, color = 'g', linewidth = 1, marker = '.')
  #line graph between year and Third top crime("Larceny_Theft").
  plt.plot(illega_act[Yar], illega_act[TOP3], label = TOP3, color = 'black', linewidth = 1, marker = '.')
  #In x-axis we take the time period from 1960-2010
  
  plt.xlabel('Year')
  #In y-axis we have the frequency of the count of people
  plt.ylabel('frequency of number of population')
  #Title of the line graph
  plt.title('Total population and top Three crime activities in US between 1960-2010')
  
  plt.legend()
  plt.grid(True)
  plt.show()

#calling function to plot a line graph
first_graph('Year', 'Population', 'Total', 'Property', 'Violent', 'Larceny_Theft')
  





