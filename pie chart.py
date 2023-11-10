#importing numpy to call functions 
import numpy as np
#To plot graphs we here importing matplotlib 
import matplotlib.pyplot as plt
#To analyze data we import pandas
import pandas as pd
#Defining a function for pie_chart
def third_plot(course_name, Heading):
 
 #Locating data sheet file for the data
 student_data = pd.read_csv('Student_Mental_health.csv')
 #Taking first 20 values from the data
 course=student_data.head(20)
 fig = plt.figure(figsize = (20, 15))
 #Counting the number of students in each course for the pie chat
 plt.pie(course[course_name].value_counts().values, 
labels=course[course_name].value_counts().index, autopct='%3.1f%%')
 #To display title of chart
 plt.title(Heading)
 plt.show()
#calling pie chart function
third_plot('What is your course?', 'Number of Students enrolled in different courses')