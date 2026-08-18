#testar conexões do bd com Dicionário: excelente para armazenar configurações.
import pymysql

#configurações do bd em um dicionário com as credenciais de acesso.
DB_CONFIG = {
    "host": "localhost", #Endereço do servidor (local nesta máquina).
    "user": "root", #Usuário do MySQL.
    "password": "", #Senha do usuário (não tem nesse caso).
    "database": "bdclientes",   #Nome do banco de dados a ser utilizado.
    "charset": "utf8mb4",   #Codificação de caracteres para suportar acentos.
    "cursorclass": pymysql.cursors.Cursor,#Tipo de cursor (padrão para executar queries).
    "autocommit": False #Desabilita autocommit para controlar manualmente as transações.
}

#Função que cria e retorna uma conexão com o bd
def conectar():
    return pymysql.connect(**DB_CONFIG) #Desempacota o dicionário DB_CONFIG como argumentos.

#Função que testa a conexão com o bd. A conexão não pode ficar aberta o tempo todo,
# ela se abre apenas quando necessário e se fecha logo em seguida, caso contrário, ficaria
#vulnerável a ataques e consumiria recursos desnecessários do servidor.
def testar_conexao():
    try:
    #tenta estabelecer a conexão com o bd.
        conexao = conectar()
        print("Conexão bem-sucedida ao banco de dados!")
    except pymysql.MySQLError as e:
    #Captura e exibe qualquer erro que ocorra durante a conexão.
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
    #Garante que a conexão seja fechada após o teste.
        if 'conexao' in locals() and conexao.open:
            conexao.close()
            print("Conexão encerrada.")
            
#Executa a função de teste de conexão quando o script é executado diretamente.
if __name__ == "__main__":
    testar_conexao()