# using random librery
import random
import caracters
from colorama import init, Fore, Back, Style
init()

def run():
    print(Fore.CYAN + """                                                 
 _______   _____________   _____ _____  _____ _     
|  ___\ \ / /_   _|  ___| |_   _|  _  ||  _  | |    
| |__  \ V /  | | | |_      | | | | | || | | | |    
|  __| /   \  | | |  _|     | | | | | || | | | |    
| |___/ /^\ \_| |_| |       | | \ \_/ /\ \_/ / |____
\____/\/   \/\___/\_|       \_/  \___/  \___/\_____/
                                                    """)
    print("")
    print(Fore.RED + "Recuerde no usar letras")
    print(Fore.LIGHTBLUE_EX + "Numero de contraseña maxima 88")
    print(Style.RESET_ALL)

    lengthPassword = input("¿Cuantos caracteres deseas que contenga la contraseña? ")
    settingPassword = input("¿Desea caracteres mayusculas o minusculas?")
    if(settingPassword == "Mayusculas" or "mayusculas"):
        makePassword(lengthPassword)
    if int(lengthPassword) <= 0 or int(lengthPassword) > 88:
        print("ingresa una cantidad valida o menor a 88")
        makePassword(lengthPassword)


# make password function
def makePassword(lengthPassword):
            # join lists to create a new password
        arrayListCaractersJoined = caracters.MAYUS+caracters.MINUS+caracters.NUMS+caracters.CHARS

        # create password
        makePass = random.sample(arrayListCaractersJoined, int(lengthPassword))
        password = "".join(makePass)
        print(Fore.CYAN + password)

        print("")
        print("")
        quest = input(Fore.LIGHTYELLOW_EX + """crear otra contraseña
              Si = 1
              No = 2
              """)
        if(quest == str(1)):
            run()   
        elif(quest == str(2)):
            exit()

# call function
if __name__ == '__main__':
    run()
