import MySQLdb


def configurar_banco_dados():
    host = 'localhost'
    usuario = 'root'
    senha = 'root'
    nome_banco = 'db_sid_ia_sandbox1'

    conexao = MySQLdb.connect(
        host=host,
        user=usuario,
        passwd=senha,
        db=nome_banco
    )

    cursor = conexao.cursor()

    tabela_demanda = """
    CREATE TABLE IF NOT EXISTS demanda (
        id_demanda INT PRIMARY KEY AUTO_INCREMENT,
        titulo VARCHAR(255) NOT NULL,
        proposta_melhoria TEXT,
        descricao_qualitativo TEXT,
        frequencia_uso_demanda TEXT,
        situacao_atual_demanda TEXT
    )
    """
    cursor.execute(tabela_demanda)

    conexao.commit()
