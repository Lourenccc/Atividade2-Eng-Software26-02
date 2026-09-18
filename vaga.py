"""
Requisito: Tratativa de vaga errada + base para o rastreamento
Vaga é a classe base. Cada subclasse define sua própria regra de
verificar_acesso(usuario), que devolve None se o uso for compatível ou uma
mensagem de aviso caso contrário (não há bloqueio físico, só aviso).
"""

from abc import ABC, abstractmethod


class Vaga(ABC):
    def __init__(self, identificador):
        self.identificador = identificador
        self.ocupante = None

    @abstractmethod
    def tipo(self):
        """Retorna o tipo da vaga (usado no mapa do estacionamento)."""
        raise NotImplementedError

    @abstractmethod
    def verificar_acesso(self, usuario):
        """Retorna None se o uso for compatível, ou uma mensagem de aviso."""
        raise NotImplementedError

    def esta_livre(self):
        return self.ocupante is None

    def ocupar(self, usuario):
        if not self.esta_livre():
            raise ValueError(f"Vaga {self.identificador} já está ocupada.")
        self.ocupante = usuario

    def liberar(self):
        self.ocupante = None

    def __repr__(self):
        status = "livre" if self.esta_livre() else f"ocupada por {self.ocupante.identificador}"
        return f"{self.__class__.__name__}({self.identificador}, {status})"


class VagaComum(Vaga):
    """Vaga comum: aceita qualquer usuário (aluno, servidor ou PCD/idoso)."""

    def tipo(self):
        return "comum"

    def verificar_acesso(self, usuario):
        return None


class VagaEspecial(Vaga):
    """Vaga especial: aceita somente usuários com necessidade especial (PCD/idoso)."""

    def tipo(self):
        return "especial"

    def verificar_acesso(self, usuario):
        if not usuario.necessidade_especial:
            return (
                f"Aviso: {usuario.identificador} ({usuario.tipo()}) estacionou em "
                f"vaga especial (PCD/idoso) sem necessidade especial cadastrada."
            )
        return None


class VagaDestinada(Vaga):
    """Vaga destinada a servidores (inclui professores) e a PCD/idoso."""

    def tipo(self):
        return "destinada"

    def verificar_acesso(self, usuario):
        if usuario.tipo() == "servidor" or usuario.necessidade_especial:
            return None
        return (
            f"Aviso: {usuario.identificador} (aluno) estacionou em vaga "
            f"reservada a servidores. Procure uma vaga comum."
        )
