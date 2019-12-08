#Public/Private keys

import random


def primenum():
	return next((x for x in (lambda y: random.shuffle(y) or y)(list(range(1000, 2000))) if not [t for t in range(2, x) if not x % t]), None)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
	return gcd(a, b) == 1, a

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

#e*d (MOD N)
def privatekey(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

def publickey(RP):
	while True:
		e = coprime(random.randrange(10, 100), RP)
		if e[0] == True:
			print("e:",e[1])
			e = int(e[1])
			break
	return e

def txtToCipher(txt, e, N):
	#C=Encryption=M**e (MOD N)
	return [M**e%N for M in (ord(c) for c in txt)]

def cipherToTxt(cipher, d, N):
	#M=Decryption=C**d (MOD N)
	#m = C**d % N 
	return ''.join((chr(txt) for txt in (C**d%N for C in cipher)))

def sign(txt, d, N):
	return [M**d%N for M in (ord(c) for c in txt)]

def verify(signedTxt, txt, e, N):
	if txt != ''.join((chr(txt) for txt in (C**e%N for C in signedTxt))):
		return False
	else:
		return True


#Tar fram primtal
p = primenum()
q = primenum()

N = p*q
RP= (p-1)*(q-1)
e = publickey(RP)
print("RP:",RP)
print("N:", N)

d = privatekey(e, RP)
print("d:", d)

signedTxt = sign('test', d, N)
print('signed:', signedTxt)


verified = verify(signedTxt, 'test', e, N)
print('The sender is verified(True/False):', verified)

"""
cipher = txtToCipher('wtf', e, N)
print("cipher txt:", cipher)



txt = cipherToTxt(cipher, d, N)

print(txt)
"""


