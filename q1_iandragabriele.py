import sys

#valida, socilcita o tipo de transação e coleta os detalhes + tratamento de erros
def selecionar_tipo_transacao():
    try:
        return int(input("Escolha o tipo de transação ou sair:\n[1] Dinheiro \n[2] Transferência de Fundos\n[3] Crédito\n[4] Sair\n"))
    except ValueError:
        print("Erro: Insira um número válido.")
        return selecionar_tipo_transacao()
def validar_tipo_transacao(tipo_transacao):
    if tipo_transacao in [1, 2, 3, 4]:
        return tipo_transacao
    else:
        print("Erro: Tipo de transação inválido.")
        return validar_tipo_transacao(selecionar_tipo_transacao())
def obter_detalhes_transacao(tipo_transacao):
    try:
        cliente = input("Nome do cliente: ")
        valor = float(input("Valor: R$"))
    except ValueError:
        print("Erro: Valor inserido inválido.")
        return obter_detalhes_transacao(tipo_transacao)
    return {
        "cliente": cliente,
        "valor": valor,
        "tipo": validar_tipo_transacao(tipo_transacao)
    }

#processando transações de acordo com a modalidade escolhida
def pagamento_em_dinheiro(detalhes_transacao):
    print(f"Valor: R$ {detalhes_transacao['valor']}\nStatus: Pago")
    return confirmar_transacao_dinheiro(detalhes_transacao)
def pagamento_credito(detalhes_transacao):
    return confirmar_transacao_credito(detalhes_transacao)
def deposito_bancario(detalhes_transacao):
    return confirmar_transacao_bancaria(detalhes_transacao)
def processar_transacao(processador_dinheiro, processador_banco, processador_credito, detalhes_transacao):
    #aqui processa uma transação baseada no tipo dela
    tipo_transacao = detalhes_transacao["tipo"]
    if tipo_transacao == 1:
        return processador_dinheiro(detalhes_transacao)
    if tipo_transacao == 2:
        return processador_banco(detalhes_transacao)
    if tipo_transacao == 3:
        return processador_credito(detalhes_transacao)
    if tipo_transacao == 4:
        print("Encerrando operações")
        sys.exit()

#confirmações de transições de acordo com a modalidade
def confirmar_transacao_dinheiro(transacao):
    return f"CLIENTE: {transacao['cliente']}\nSTATUS: CONCLUÍDO\n "
def confirmar_transacao_bancaria(transacao):
    return confirmar_transacao_com_credenciais(transacao, 
        {"banco": input("Insira o nome do banco: "), 
        "id": input("Insira o seu CPF"), 
        "senha": input("Insira a sua senha")},
        input("Confirmar?\n[S]im\n[N]ão\n"))
def confirmar_transacao_credito(transacao):
    return confirmar_transacao_com_credenciais(transacao, 
        {"cartao": input("Insira a bandeira do cartão: "), 
        "senha": input("Insira a sua senha")},
        input("Confirmar?\n[S]im\n[N]ão\n"))
def confirmar_transacao_com_credenciais(transacao, credenciais, opcao_confirmacao):
    if opcao_confirmacao.lower() == "s":
        print("Encerrando operações")
        sys.exit()
    if transacao["tipo"] == 2:
        return {
            "cliente": transacao["cliente"],
            "tipo": "transferência bancária",
            "banco": credenciais["banco"],
            "status": "confirmado"
        }
    if transacao["tipo"] == 3:
        return {
            "cliente": transacao["cliente"],
            "tipo": "crédito",
            "cartao": credenciais["cartao"],
            "status": "confirmado"
        }
print("Bem vindo(a) ao processador de pagamentos")
tipo_transacao = selecionar_tipo_transacao()
print(processar_transacao(pagamento_em_dinheiro, deposito_bancario, pagamento_credito, obter_detalhes_transacao(tipo_transacao)))
