from os import remove, system

def loop(p):
	global t
	t = ''
	carc = []
	for c in range(p):
		arq.write(f'{t}for c{c} in char:\n')
		t = t + '\t'
		carc.append('c' + str(c))
	arq.write(f'{t}palavra = {" + ".join(carc)}\n')
	arq.write(t+"arq.write(f'{palavra}\\n')\n")

try:
    system('clear')
except:
    system('cls')
print('''
  ___ _____   _ _ __ ___   __ _ _ __   __| (_) __ _ ___ 
 / _ \_  / | | | '_ ` _ \ / _` | '_ \ / _` | |/ _` / __|
| (_) / /| |_| | | | | | | (_| | | | | (_| | | (_| \__ \ 
 \___/___|\__, |_| |_| |_|\__,_|_| |_|\__,_|_|\__,_|___/
          |___/                                         
  

							by: HENRIQUE
	  /"*._         _
      .-*'`    `*-.._.-'/
    < * ))     ,       ( 
      `*-._`._(__.--*"`.\ 

''')


n1 = int(input('Digite a quantidade inicial de carácteres: '))
n2 = int(input('Digite a quatidade final: '))
char = input('Digite os carácteres: ')
nome = input('Digite o nome do arquivo (com a extensão): ')

arq = open('word.py', 'w')

arq.write('from sys import argv\nchar = argv[1:]\n')

arq.write(f"arq = open('{nome}', 'w')\n")


for c in range(n1, n2 + 1):
	loop(c)

arq.close()

try:
	system(f'python3 word.py {char}')
except:
	system(f'python word.py {char}')
	
remove('word.py')
print('Wordlist criada')
