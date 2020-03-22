import pandas as pd
import matplotlib.pyplot as plt

class Student:
    
    def __init__(self):
        
        self.data_base = pd.read_csv("student_data.csv") #Reads file from Student_data.csv
        self.temp_data = []   #Temporaray data of the session.
    def add_student(self): #To add new student to the existing database.
        
        while True:
            temp_name = input("Enter name of the student: ")  #Inputs name of student from the User.
            if temp_name.isalpha() :
                break
            else:
                print("Please Enter String Data")
                
            
        while True:
            
            nsub = 3 #Number of Subjects
            marks_list = []
            for i in range(nsub):
                print("Enter marks for subject {}".format(i+1))
                try:        #Subject Integer Input for the Student
                    subject_marks = int(input())
                    marks_list.append(subject_marks)
                except ValueError: #If not integer, then code runs into this error message.
                    print("\nSubjects can only be integers")
                    print('Enter Again')
                    break
                
            if i==2:
                print("Marks for student {} is {}".format(temp_name,marks_list))
                break
        self.temp_data = []   
        self.temp_data.append(temp_name)
        for item in marks_list:
            self.temp_data.append(item)
        temp_data_df = pd.DataFrame([self.temp_data],
                                    columns= ["Name","Marks1","Marks2","Marks3"]) #Coverting List data into panda dataframe.
        self.data_base = pd.concat([self.data_base,temp_data_df],ignore_index= True)#Adding temporary data to main database
       # print(self.data_base)
        #print(self.temp_data)
        
        
    def Average_marks(self): #To calculate average marks obtained by the student.
        
        while True:
            name_to_find = input("Enter the name to find: ")
            if type(name_to_find) != str:
                print("Please Enter only sting values")
            else:
                break
        if name_to_find in self.data_base.values:
            average = self.data_base[self.data_base["Name"] == name_to_find].mean(axis = 1)#Logic to calculate average marks. Axis 1 denotes the row
            print("Average Marks for {} is {}".format(name_to_find,average))
        else:
            print("The student {} is not in Database".format(name_to_find))
            
            
    def search_student(self): #To search a student in the database
        while True:
            name_to_find = input("Enter the name to find: ")
            if type(name_to_find) != str:
                print("Please Enter only sting values")
            else:
                break
        if name_to_find in self.data_base.values: #If the name exists in the database then it returns true
            print("{} is Present".format(name_to_find))
        else:
            print("The student {} is not in Database".format(name_to_find))
            
        
        
            
    def show_summary(self):#Lists the number os students with their marks.
        print(self.data_base.to_string(index = False))
    
    def save_toCSV(self): #To save the current data to the csv file.
        self.data_base.to_csv('student_data.csv',index=False)
        print("Data Saved to the current Directory")
        
    def Plot_Bar_Chart(self):
        Temp_chart_data = self.data_base.set_index("Name") #Copying the database to anew variable and setting the index as Name(by deafult the index was 0,1...)
        Temp_chart_data.plot.bar()
        plt.show() #Forcing pandas to show the plot
        
            
def main(): #Its like a menu for the user.
    
    st1 = Student()
    
    while(True):
        try:
            print("""
           
              --- Welcome to Student Management System ----
           
              Please select one of the following option 
              
              1.Add New Student
              2.Search Student
              3.Average Marks of the Student
              4.Show Summary
              5.Save Student Data
              6.Plot Bar Chart
              7.Exit Program""")
            option = int(input("Enter your choice :"))
            
            if option==1:
                st1.add_student()
            elif option ==2:
                st1.search_student()
            elif option ==3:
                st1.Average_marks()
            elif option ==4:
                st1.show_summary()
            elif option == 5:
                st1.save_toCSV()
            elif option ==6:
                st1.Plot_Bar_Chart()
            elif option == 7:
                print("\n Good Day !!")
                break
            else:
                print("Please select one of the options")
            
                
            
        
            
        except ValueError:
                print("""Invalid Input: Please enter a number""")
                
                
                
        
        
main()
