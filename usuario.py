"""
Requisito: Login
Usuario é a classe base. Cada subclasse define sua própria forma de
identificação e validação:
  - Aluno    -> login pelo RA (Registro Acadêmico)
  - Servidor -> login pelo CPF (cobre servidores técnico-administrativos
                e professores, já que ambos usam o mesmo tipo de documento)
"""

from abc import ABC, abstractmethod
import re


class Usuario(ABC):
    def __init__(self, nome, identificador):
        self.nome = nome
        self.identificador = identificador

    @abstractmethod
    def tipo(self):
        """Retorna o tipo do usuário (usado pelas regras de vaga)."""
        raise NotImplementedError

    @abstractmethod
    def validar_identificador(self):
        """Valida se o identificador está no formato esperado para o tipo de usuário."""
        raise NotImplementedError

    def __repr__(self):
        return f"{self.__class__.__name__}(nome={self.nome!r}, id={self.identificador!r})"


class Aluno(Usuario):
    """Login feito através do RA (Registro Acadêmico)."""

    def tipo(self):
        return "aluno"

    def validar_identificador(self):
        ra = self.identificador.strip()
        # RA: apenas dígitos, tamanho típico entre 6 e 10 caracteres
        return ra.isdigit() and 6 <= len(ra) <= 10


class Servidor(Usuario):
    """
    Login feito através do CPF.
    Cobre tanto servidores técnico-administrativos quanto professores,
    já que ambos se autenticam da mesma forma (CPF).
    """

    def tipo(self):
        return "servidor"

    def validar_identificador(self):
        cpf = re.sub(r"\D", "", self.identificador)
        return len(cpf) == 11


class SistemaLogin:
    """Recebe um Usuario já construído (Aluno ou Servidor) e valida o login."""

    def __init__(self):
        self.usuario_logado = None

    def login(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("Login requer uma instância de Usuario (Aluno ou Servidor).")
        if not usuario.validar_identificador():
            raise ValueError(
                f"Identificador inválido para {usuario.__class__.__name__}: "
                f"{usuario.identificador!r}"
            )
        self.usuario_logado = usuario
        return usuario

    def logout(self):
        self.usuario_logado = None
