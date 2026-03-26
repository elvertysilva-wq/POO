print("Digite um número inteiro")
n = int(input)
primo = True                        
for d in range(2, n):
    if n % d == 0: primo = False    
if primo : print(n, "é primo")      # if primo:
else: print(n, "não é primo")

def Primo(n):
    primo = True
    for d in range(2, n):
        if n % d == 0: primo = False
        if primo == False: break
    return primo
 # continua