# coding: utf-8 

# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
# --------------- Rotina de Sorteio de Brindes do TcheLinux --------------- #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #

import random, math, os

# Limpa a tela
os.system('clear')

# Números que já foram sorteados
jaSorteados = []

# Nome do pessoal que vai participar do sorteio
galera = [
			'Fulaninho',
			'Ciclaninho',
			'Pedrinho',
			
			# Coloque seu nome aqui! :)
		 ]

# ------------------------------------------------------------------------- #
# ---------- Início da Rotina de Sorteio de Brindes do TcheLinux ---------- #
# ------------------------------------------------------------------------- #

print "Seja bem vindo ao sorteio de brindes do TcheLinux"

# Verifica nomes duplicados

if (len(galera) != len(set(galera))):
	print("\n-> ERRO! Algum(a) safadinho(a) se cadastrou duas vezes!\n")
	exit()
	

print "Uma vez sorteado, seu nome não será mostrado novamente.\n"
print "Existem "+str(len(galera))+" pessoas na lista do sorteio! Bora lá?\n"

#Embaralha a galera toda da lista
random.shuffle(galera)

while True:
	# Prompt para sorteio
	vaiMais = raw_input("Sortear mais um [s/n]? ")
	
	if vaiMais == "s":
		# Ao esvaziar a lista, encerra o programa
		if len(galera) < 1:
			print("\nVixi! Não existem mais pessoas para sortear!\n")
			break
		
		# Nome do sorteado (ultima posição)
		print("-> E a pessoa sortuda é: "+galera[-1]+"\n")
		
		# Remove o nome do sorteado da lista
		jaSorteados.append(galera.pop())
		
	else:
		break
		
print "\nFim do programa\n"