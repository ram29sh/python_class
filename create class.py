class student:
    stucount=0
    def __init__(self,name,score):
        self.name= name
        self.score= score
        student.stucount+=1
        
    def displaycount(self):
        print("total student %d" % student.stucount)

    def displaystudent(self):
        print("name:",self.name, "score:", self.score)
        


stu1=student("ramesh",100)
stu2=student("koritikanti",200)
stu1.displaystudent()
stu2.displaystudent()
print(" total count %d" % student.stucount)
