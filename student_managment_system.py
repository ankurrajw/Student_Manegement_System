# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:22:28 2020

@author: Suraj Pandey
"""

class Student:
    
    def __init__(self):
        
        self.data_base = {}
        
    def add_student(self):
        
        while True:
            try:
                temp_name = str(input("Enter name of the student: "))
                break
            except:
                self.Error()
            
        
        while True:
            nsub = int(input("Number of subjects: "))
            if nsub != int or 0<=nsub<=10:
                self.Error()
            else:
                break
            
        
        
        marks_list = []
        for i in range(nsub):
            while True:
                temp_marks = int(input ("Enter sub " + str(i+1) +" :" ))
                if temp_marks != int:
                    self.Error()
                else:
                    break
            
            
            marks_list.append(temp_marks)
            
            
        self.data_base.update({temp_name:marks_list})
        print(self.data_base[temp_name])
        
    def Average_marks(self):
        
        while True:
            name_to_find = input("Enter the name to find: ")
            if name_to_find != str:
                self.Error()
            else:
                    break
        
        if name_to_find in self.data_base:
            marks_to_find = self.data_base[name_to_find]
            print( sum(marks_to_find)/len(marks_to_find))
        else:
            print( name_to_find +" not in the databae")
            
    def search_student(self):
        
        while True:
                name_to_find = input("Enter the name to find: ")
                if name_to_find != str:
                    self.Error()
                else:
                    break
        if name_to_find in self.data_base:
            print(name_to_find + " Exist")
            print(self.data_base[name_to_find])
        else:
            print( name_to_find +" not in the databae")
    def show_summary(self):
        for name in self.data_base:
            print(name, self.data_base[name])
            
    def Error(self):
        print("Invalid Input")
            
def main():
    
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
              5.Exit Program""")
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
            
                
            
                break
            
                
            
        
            
        except ValueError:
                print("""Invalid Input: Please enter a number""")
                
                
                
        
        
main()

     
            
            
        
        
        
        
        
