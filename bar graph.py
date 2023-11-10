#importing numpy to call functions 
import numpy as np
#To plot graphs we here importing matplotlib 
import matplotlib.pyplot as plt
#To analyze data we import pandas
import pandas as pd
#defing a function for a bar chart

def second_plot(ages,heading, on_x_axis, on_y_axis):
#values:
 #ages = age of each student in the data
 #heading = Title of the bar graph
 #on_x_axis,on_y_axis = lables on each axis
 
 fig = plt.figure(figsize = (20, 7))
 #counts the total number of students of each age group
 counts = student_data[ages].value_counts().sort_index()
 #taking values from count and use in the bar graph
 plt.bar(counts.index, counts.values, color = ['red', 'blue', 'green', 'yellow'])
 #label on x-axis
 plt.xlabel(on_x_axis)
 #label on y-axis
 plt.ylabel(on_y_axis)
 #title of the bar graph
 plt.title(heading)
 plt.show()
#location of the file which consists of student data
student_data = pd.read_csv('Student_Mental_health.csv')

#Calling function for the bar graph
second_plot('Age', 'Ages of students', 'Number of students', 'Number of students in each age group')