class Triangulo:
    def __init__(self):
        self.b = 0 # atributos
        self.h = 0
    def calc_area(self): # método
        return self.b * self.h / 2

x = Triangulo()
print(x.b, x.h)
x.b = float(input("Informe a base do segundo triângulo\n"))
x.h = float(input("Informe a altura do triângulo\n"))         
print(x.b, x.h)
a = x.calc_area()
print(f"A a´rea do triângulo é {a:.2f}")