import resistor as r
def parallel_pair():
    my_resistor1 = r.Resistor('red', 'red', 'brown', 'gold')
    my_resistor2 = r.Resistor('yellow', 'orange', 'black', 'silver')
    R_Total_Inverse = (1/my_resistor1.value()) + (1/my_resistor2.value())
    R_Total = 1/R_Total_Inverse
    return R_Total

print(parallel_pair())