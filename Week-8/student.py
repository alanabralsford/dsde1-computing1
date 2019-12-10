class DesEngStudent:
    def __init__(self, name, year, budget):
       self.name = name
       self.year = year
       self.budget = budget
    
    def print(self):
        #LINE BELOW IS ABSOLUTE BULLSHIT
        #my_student = (self.name + " (DE" + str(self.year) + ") with £" + self.budget + "remaining") 
        #LINE BELOW IS THE BOLLOCKS THANK YOU VICTOR     https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html
        my_student = ("%s (DE%d) with £%g remaining" % (self.name, self.year, self.budget))
        #print(my_student)
        return my_student
#% converts variable to whatever you label it as
#yes please 
    def spend(self, splash):
        if splash > self.budget:
            #print("call daddy")
            raise ValueError
        else:
            daddys_bank = self.budget - splash
            self.budget = daddys_bank
            return daddys_bank
    
    def three_d(self, amount):
        final = self.spend(5.50*amount)
        return final

    def paper_print(self, amount):
        final = self.spend(0.10*amount)
        return final
    
    def laser_cut(self, amount):
        final = self.spend(1.00*amount)
        return final


#s1 = DesEngStudent("Peter", 3, 100)
""" s1.print()
#print(s1.spend(30))
print(s1.three_d(5))
print(s1.paper_print(3))
print(s1.laser_cut(6)) """




