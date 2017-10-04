from bs4 import BeautifulSoup
import requests
import time
                
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
        self.__soup = BeautifulSoup(requests.get(url).text,'html5lib')
        self.__url = url

    #~ Métodos
    def get_username(self):
        return self.__username
    
    def get_bio(self):
        p = self.__soup.find(attrs = {'class': 'about'})
        self.__bio = p.contents[5].text        
        return self.__bio
    
    def get_comunidades(self):
        r = requests.get(self.__url)
        texto = r.text
        soup_comunidades = BeautifulSoup(r.text, 'html5lib')
        view_more = soup_comunidades.find(attrs = {'class':'view-more'})
        if view_more == None:
            comunidades = soup_comunidades.find_all(attrs = {'class':'community-name'})
            for i in comunidades:
                self.__lista_comunidades.append(i.text.strip())        
        elif view_more.text.find("View network profile") != -1:
            #print(view_more.a['href'])
            #r = requests.get(view_more.a['href'])
            #texto = r.text
            #soup_comunidades = BeautifulSoup(r.text,'html5lib')
            comunidades = soup_comunidades.find_all(attrs = {'class':'account-site'})
            for i in comunidades:
                self.__lista_comunidades.append(i.a.text.strip())   
        else:
            comunidades = soup_comunidades.find_all(attrs = {'class':'community-name'})
            for i in comunidades:
                self.__lista_comunidades.append(i.text.strip())    
        return self.__lista_comunidades
    
    


            
    
    
        
    
    
