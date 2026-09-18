"""
Requisito: Rastreamento do estacionamento
Estacionamento monta as 44 vagas do campus (12 destinadas a servidores,
8 especiais e 24 comuns) e permite que qualquer usuário registre em qual
vaga estacionou, informando apenas o número dela.

Numeração das vagas:
  1  a 12 -> VagaDestinada (servidores)
  13 a 20 -> VagaEspecial  (PCD/idoso)
  21 a 44 -> VagaComum
"""

from vaga import VagaComum, VagaEspecial, VagaDestinada


class Estacionamento:
    TOTAL_VAGAS = 44
    QTD_DESTINADA = 12
    QTD_ESPECIAL = 8
    # o restante (44 - 12 - 8 = 24) é comum

    def __init__(self):
        self.vagas = {}
        self._montar_vagas()

    def _montar_vagas(self):
        numero = 1
        for _ in range(self.QTD_DESTINADA):
            self.vagas[numero] = VagaDestinada(numero)
            numero += 1
        for _ in range(self.QTD_ESPECIAL):
            self.vagas[numero] = VagaEspecial(numero)
            numero += 1
        qtd_comum = self.TOTAL_VAGAS - self.QTD_DESTINADA - self.QTD_ESPECIAL
        for _ in range(qtd_comum):
            self.vagas[numero] = VagaComum(numero)
            numero += 1

    def registrar_estacionamento(self, numero_vaga, usuario):
        """
        Registra que 'usuario' estacionou na vaga 'numero_vaga'.
        Sempre ocupa a vaga (não há bloqueio físico) e retorna None se o
        acesso for compatível, ou a mensagem de aviso caso contrário.
        """
        vaga = self.vagas.get(numero_vaga)
        if vaga is None:
            raise ValueError(f"Vaga {numero_vaga} não existe.")

        aviso = vaga.verificar_acesso(usuario)
        vaga.ocupar(usuario)
        return aviso

    def liberar_vaga(self, numero_vaga):
        vaga = self.vagas.get(numero_vaga)
        if vaga is None:
            raise ValueError(f"Vaga {numero_vaga} não existe.")
        vaga.liberar()

    def vagas_disponiveis(self):
        return [numero for numero, vaga in self.vagas.items() if vaga.esta_livre()]

    def mapa(self):
        linhas = []
        for numero, vaga in self.vagas.items():
            if vaga.esta_livre():
                status = "livre"
            else:
                status = f"ocupada por {vaga.ocupante.identificador}"
            linhas.append(f"  Vaga {numero:>2} ({vaga.tipo()}): {status}")
        return "\n".join(linhas)
