import mysql.connector
#lembrete: para funcionar usar o comando
#pip install mysql-connector-python

#função que estabelece a conexão com o banco de dados
def conectar_ao_banco(host, usuario, senha, banco_de_dados):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco_de_dados)
#função que executa uma consulta sql e retorna os resultados
def executar_consulta(conexao, consulta, parametros=None):
    cursor = conexao.cursor()
    cursor.execute(consulta, parametros)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados
#função que executa uma operação sql ma nao retorna os resultados (inserção, exclusão e etc)
def executar_operacao(conexao, consulta, parametros=None):
    cursor = conexao.cursor()
    cursor.execute(consulta, parametros)
    conexao.commit()
    cursor.close()

#funções pra operações específicas de usuário
def inserir_usuario(conexao, id, nome, pais, id_console):
    return executar_operacao(
        conexao, "INSERT INTO USUARIOS (id, nome, pais, id_console) VALUES (%s, %s, %s, %s)", (id, nome, pais, id_console))
def remover_usuario(conexao, id_usuario):
    return executar_operacao(
        conexao, "DELETE FROM USUARIOS WHERE id = %s", (id_usuario,))
def obter_todos_os_usuarios(conexao):
    return executar_consulta(conexao, "SELECT * FROM USUARIOS")

#função principal (main)
def main():
    #credenciais do banco de dados
    host = "host"
    usuario = "usuario"
    senha = "senha"
    banco_de_dados = "banco_de_dados"

    #estabelecendo a conexao
    conexao = conectar_ao_banco(host, usuario, senha, banco_de_dados)

    #EX: funções
    inserir_usuario(conexao, 1, "Jonas", "Brasil", 1)
    print("Usuários após inserção:")
    print(obter_todos_os_usuarios(conexao))

    remover_usuario(conexao, 1)
    print("Usuários após remoção:")
    print(obter_todos_os_usuarios(conexao))

    conexao.close()

if __name__ == "__main__":
    main()
