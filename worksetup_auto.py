import webbrowser as wb 
#Abrir automaticamente URLs em um navegador web específico
#Importa o módulo webbrowser e renomeia-o para wb para facilitar o uso
import os
#Permite a execução de comandos do sistema operacional.

def workAuto():
    #Define o caminho do executável do Sublime Text 3 
    codePath = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe %s'
    #Abrir o Sublime Text.
    os.startfile(codePath)
    #Armazena o caminho do executável do navegador que você deseja usar
    # %s no final do caminho é um marcador de posição que será substituído pela URL ao abrir o navegador
    path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    #Sites que quer visitar, URLs completas, incluindo o protocolo "https://".
    urls = ('https://gmail.com', 'https://google.com', 'https://youtube.com')

    #Um loop for percorre cada URL na tupla urls e utiliza o método open 
    #do objeto webbrowser para abrir cada URL no navegador especificado.
    for url in urls:
        wb.get(path).open(url)


workAuto()



