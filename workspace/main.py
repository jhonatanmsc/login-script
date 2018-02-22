# Auth: jhonatanmsc
# v 1.2
from os import system
from user import User
from log import Log

def limpar():
    system('cls')

def main():

    while True:
        user = User.get_instance()
        limpar()
        try:
        
            titulo = '<<        LoGin ScRiPt | versão 1.2        >>'
            
            print(titulo)
            login = input("Digite seu login: ")
            passwd = input("Digite sua senha: ")
            User.get_instance(login, passwd)
            Log.check_host()

        except KeyboardInterrupt as e:
            break

    print('\nfim da aplicação.')
if __name__ == '__main__':
    main()