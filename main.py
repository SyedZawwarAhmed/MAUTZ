from modules.tokenize import tokenize

variableString = 'ye car123,apple11,house101;'
ifString = '''
agar a % 5 == 0 aur a == 5 :
\ta = 10
magar phir a % 5 > 0 :
\ta = 8
warna :
\ta = 2
'''
loopString = '''
ye num1,nateeja,num2;
num2 = 0
num1 = 1
jab tak num1 + num2 <= 10 aur num1 == 1 :
\tnateeja = 2 * num2
\tdikhao ( nateeja )
\tnum2 ++
'''

functionString = '''
Kaam jamaKaro ( ye a, ye b ) :
\tye c;
\tc = a + b
\tbhejo c
'''

print(tokenize(variableString))
print(tokenize(ifString))
print(tokenize(loopString))
print(tokenize(functionString))
