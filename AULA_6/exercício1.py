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
    
class ContaBancária:
    def __init__(self):
        self.__nome = ""
        self.__número = 0
        self.saldo = 0
        self.__depósito = 0
        self.__saque = 0
    def set__nome(self, nome):
        if len(nome) > 3: self.__nome = nome
        else: raise ValueError()
    def set__número(self, v):
        if v >= 0: self.__número = v
        else: raise ValueError()
    def set__saldo(self, v):
        if v >= 0: self.__saldo = v
        else: raise ValueError()
    def get_nome(self):
        return self.__nome
    def get_número(self):
        return self.__número