from Pregunta import Pregunta
#pregunta = Pregunta("https://stackoverflow.com/questions/43120445/scraping-a-webpage-that-has-javascript-with-beautifulsoup")
#pregunta = Pregunta('https://stackoverflow.com/questions/46498275/how-to-receive-input-from-extension-to-javascript')
#pregunta = Pregunta("https://stackoverflow.com/questions/89228/calling-an-external-command-in-python?rq=1")
pregunta = Pregunta("https://stackoverflow.com/questions/46575750/why-does-it-say-expected-declaration-specifiers-before-main")
#pregunta = Pregunta("https://parenting.stackexchange.com/questions/31906/if-my-5yr-old-is-an-exceptional-liar-should-i-expect-that-she-will-continue-lyi")

pregunta.crea_respuestas()
pregunta.crea_lista_usuarios()


#Ejemplo de utilización (1)
#temp = open('temp.txt','w', encoding='utf-8')
#pregunton = pregunta.get_usuario_que_pregunta_name()
#question = pregunta.get_pregunta()

#string = (
#'''
#USUARIO QUE REALIZA LA PREGUNTA: {}
#PREGUNTA: {}
#'''.format(pregunton,question)
#)
#temp.write(string)
#for i in pregunta.get_lista_respuestas():
#    usuario = i.get_usuario()
#    respuesta = i.get_respuesta()
#    fecha = i.get_fecha()
#    informe = (
#    '''
#    El usuario {} respondió:
#    {}
#    con fecha {}
#    '''.format(usuario,respuesta,fecha)
#    )
#    print(informe)
#    print("*" * 80)
#    temp.write(informe)
#    temp.write("*"*80)
#temp.close()


#Ejemplo de utilización(2)
pregunta.imprime_bio()
pregunta.imprimeUsuarios()
pregunta.imprime_comunidades()
#~ pregunta.imprime_respuestas()
#~ print(pregunta.get_lista_usuarios()[0].get_username())
#for i in pregunta.get_lista_usuarios():
#    print(i.get_username())
#    print(i.get_bio())
