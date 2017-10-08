from bs4 import BeautifulSoup
import requests


class ScrapFactory(object):

    __soup = ''

    def __init__(self,url):
        self.__soup = BeautifulSoup(requests.get(url).text,'html5lib')

    def class_finder(self,comando,val):        
        if comando == 'findall':
            return self.__soup.find_all(attrs = {'class' : val})
        elif comando == 'find':
            return self.__soup.find(attrs = {'class' : val})

    def busca(self,texto,attr):
        if attr.text.find(texto) == 0:
            return true

        '''
        Clase pregunta
        '''
class Pregunta():
    #~ campos
    
    __lista_usuarios = []
    __lista_respuestas = []
    __pregunta = ''
    __usuario = ''
    __url = ''
    
    
    #~ constructor
    def __init__ (self,url):
        self.__url = url
        self.scrap = ScrapFactory(url)
    
    
    #~ Métodos
    '''Método crea respuestas: toma la url y extrae todas las respuestas 
    en orden por cada usuario'''
    
    def crea_respuestas(self):
        descRespuesta = self.scrap.class_finder('findall','post-text')
        usuario_responde = self.scrap.class_finder('findall','post-text')
        usuario_action_time = self.scrap.class_finder('findall','post-text')
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
        user = self.scrap.class_finder('findall','user-action-time')
        usuario_responde = self.scrap.class_finder('findall','user-details')
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
        pregunta = self.scrap.class_finder('find','question-hyperlink')
        return pregunta.text    
    
    def get_usuario_que_pregunta_name(self):        
        itera = 0
        user = self.scrap.class_finder('findall','user-action-time')
        p = self.scrap.class_finder('findall','user-details')
        for i in user:
            if i.text.find("asked")!=-1:
                self.__usuario = p[itera].a.text
            itera+=1                                
        return self.__usuario
    
    def get_usuario_que_pregunta_link(self):        
        itera = 0
        user = self.scrap.class_finder('findall','user-action-time')
        p = self.scrap.class_finder('findall','user-details')
        for i in user:
            if i.text.find("asked")!=-1:
               link = "https://stackoverflow.com" + p[itera].a['href']
            itera+=1                                
        return link
    
    def get_descripcion_pregunta(self):
        descPregunta = self.scrap.class_finder('findall','post-text')
        return descPregunta[0].text
    
    def get_lista_usuarios(self):
        print(len(self.__lista_usuarios))
        return self.__lista_usuarios
        
    def get_lista_respuestas(self):
        return self.__lista_respuestas

    '''
    Clase respuesta
    '''
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

    '''
    Clase Usuario
    '''

class Usuario:
    
    #~ campos
    
    __username = ''
    __bio = ''
    __soup = ''
    __url = ''
    __lista_comunidades = []
    
    #~ constructor
    def __init__(self,url,username):
        self.__username = username
        self.scrap = ScrapFactory(url)


    #~ Métodos
    def get_username(self):
        return self.__username
    
    def get_bio(self):
        p = self.scrap.class_finder('find','about')
        self.__bio = p.contents[5].text        
        return self.__bio
    
    def get_comunidades(self):
        r = requests.get(self.__url)
        texto = r.text
        scrap_tmp = ScrapFactory(self.__url)
        view_more = scrap_tmp.class_finder('find','view-more')
        if view_more == None:
            comunidades = scrap_tmp.class_finder('findall','commmunity-name')
            for i in comunidades:
                self.__lista_comunidades.append(i.text.strip())        
        elif view_more.text.find("View network profile") != -1:
            comunidades = scrap_tmp.class_finder('findall','account-site')
            for i in comunidades:
                self.__lista_comunidades.append(i.a.text.strip())   
        else:
            comunidades = scrap_tmp.class_finder('findall','community-name')
            for i in comunidades:
                self.__lista_comunidades.append(i.text.strip())    
        return self.__lista_comunidades

class Main(object):

    def main():
        #scrap = ScrapFactory("https://stackoverflow.com/users/8079899/clay-whaley")
        #scrap = ScrapFactory("https://stackoverflow.com/users/8079899/clay-whaley")
        #scrap = ScrapFactory("https://stackoverflow.com/questions/43120445/scraping-a-webpage-that-has-javascript-with-beautifulsoup")
        pregunta = Pregunta("https://stackoverflow.com/questions/43120445/scraping-a-webpage-that-has-javascript-with-beautifulsoup")
        pregunta.crea_lista_usuarios()
        pregunta.imprimeUsuarios()
        pregunta.imprime_bio()

    if __name__ == "__main__":
        main()








