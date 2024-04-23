def gerar_consulta_inner_join():
    return "SELECT * FROM tabela1 INNER JOIN tabela2 ON tabela1.id = tabela2.id"
#gerando comandos de sql para realizar inner joins
def gerar_comando_select():

    return gerar_consulta_inner_join()
def imprimir_consulta(consulta):
    print("Comando SQL gerado:")
    print(consulta)
def main():
    consulta = gerar_comando_select()
    imprimir_consulta(consulta)

if __name__ == "__main__":
    main()
