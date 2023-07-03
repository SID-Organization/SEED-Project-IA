import MySQLdb

from models.entities.Demanda import Demanda


class DemandaService:
    def __init__(self):
        self.host = 'localhost'
        self.usuario = 'root'
        self.senha = 'root'
        self.nome_banco = 'db_sid_sandbox2'

    def obter_conexao(self):
        return MySQLdb.connect(
            host=self.host,
            user=self.usuario,
            passwd=self.senha,
            db=self.nome_banco
        )

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
            return Demanda(resultado[0], resultado[15], resultado[10], resultado[4], resultado[5], resultado[12])
        else:
            return None

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
            demandas.append(Demanda(item[0], item[15], item[10], item[4], item[5], item[12]))

        return demandas
