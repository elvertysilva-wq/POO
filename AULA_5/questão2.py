class País:
    def __init__(self):
        self.nome = ""
        self.população = 0
        self.área = 0

    def calc_densidade(self):
        x = self.população / self.área
        return x
    
maior_densidade = 0
país_maior = 0

for i in range(10):
    print(f"país {i+1}:")

    p = País()
    p.nome = input("nome: ")
    p.população = int(input("população: "))
    p.área = int(input("área: "))

    x = p.calc_densidade()
    if x > maior_densidade:
        maior_densidade = x
        país_maior = p.nome
        print(país_maior)


    
