import sympy
import math

def gcd(a,b):
    while(1):
        t=a%b
        if t==0:
            return b
        a=b
        b=t

if __name__=="__main__":
    primeNumber1 = sympy.randprime(1000000000,9999999999)
    primeNumber2 = sympy.randprime(1000000000,9999999999)
    n= primeNumber1*primeNumber2
    phi = (primeNumber1-1)*(primeNumber2-1)
    e=2
    while e<phi:
        track = gcd(e,phi)
        if track==1:
            break
        else:
            e+=1

    d1 = 1/e
    d= math.fmod(d1,phi)
    message = int(input("Enter Your Message : "))
    c = pow(message,e)
    m = pow(c,d)
    C = math.fmod(c,n)
    M = math.fmod(m,n)

    print(f" Original Message : {message}")
    print(f" PrimeNumber1 p : {primeNumber1}")
    print(f" PrimeNumber2 q : {primeNumber2}")
    print(f" phi(n): phi({n})= {phi}")
    print(f" e = {e}")
    print(f" d = {e}")
    print(f" Encrypted Message = {C}")
    print(f" Decrypted Message = {M}")