#Agenda Telefonica Sagui
import funcoes

funcoes.bemvindo()

#Opcoes do Usuario
opcao = int(raw_input())
print("Selecionou a ", opcao)


#Estrutura de controle
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
else:
	funcoes.falha()


