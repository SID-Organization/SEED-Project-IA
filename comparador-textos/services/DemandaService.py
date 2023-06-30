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

        sql = "INSERT INTO demanda (id_demanda, titulo, proposta_melhoria, descricao_qualitativo, frequencia_uso_demanda, situacao_atual_demanda) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (demanda.id_demanda, demanda.titulo, demanda.proposta_melhoria, demanda.descricao_qualitativo, demanda.frequencia_uso_demanda, demanda.situacao_atual_demanda)

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

        print(resultado)

        if resultado:
            return Demanda(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
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

    def obter_todas_demandas(self):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()

        sql = "SELECT * FROM demanda"

        cursor.execute(sql)
        resultado = cursor.fetchall()

        cursor.close()
        conexao.close()

        demandas = []

        for item in resultado:
            demandas.append(Demanda(item[0], item[1], item[2], item[3], item[4], item[5]))

        return demandas
