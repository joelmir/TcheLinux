# coding: utf-8 

# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
# --------------- Rotina de Sorteio de Brindes do TcheLinux --------------- #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #

import random
import math
import os

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

# Limpa a tela
os.system('clear')

print "Seja bem vindo ao sorteio de brindes do TcheLinux"

# Verifica nomes duplicados
if (len(galera) != len(set(galera))):
	print "\n-> ERRO! Algum(a) safadinho(a) se cadastrou duas vezes!\n"
	exit()

print "Uma vez sorteado, seu nome não será mostrado novamente.\n"
print "Existem {0} pessoas na lista do sorteio! Bora lá?\n".format(len(galera))

while galera:
	# Prompt para sorteio
	if raw_input("Sortear mais um [s/n]? ") != "s":
		break

	# Nome do sorteado
	sorteado = random.choice(galera)
	print "\n-> E a pessoa sortuda é: {0}\n".format(sorteado)
	
	# Tira da lista
	galera.remove(sorteado)
		
# Se ao sair do loop a lista estiver vazia, avisa que não existe mais o que sortear
if not galera:
	print "Todas as pessoas já foram sorteadas."
print "Sorteio finalizado"