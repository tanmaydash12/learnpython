class Employee:
    no_of_leaves= 8

    def __init__(self,aname, asalary, arole) :
        self.name = aname
        self.salary  = asalary
        self.role = arole
        
    def printdetails(self):
        returm(f"The name is ")