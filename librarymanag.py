class Student:
    def __init__(self,firstname,lastname,rollno):
        self.a=firstname
        self.b=lastname
        self.c=rollno
        
class Library(Student):
       def book(self,bookname):
           self.bookn=bookname
       def purpose(self,p):
           self.pur=purpose    
       def issuedate(self,d):
           self.dateofissue=d 
       def returndate(self,r):
           self.dateofreturn=r      
       def display(self):
           print(f"Student firstname:{self.a}   Student lastname:{self.b}      Student rollno:{self.c}        Bookname:{self.bookn}     Purpose:{self.pur}      Date of issuing:{self.dateofissue}      Date of returning:{self.dateofreturn}")
frstname=input("Enter student firstname: ")    
lastname=input("Enter student lastname: ")    
rolln=int(input("Enter student rollno. : ")) 
bookname=input("Enter bookname: ")     
i=0
purpose=input("Do you wanna issue/return the book?") 
while((purpose!="issue") or (purpose!="return")):  
    if(purpose=="issue"):
      dateissue=(input("Enter date of issued: "))
      datereturn=(input("Enter date of return: "))
      break
    elif(purpose=="return"):
      dateissue=(input("Enter date of issued: ")) 
      datereturn=(input("Enter date of return: "))
      break
    else:
       print("Enter correct input!")
       purpose=input("Do you wanna issue/return the book?") 
i+=1    
     
obj=Library(frstname,lastname,rolln) 
obj.book(bookname)   
obj.purpose(purpose)
obj.issuedate(dateissue)
obj.returndate(datereturn)
obj.display()       
                
