# Auth: jhonatanmsc
# v 1.0
from user import User
from log import Log

def main():

    while True:
        user = User.get_instance()
        print(user)
        try:
            if user:
                titulo = '<<        usuario: '+user.login+'      >>'

            else:
                titulo = '<<        LoGin ScRiPt      >>'
            
            print(titulo)
            login = input("Digite seu login: ")
            passwd = input("Digite sua senha: \n")
            User.get_instance(login, passwd)
            Log.check_host()

        except KeyboardInterrupt as e:
            break

    print('\nfim da aplicação.')
if __name__ == '__main__':
    main()