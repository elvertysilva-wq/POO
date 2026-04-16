class Agua:
    def __init__(self):
        self.mes = 0
        self.ano = 0 
        self.consumo = 0

    def calc_consumo(self):
        if self.consumo <= 10:
            return 38.0 
        
        elif 11 <= self.consumo <= 20:
            além_do_10 = self.consumo - 10
            return 5.0 * além_do_10 + 38
        
        else: 
            self.consumo >=20
            além_de_20 = self.consumo - 20
            return 6.0 * além_de_20 + 38 + 50

conta = Agua()            
conta.mes = input("digite o mes: ")
conta.ano = input("dgite o ano: ")
conta.consumo = float(input("digite o consumo em m3: "))
valor = conta.calc_consumo()

print(f"Conta de água: {conta.mes}/{conta.ano}")
print(f"Consumo: {conta.consumo} m³")
print(f"Valor a pagar: R$ {valor:.2f}")


        
    
        
            

