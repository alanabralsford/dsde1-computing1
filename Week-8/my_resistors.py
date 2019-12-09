import resistor as r
Resistor1 = r.Resistor('brown', 'black', 'red', 'silver')
Resistor2 = r.Resistor('red', 'red', 'red', 'brown', 'gold')

print(Resistor1.value())
print(Resistor1.min_value())
print(Resistor1.max_value())
print(Resistor2.min_value())
print(Resistor2.max_value())
