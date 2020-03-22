import pandas as pd

class Student:
    
    def __init__(self):
        
        self.data_base = pd.read_csv("student_data.csv")
        self.temp_data = []
    def add_student(self):
        
        while True:
            temp_name = input("Enter name of the student: ")
            if temp_name.isalpha() :
                break
            else:
                self.Error()
                
            
        while True:
            #nsub = int(input("Number of subjects: "))
            nsub = 3 #Number of Subjects
            marks_list = []
            for i in range(nsub):
                print("Enter marks for subject {}".format(i+1))
                try:
                    subject_marks = int(input())
                    marks_list.append(subject_marks)
                except ValueError:
                    print("\nSubjects can only be integers")
                    print('Enter Again')
                    break
                
            if i==2:
                print("Marks for student {} is {}".format(temp_name,marks_list))
                break
            
        self.temp_data.append(temp_name)
        for item in marks_list:
            self.temp_data.append(item)
        temp_data_df = pd.DataFrame([self.temp_data],
                                    columns= ["Name","Marks1","Marks2","Marks3"])
        self.data_base = pd.concat([self.data_base,temp_data_df],ignore_index= True)
        print(self.data_base)
        #print(self.temp_data)
        
        
    def Average_marks(self):
        
        while True:
            name_to_find = input("Enter the name to find: ")
            if type(name_to_find) != str:
                print("Please Enter only sting values")
            else:
                break
        if name_to_find in self.data_base.values:
            average = self.data_base[self.data_base["Name"] == name_to_find].mean(axis = 1).values
            print("Average Marks for {} is {}".format(name_to_find,average))
        else:
            print("The student {} is not in Database".format(name_to_find))
            
            
    def search_student(self):
        while True:
            name_to_find = input("Enter the name to find: ")
            if type(name_to_find) != str:
                print("Please Enter only sting values")
            else:
                break
        if name_to_find in self.data_base.values:
            print("{} is Present".format(name_to_find))
        else:
            print("The student {} is not in Database".format(name_to_find))
            
        
        
            
    def show_summary(self):
        print(self.data_base.to_string(index = False))
    
    def save_toCSV(self):
        self.data_base.to_csv('student_data.csv',index=False)
        print("Data Saved to the current Directory")
            
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
              5.Save Student Data
              6.Exit Program""")
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
            elif option == 6:
                break
            else:
                print("Please select one of the options")
            
                
            
        
            
        except ValueError:
                print("""Invalid Input: Please enter a number""")
                
                
                
        
        
main()
