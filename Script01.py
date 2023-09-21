List keyword


import keyword

listkeyword=keyword.kwlist
print(listkeyword)
print(len(listkeyword))

#Les types de données en python


    1 int
    2 float
    3 complex
    4 bool
    5 str
    6 bytes
    7 bytearray
    8 range
    9 list
    10 tuple
    11 set
    12 frozenset
    13 dict
  
    
    
    

a=20
b=62.5
c=2+3j
d='test'

# Les fonctions suivantes sont natives à python:print(),id(),type()
# les types entier (int)
print(a)

type(a)

id(a)
type(a)
print(a)

id(a)

type(a)

print(a)

id(a),type(a),print(a)

id(c),type(c),print(c)

id(d),type(d),print(d)

# pour representer un nombre entier en binaiore on le préfixe avec 0b ou 0B:
a=0b00011
print(a)

# en octale avec 0o ou 0O:
b=0o12345
print(b)

# en hexadecimale avec 0x ou 0X:
c=0xfaf
print(c)

# pour convertir n'importe quel nombre entier vers la base binaire:
bin(15)

bin(0xface)

# pour convertir n'importe quel nombre entier vers la base octale:
oct(25)

oct(0xface)


# pour convertir n'importe quel nombre entier vers la base hexadicimale:
hex(256)

hex(174658)

# nombre à virgule flottante (float)
a=1.25
print(a)

type(a)

b=1.2e3
print(b)

c=1.5E4
print(c)

# nombre complexe : a+bj
a=3+6j
print(a)

type(a)

print(a.real)

print(a.imag)

# booléen : True, False
a=True
b=False
print(a)
print(b)

type(a)
type(b)

c=5>10
print(c)

d=True+True
print(d)

e=True+True
print(e)

# Le type chaine de caractère(str):
s1="sara"
s2="haithem"
s3="azzabi"
print(s1,s2,s3)

s4="Python est 'facile'"
print(s4)

s4="Python est "facile""
print(s4)

s4='Python est "facile"'
print(s4)

s4='Python est 'facile'''
print(s4)

