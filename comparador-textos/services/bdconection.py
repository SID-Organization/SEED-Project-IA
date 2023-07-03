import MySQLdb


def configurar_banco_dados():
    host = 'localhost'
    usuario = 'root'
    senha = 'root'
    nome_banco = 'db_sid_sandbox2'

    conexao = MySQLdb.connect(
        host=host,
        user=usuario,
        passwd=senha,
        db=nome_banco
    )

    cursor = conexao.cursor()

    conexao.commit()
