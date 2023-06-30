# A classe possuirá um objeto Demanda e um int similaridade

class DemandaSimilar:
    def __init__(self, demanda, similaridade):
        self.demanda = demanda
        self.similaridade = similaridade

    def to_dict(self):
        return {
            'demanda': self.demanda.to_dict(),
            'similaridade': self.similaridade
        }