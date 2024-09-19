'''On importe la fonction sqrt'''
from math import sqrt


def isprime(p:int)->bool:
    '''On veut vérifier si p est permier ou non'''
    k=int(sqrt(p))
    if p in (0,1):
        return False
    for i in range(2,k+1):#1 ne rentre pas dans notre etude et k+1>int(sqrt(p))
        if p%i==0:#si p est divible par i alors ce n'est pas un nb premier
            return False
    return True
#### Fonction principale

def main():
    '''Utilise la fonction isprime pour déterminer les nombres premiers entre 0 et 100'''
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
