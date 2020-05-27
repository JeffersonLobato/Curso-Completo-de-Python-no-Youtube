import sqlite3

conexao = sqlite3.connect('aula44.db')
c = conexao.cursor()


requisicao = 'SELECT * FROM usuario WHERE nome = ?'

for linha in c.execute(requisicao, ('Natali',)):
    print(linha)