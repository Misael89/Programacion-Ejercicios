num=int(input('Introdusca el numero al que le quiere buscar el factorial: '))
def fact(num):
    if num>0:
        fact=1
        for i in range(2,num+1):
            fact=fact*i
        print('El Factorial del numero introducido es',fact)
    else:
        print('Esta operacios solo se puede efectual con numeros mayores a 0')
        
fact(num)
