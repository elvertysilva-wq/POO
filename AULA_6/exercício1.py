import math
class Círculo:
    def __init__(self):
        self.__r = 0
    def set_raio(self, v):
        if v >= 0: self.__r = v
        else: raise ValueError()
    def get_raio(self):
        return self.__r
    def calc_circunferência(self):
        return 2 * math.pi * self.__r
    
class Viagem:
    def __init__(self):
        self.__d = 0
        self.__t = 0
    def set__distância(self, v):
        if v >=0: self.__d = v
        else: raise ValueError()
    def set__tempo(self, v):
        if v >= 0: self.__t = v
    def get_distância(self):
        return self.__d
    def get_tempo(self):
        return self.__t
    def calc_velocidade_média(self):
        return self.__d / self.__t
    

class Conta:
    def __init__(self):
            self.__nome = ''
            self.__numero = ''
            self.__saldo = 0.00  
            self.__deposito = 0.00
            self.__saque = 0.00

        
    def set_nome(self, v):
            if len(v) >= 4:
                self.__nome = v
            else:
                raise ValueError()

    def set_numero(self, v):
            if len(v) >= 5:
                self.__numero = v
            else:
                raise ValueError()

    def set_deposito(self, v):
            if v > 0:
                self.__deposito = v
            else:
                raise ValueError()

    def set_saque(self, v):
            if v > 0:
                self.__saque = v
            else:
                raise ValueError()

        
    def get_nome(self):
            return self.__nome

    def get_numero(self):
            return self.__numero

    def get_deposito(self):
            return self.__deposito

    def get_saque(self):
            return self.__saque

    def get_saldo(self):
            return self.__saldo

    
    def set_deposito(self, v):
            self.__saldo += v

    def set_saque(self, v):
            self.__saldo -= v

class EntradaCinema:
    def __init__(self):
        self.__dia = ''
        self.__horario = 0  

    
    def set_dia(self, dia):
        dias_validos = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
        if dia.lower() in dias_validos:
            self.__dia = dia.lower()
        else:
            raise ValueError('Dia inválido')

    def set_horario(self, horario):
        if 0 <= horario <= 23:
            self.__horario = horario
        else:
            raise ValueError('Horário inválido')

    
    def get_dia(self):
        return self.__dia

    def get_horario(self):
        return self.__horario

    
    def __valor_base(self):
        if self.__dia in ['segunda', 'terca', 'quinta']:
            return 16.0
        elif self.__dia == 'quarta':
            return 8.0
        elif self.__dia in ['sexta', 'sabado', 'domingo']:
            return 20.0

    def __aplicar_acrescimo(self, valor):
        if 17 <= self.__horario <= 23:
            return valor * 1.5
        return valor

    def calcular_inteira(self):
        if self.__dia == 'quarta':
            return 8.0  # já é meia pra todo mundo
        valor = self.__valor_base()
        return self.__aplicar_acrescimo(valor)

    def calcular_meia(self):
        if self.__dia == 'quarta':
            return 8.0
        valor = self.__valor_base() / 2
        return self.__aplicar_acrescimo(valor)

def main():
    ingresso = EntradaCinema()

    try:
        dia = input('Dia da sessão: ')
        horario = int(input('Horário (0-23): '))

        ingresso.set_dia(dia)
        ingresso.set_horario(horario)

        print('\n--- RESULTADO ---')
        print(f'Dia: {ingresso.get_dia()}')
        print(f'Horário: {ingresso.get_horario()}h')
        print(f'Inteira: R$ {ingresso.calcular_inteira():.2f}')
        print(f'Meia: R$ {ingresso.calcular_meia():.2f}')

    except ValueError as e:
        print('Erro:', e)


if __name__ == '__main__':
    main()



class UI:

    @staticmethod
    def circulo():
        import math

        print('-' * 40)
        print('CÁLCULO DO CÍRCULO')
        print('-' * 40)

        x = Círculo()

        try:
            x.set_raio(float(input('Informe o raio: ')))

            print('\n' * 2)
            print('*RESULTADOS*')
            print(f'Raio: {x.get_raio()}')
            print(f'Circunferência: {x.calc_circunferência():.2f}')

        except ValueError:
            print('Erro: valor inválido')


    @staticmethod
    def viagem():
        print('-' * 45)
        print('DADOS DA VIAGEM')
        print('-' * 45)

        x = Viagem()

        try:
            x.set__distância(float(input('Distância (km): ')))
            x.set__tempo(float(input('Tempo (horas): ')))

            print('\n' * 2)
            print('*RESULTADOS*')
            print(f'Distância: {x.get_distância()} km')
            print(f'Tempo: {x.get_tempo()} h')

            if x.get_tempo() > 0:
                print(f'Velocidade média: {x.calc_velocidade_média():.2f} km/h')
            else:
                print('Erro: tempo não pode ser zero')

        except ValueError:
            print('Erro: valor inválido')


    @staticmethod
    def conta():
        print('-' * 40)
        print('CONTA BANCÁRIA')
        print('-' * 40)

        x = Conta()

        try:
            x.set_nome(input('Nome: '))
            x.set_numero(input('Número da conta: '))

            print('\n*Conta criada com sucesso!*')

            acao = -1
            while acao != 0:
                print('''
[1] Depositar
[2] Sacar
[3] Ver saldo
[0] Sair
''')
                acao = int(input('Escolha: '))

                if acao == 1:
                    valor = float(input('Valor: R$ '))
                    x.set_deposito(valor)

                elif acao == 2:
                    valor = float(input('Valor: R$ '))
                    x.set_saque(valor)

                elif acao == 3:
                    print(f'Saldo: R$ {x.get_saldo():.2f}')

        except ValueError:
            print('Erro: valor inválido')


    @staticmethod
    def cinema():
        print('-' * 45)
        print('INGRESSO DE CINEMA')
        print('-' * 45)

        x = EntradaCinema()

        try:
            x.set_dia(input('Dia da sessão: '))
            x.set_horario(int(input('Horário (0-23): ')))

            print('\n' * 2)
            print('*RESULTADOS*')
            print(f'Dia: {x.get_dia()}')
            print(f'Horário: {x.get_horario()}h')
            print(f'Inteira: R$ {x.calcular_inteira():.2f}')
            print(f'Meia: R$ {x.calcular_meia():.2f}')

        except ValueError as e:
            print('Erro:', e)
    
    