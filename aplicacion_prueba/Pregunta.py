from bs4 import BeautifulSoup
import requests
import time
from Usuario import Usuario
from Respuesta import Respuesta
class Pregunta():
    #~ campos

    __lista_usuarios = []
    __lista_respuestas = []
    __pregunta = ''
    __usuario = ''
    __url = ''


    #~ constructor
    def __init__ (self,url):
        self.__soup = BeautifulSoup(requests.get(url).text,'html5lib')
        self.__url = url


    #~ Métodos

    '''Método crea respuestas: toma la url y extrae todas las respuestas
    en orden por cada usuario'''
    def crea_respuestas(self):
        descRespuesta = self.__soup.find_all(attrs = {'class' :'post-text'})
        usuario_responde = self.__soup.find_all(attrs = {'class':'user-details'})
        usuario_action_time = self.__soup.find_all(attrs = {'class':'user-action-time'})
        itera = 0
        j=1
        for i in usuario_action_time:
            try:
                if i.text.find('answered')!=-1:
                    respuesta = Respuesta(usuario_responde[itera].a.text, descRespuesta[j].text, i.contents[1].text)
                    self.__lista_respuestas.append(respuesta)
                    j+=1
            except Exception as inst:
                print(inst)
            itera+=1

    '''Método para crear la lista de los usuarios, el primer índice es el que
    pregunta'''
    def crea_lista_usuarios(self):
        usuario = Usuario(self.get_usuario_que_pregunta_link(),self.get_usuario_que_pregunta_name())
        self.__lista_usuarios.append(usuario)
        itera = 0
        user = self.__soup.find_all(attrs = {'class' :'user-action-time'})
        usuario_responde = self.__soup.find_all(attrs = {'class': 'user-details'})
        for i in user:
            if i.text.find("answered")!=-1:
               link = "https://stackoverflow.com" + usuario_responde[itera].a['href']
               nombre = usuario_responde[itera].a.text
               usuario = Usuario(link,nombre)
               self.__lista_usuarios.append(usuario)
            itera+=1

    def imprimeUsuarios(self):
        for i in self.__lista_usuarios:
            print (i.get_username())

    def imprime_bio(self):
        for i in self.__lista_usuarios:
            print(i.get_bio())

    def imprime_comunidades(self):
        for i in self.__lista_usuarios:
            print(i.get_comunidades())

    def imprime_respuestas(self):
        for i in self.__lista_respuestas:
            print(i.get_usuario())
            print(i.get_respuesta())
            print(i.get_fecha())

    def get_pregunta(self):
        pregunta = self.__soup.find(attrs = {'class':'question-hyperlink'})
        return pregunta.text

    def get_usuario_que_pregunta_name(self):
        itera = 0
        user = self.__soup.find_all(attrs = {'class' :'user-action-time'})
        p = self.__soup.find_all(attrs = {'class': 'user-details'})
        for i in user:
            if i.text.find("asked")!=-1:
                self.__usuario = p[itera].a.text
            itera+=1
        return self.__usuario

    def get_usuario_que_pregunta_link(self):
        itera = 0
        user = self.__soup.find_all(attrs = {'class' :'user-action-time'})
        p = self.__soup.find_all(attrs = {'class': 'user-details'})
        for i in user:
            if i.text.find("asked")!=-1:
               link = "https://stackoverflow.com" + p[itera].a['href']
            itera+=1
        return link

    def get_descripcion_pregunta(self):
        descPregunta = self.__soup.find_all(attrs = {'class' :'post-text'})
        return descPregunta[0].text

    def get_lista_usuarios(self):
        print(len(self.__lista_usuarios))
        return self.__lista_usuarios

    def get_lista_respuestas(self):
        return self.__lista_respuestas
