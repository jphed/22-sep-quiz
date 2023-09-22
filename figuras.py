from abc import ABC, abstractmethod
import math

class Figura(ABC):
    def __init__(self, color="Amarillo"):
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not isinstance(color, (str)):
            raise TypeError("color debe ser texto")
        self.__color = color
    
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getVolumen(self):
        pass

    def __str__(self):
        return f"Figura [{self.color}]"

class Circulo(Figura):
    def __init__(self, color = "Verde", radio = 5):
        self.radio = radio
        super().__init__(color)
                
    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, radio):
        if not isinstance(radio, (float, int)):
            raise TypeError("radio debe ser un número")
        if radio<=0:
            raise ValueError("radio debe ser mayor a cero")
        self.__radio = radio

    def getArea(self):
        a = (math.pi)
        b = (self.radio**2)
        result = a*b
        return result
    
    def getVolumen(self):
        return 0

    def __str__(self):
        return super().__str__() + f"Circulo Area = {math.pi * self.radio**2}"
    
class CilindroCircular(Circulo):
    def __init__(self, color="Verde", radio=5, altura=2):
        self.altura = altura
        super().__init__(color, radio)

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, (float, int)):
            raise TypeError("altura debe ser un número")
        if altura<=0:
            raise ValueError("altura debe ser mayor a cero")
        self.__altura = altura

    def getArea(self):
        a = (2*math.pi)
        b = (self.altura+self.radio)
        result = round(a*b,2)
        return result
    
    def getVolumen(self):
        a = (2*3.14)
        b = (self.altura+self.radio)
        area = a*b
        result = area * self.altura
        return result

    def __str__(self):
        return f"Color: {self.color} -- Area: {self.getArea()} -- Volumen: {self.getVolumen()}"

#main

cc = CilindroCircular(radio = 20, color="rojo", altura=5)
print(cc)


