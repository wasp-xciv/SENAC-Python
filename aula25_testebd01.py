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