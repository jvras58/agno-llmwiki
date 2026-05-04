---
tags:
  - sdd
  - engenharia
  - pydantic
---
# Spec-Driven Development (SDD)

> [!quote] Definição
> O Spec-Driven Development é uma abordagem onde a implementação de software é estritamente guiada por especificações e contratos bem definidos antes de a primeira linha de código lógico ser escrita.

## Princípios no Contexto de Agentes
Ao construir sistemas multi-agentes, o SDD nos ajuda a:
1. **Limitar Alucinações:** O agente sabe exatamente o contrato de dados que deve retornar (ex: schemas validados com Pydantic).
2. **Desacoplamento:** Serviços de processamento (como o nosso worker do [[Projeto Nexus]]) são isolados das regras de resposta do LLM.