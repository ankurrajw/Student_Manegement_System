# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:22:28 2020

@author: Suraj Pandey
"""

class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        self.data_base = {self.name:self.marks}
        
    def add_student(self):
        temp_name = input("Enter name of the student: ")
        nsub = int(input("Number of subjects: "))
        
        marks_list = []
        for i in range(nsub):
            temp_marks = int(input ("Enter sub " + str(i+1) +" :" ))
            marks_list.append(temp_marks)
            
            
        self.data_base.update({temp_name:marks_list})
        print(self.data_base[temp_name])
        
    def Average_marks(self,name_to_find):
        if name_to_find in self.data_base:
            marks_to_find = self.data_base[name_to_find]
            return sum(marks_to_find)/len(marks_to_find)
        else:
            print( name_to_find +" not in the databae")
            
    def search_student(self,name_to_find):
        if name_to_find in self.data_base:
            print(name_to_find + " Exist")
            print(self.data_base[name_to_find])
        else:
            print( name_to_find +" not in the databae")
        

st1 = Student("Elia", [34 , 12, 45, 78, 99 ])  

st1.add_student()
st1.add_student()


st1.search_student(input("Enter Name to be searched: "))


     
            
            
        
        
        
        
        