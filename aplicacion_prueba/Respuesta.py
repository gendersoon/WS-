from bs4 import BeautifulSoup
import requests
class Respuesta(object):
    """description of class"""
      
    #~ campos
    __respuesta = ''
    __usuario = ''
    __fecha = ''
    
    def __init__(self,usuario,respuesta,fecha):
        self.__usuario = usuario
        self.__respuesta = respuesta
        self.__fecha = fecha

    def get_usuario(self):
        return self.__usuario
    
    def get_respuesta(self):
        return self.__respuesta
    
    def get_fecha(self):
        return self.__fecha    



