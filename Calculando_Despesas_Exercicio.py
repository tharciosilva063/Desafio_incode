nome = input('Nome: ')
lancamentos=[]

def cadastro():
	natureza = int(input('natureza da despesa 1-Receita | 2-Despesa: '))
	planoContas = input('Plano de Contas: ')
	valor = float(input('Valor: '))
	registro = [id_lancamento,nome,natureza,planoContas,valor]
	lancamentos.append(registro)

def calculando():
	lancamentos_receitas = 0
	lancamentos_despesas = 0
	for lancamento in (lancamentos):
		if lancamento[2] == 1:
			lancamentos_receitas += lancamento[4]
		elif lancamento[2] == 2:
			lancamentos_despesas += lancamento[4]
	return print(f"""
=================== RESUMO FINANCEIRO ===========================
> Quantidade de lançamentos: {len(lancamentos)}                 
> Receita total R${lancamentos_receitas:.2f}				    
> Despesa total R${lancamentos_despesas:.2f}				    
> Liquido R${(lancamentos_receitas - lancamentos_despesas):.2f}
=================================================================
""")

while True:
	id_lancamento = len(lancamentos)+1
	try:
		cadastro()
		print('Deseja continuar com os Lançamentos ?')
		sair_encerrar = input('1-Continuar | Qualquer tecla para Sair: ')
		if sair_encerrar != '1':
			break
	except:
		print('Ops! Alguma informação inserido é invalido para o campo.')

calculando()	
