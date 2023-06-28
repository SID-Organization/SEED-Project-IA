class Demanda:
    def __init__(self, id_demanda, titulo, proposta_melhoria, descricao_qualitativo, frequencia_uso_demanda,
                 situacao_atual_demanda):
        self.id_demanda = id_demanda
        self.titulo = titulo
        self.proposta_melhoria = proposta_melhoria
        self.descricao_qualitativo = descricao_qualitativo
        self.frequencia_uso_demanda = frequencia_uso_demanda
        self.situacao_atual_demanda = situacao_atual_demanda

    def to_dict(self):
        return {
            'id_demanda': self.id_demanda,
            'titulo': self.titulo,
            'proposta_melhoria': self.proposta_melhoria,
            'descricao_qualitativo': self.descricao_qualitativo,
            'frequencia_uso_demanda': self.frequencia_uso_demanda,
            'situacao_atual_demanda': self.situacao_atual_demanda
        }
