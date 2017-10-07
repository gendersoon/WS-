from bs4 import BeautifulSoup

import requests

from urlextract import URLExtract

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

BD = declarative_base()

class User(BD):
    __tablename__ = "User"

    userName = Column('userName', String, primary_key=True)
    descUser = Column('descUser', String)
    Communities = Column('Communities', String)
    Activities = Column('Activities', String)

class Respuesta(BD):
    __tablename__ = "Respuesta"

    idRespu = Column('idRespu', Integer, primary_key=True)
    Respuesta = Column('Respuesta', String)
    descRespu = Column('descRespu', String)
    userNameRespuesta = Column('userNameRespuesta', String, ForeignKey("User.userName"), nullable=False)

class Pregunta(BD):
    __tablename__ = "Pregunta"

    idPregun = Column('idPregun', Integer, primary_key=True)
    Pregunta = Column('Pregunta', String)
    descPregun = Column('descPregun', String)
    userNamePregunta = Column('userNamePregunta', String, ForeignKey("User.userName"), nullable=False)

engine = create_engine('sqlite:///ComunidadStack.db', echo=True)

BD.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

def NoSeComoLlamarAEsteMetodo():
    url = 'https://stackoverflow.com/questions/89228/calling-an-external-command-in-python?rq=1

    re = requests.get(url)

    soup = BeautifulSoup(re.text,'htlm5lib.parser')

    while True:
        input_string = "¿Qué desea hacer?\n\t1. Obtener atributos generales."
        input_string += "\n\t2. Obtener Respuestas."
        input_string += "\n\t3. Obtener Preguntas."
        input_string += "\n\t4. Salir.\n"
        opt = input(input_string)
        if opt != '4':
            if opt == '1':
                get_user_attributes(soup)
                print(">>Usuarios han sido guardados en base de datos.")
            elif opt == '2':
                get_user_Respuesta(soup)
                print(">>La Respuesta ha sido guardada en base de datos.")
            elif opt == '3':
                get_user_Pregunta(soup)
                print(">>Las Preguntas han sido guardados en base de datos.")
            else:
                break
def get_user_attributes(soup):
    session = Session()
    user = User()

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

def get_user_Respuesta(soup):
    extractor = URLExtract()
    session = Session()

def get__user__Pregunta(soup):
    extractor = URLExtract()
    session = Session()
