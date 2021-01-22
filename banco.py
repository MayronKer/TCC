from run import db


# class == banco de dados no SQL
class TCC(db.Model):
    # __tablename__ == uma tabela no SQL
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(45))
    senha = db.Column(db.String)
    emil = db.Column(db.String, unique = True)

    # Construtor -> todos os parâmetros são necessários
    def __init__(self, nome, senha, email):
        self.nome = nome
        self.senha = senha
        self.email = email

    # representatios -> Como irá aparecer quando chamado
    def __repr__(self):
        return "<Nome %r>" % sellf.nome
