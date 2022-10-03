# using random librery
import random
import caracters

def run():
    lengthPassword = input("¿Cuantos caracteres deseas que contenga la contraseña?")
    if(int(lengthPassword) <= 0 or lengthPassword.islower() or lengthPassword.isupper()):
        print("ingresa una cantidad valida")
    else:
        pass
        arrayListCaractersJoined = caracters.MAYUS+caracters.MINUS+caracters.NUMS+caracters.CHARS
        print(arrayListCaractersJoined) 
        

# call function
if __name__ == '__main__':
    run()