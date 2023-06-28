import MySQLdb

from models.entities.Demanda import Demanda


class DemandaService:
    def __init__(self):
        self.host = 'localhost'
        self.usuario = 'root'
        self.senha = 'root'
        self.nome_banco = 'db_sid_ia_sandbox1'

    def obter_conexao(self):
        return MySQLdb.connect(
            host=self.host,
            user=self.usuario,
            passwd=self.senha,
            db=self.nome_banco
        )

    def criar_demanda(self, demanda):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()

        sql = "INSERT INTO demanda (id_demanda, titulo, proposta_melhoria, descricao_qualitativo) VALUES (%s, %s, %s, %s)"
        valores = (demanda.id_demanda, demanda.titulo, demanda.proposta_melhoria, demanda.descricao_qualitativo)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

    def obter_demanda_por_id(self, id_demanda):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()

        sql = "SELECT * FROM demanda WHERE id_demanda = %s"
        valores = (id_demanda,)

        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

        if resultado:
            id_demanda, titulo, proposta_melhoria, descricao_qualitativo = resultado
            return Demanda(id_demanda, titulo, proposta_melhoria, descricao_qualitativo)
        else:
            return None

    def atualizar_demanda(self, demanda):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()

        sql = "UPDATE demanda SET titulo = %s, proposta_melhoria = %s, descricao_qualitativo = %s WHERE id_demanda = %s"
        valores = (demanda.titulo, demanda.proposta_melhoria, demanda.descricao_qualitativo, demanda.id_demanda)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

    def excluir_demanda(self, id_demanda):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()

        sql = "DELETE FROM demanda WHERE id_demanda = %s"
        valores = (id_demanda,)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()
