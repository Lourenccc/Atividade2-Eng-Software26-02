"""
PLANO (Passo 1)
Requisitos escolhidos, na ordem de implementação:
  1. Login (usuario.py) — Aluno por RA, Servidor/Professor por CPF — ~15 min
  2. Regras de vaga (vaga.py) — VagaComum / VagaEspecial / VagaDestinada — ~15 min
  3. Rastreamento (estacionamento.py) — 44 vagas, registro por número — ~20 min
  4. Ponto de entrada (este arquivo) — integra tudo num menu de linha de
     comando — ~10 min
IA: usada para estruturar as classes por requisito e o fluxo deste ponto de
entrada; a numeração das vagas e as regras de acesso foram definidas e
conferidas manualmente contra o levantamento de requisitos original.
"""

from usuario import Aluno, Servidor, SistemaLogin
from estacionamento import Estacionamento


def fazer_login():
    print("=== Login ===")
    print("1 - Aluno (login por RA)")
    print("2 - Servidor/Professor (login por CPF)")

    while True:
        opcao = input("Escolha o tipo de usuário [1/2]: ").strip()
        if opcao in ("1", "2"):
            break
        print("Opção inválida, digite 1 ou 2.")

    nome = input("Nome: ").strip()
    pcd = input("Possui necessidade especial (PCD/idoso)? (s/n): ").strip().lower() == "s"

    sistema = SistemaLogin()

    while True:
        if opcao == "1":
            identificador = input("Digite seu RA: ").strip()
            usuario = Aluno(nome, identificador, necessidade_especial=pcd)
        else:
            identificador = input("Digite seu CPF: ").strip()
            usuario = Servidor(nome, identificador, necessidade_especial=pcd)

        try:
            sistema.login(usuario)
            break
        except ValueError as erro:
            print(f"Erro: {erro}")
            print("Tente novamente.")

    print(f"\nLogin realizado com sucesso: {usuario} — tipo: {usuario.tipo()}\n")
    return usuario


def registrar_vaga(est, usuario):
    entrada = input("Digite o número da vaga em que estacionou: ").strip()
    if not entrada.isdigit():
        print("Número de vaga inválido.")
        return

    numero_vaga = int(entrada)
    try:
        aviso = est.registrar_estacionamento(numero_vaga, usuario)
    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    if aviso:
        print(aviso)
    else:
        print(f"Vaga {numero_vaga} registrada com sucesso.")


def menu_estacionamento(est, usuario):
    while True:
        print("\n=== Menu ===")
        print("1 - Registrar vaga onde estacionei")
        print("2 - Ver vagas disponíveis")
        print("3 - Ver mapa completo do estacionamento")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_vaga(est, usuario)
        elif opcao == "2":
            disponiveis = est.vagas_disponiveis()
            print(f"Vagas disponíveis ({len(disponiveis)}): {disponiveis}")
        elif opcao == "3":
            print(est.mapa())
        elif opcao == "4":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")


def main():
    est = Estacionamento()
    usuario = fazer_login()
    menu_estacionamento(est, usuario)


if __name__ == "__main__":
    main()


"""
AUTOAVALIAÇÃO (Passo 3)
- Critérios atingidos: protótipo roda do início ao fim sem editar código
  (basta rodar `python3 entry_point.py`); cada requisito em classe própria,
  em arquivo separado do ponto de entrada (usuario.py, vaga.py,
  estacionamento.py); ponto de entrada único; histórico com commits
  identificando cada requisito; README explicando o que o protótipo faz.
- Requisito mais difícil de traduzir em código: a regra de acesso das vagas,
  porque "quem pode estacionar onde" mudou mais de uma vez durante a
  conversa (vaga comum aceita todos, destinada aceita servidor e PCD,
  especial só PCD) — resolvido com necessidade_especial como atributo
  independente do tipo de usuário.
- Uso de IA: ajudou a estruturar rápido as classes por requisito e o menu de
  linha de comando; atrapalhou quando a primeira versão da regra de acesso
  não bateu com o que eu realmente queria, precisei corrigir manualmente.
"""
