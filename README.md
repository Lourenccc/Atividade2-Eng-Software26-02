# Atividade 2 — Eng. Software: Dos Requisitos ao Protótipo Inicial

Protótipo em linha de comando (Python, POO) que implementa 3 requisitos do
levantamento de requisitos do app de controle de vagas do estacionamento do
campus:

1. **Login simples** — acesso rápido, sem senha, identificando o usuário
   como `Aluno` ou `Servidor`.
2. **Tratativa para vaga errada** — aviso quando um `Aluno` estaciona em uma
   `VagaDestinada` (reservada a servidores), já que bloqueio físico não é
   possível.
3. **Rastreamento do estacionamento** — mapa das vagas (`VagaComum`,
   `VagaEspecial`, `VagaDestinada`), mostrando quais estão livres/ocupadas.

## Estrutura orientada a objetos

- `Usuario` → `Aluno`, `Servidor`
- `Vaga` → `VagaComum`, `VagaEspecial` (acessibilidade/PCD/idoso), `VagaDestinada` (servidores)

## Como executar
```
python3 entry_point.py
```
