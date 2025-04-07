# Etapa 1: Pré-processamento de Dados

Este repositório contém a implementação da **Etapa 1 do projeto de Grafos**, no qual o objetivo é realizar o **pré-processamento de dados** de problemas de logística representados por grafos.

---

## Objetivo da Etapa 1

- Modelar instâncias de problemas logísticos como grafos
- Ler dados de arquivos `.dat` fornecidos
- Calcular estatísticas básicas da estrutura do grafo
- Identificar elementos requeridos (vértices e arestas)

---

## Dados de Entrada

As instâncias estão contidas no arquivo:

202501_selected_instances.zip

Cada arquivo `.dat` possui informações como:

- Número de vértices, arestas e arcos
- Vértices e arestas requeridos para atendimento
- Capacidade dos veículos e depósito inicial
- Custos de viagem e demanda por aresta

---

## Funcoes do programa

O script em Python (`grafo_logistico.py`) executa os seguintes passos:

1. Extrai automaticamente os arquivos `.dat` de dentro do `.zip`
2. Lê a primeira instância encontrada
3. Monta uma **estrutura de grafo com lista de adjacência**
4. Calcula as estatísticas solicitadas:

### Estatísticas calculadas

- Quantidade de vértices
- Quantidade de arestas
- Vértices requeridos
- Arestas requeridas
- Densidade do grafo
- Componentes conexas
- Grau mínimo e máximo dos vértices

---
