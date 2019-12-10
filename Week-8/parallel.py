import resistor as r
def parallel_pair():
    my_resistor1 = r.Resistor('red', 'red', 'brown', 'gold')
    my_resistor2 = r.Resistor('yellow', 'orange', 'black', 'silver')
    R_Total_Inverse = (1/my_resistor1.value()) + (1/my_resistor2.value())
    R_Total = 1/R_Total_Inverse
    return R_Total

def parallel_resistance(*resistances):
    total_rec = 0
    for resistance in resistances:
        total_rec = total_rec + (1 / resistance.value())
    total = 1 / total_rec
    return total

print(parallel_resistance(r.Resistor('red', 'red', 'brown', 'gold'),r.Resistor('yellow', 'orange', 'black', 'silver')))

print(parallel_pair())