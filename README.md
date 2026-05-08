# Python Ecommerce Simulator

Simulador transacional de ecommerce desenvolvido em Python para geração contínua de dados operacionais em banco relacional MySQL.

O projeto foi criado para simular um ambiente real de ecommerce, reproduzindo operações de negócio como criação de pedidos, pagamentos, movimentação de estoque e reabastecimento de produtos.

Os dados gerados são utilizados como origem operacional para pipelines de Data Engineering baseados em arquitetura Medallion e Lakehouse.

---

# Objetivo do Projeto

O principal objetivo do projeto é fornecer uma fonte de dados transacionais para estudos de:

- Engenharia de Dados
- Arquitetura Medallion
- Processamento distribuído
- Ingestão incremental
- Modelagem dimensional
- Data Lakes e Lakehouses
- Pipelines analíticos

O simulador reproduz cenários próximos de um ambiente OLTP real, permitindo alimentar pipelines analíticos com dados continuamente gerados.

---

# Funcionalidades

- Geração de clientes, produtos e pedidos
- Simulação de fluxo transacional de compras
- Atualização automática de estoque
- Reabastecimento de produtos
- Agendamento automatizado de eventos
- Persistência em banco relacional MySQL
- Geração contínua de dados para pipelines analíticos

---

# Modelo Relacional

Diagrama relacional utilizado para representar as operações transacionais do ecommerce.

![Modelo Relacional](docs/images/modelo_relacional.png)

O modelo relacional foi estruturado para representar entidades típicas de ecommerce:

- Clientes
- Produtos
- Pedidos
- Itens de Pedido
- Pagamentos
- Estoque

A granularidade transacional do modelo está centrada na entidade `itens_pedido`, representando o menor nível de detalhe operacional utilizado posteriormente na construção da tabela fato analítica.

---

# Arquitetura do Projeto

| Módulo | Responsabilidade |
|---|---|
| `data_generators.py` | Geração de entidades e dados simulados |
| `order_flow.py` | Fluxo transacional de pedidos |
| `restock.py` | Reabastecimento de estoque |
| `scheduler.py` | Agendamento e automação da simulação |
| `db.py` | Persistência e conexão com banco de dados |

---

# Fluxo Operacional

```text
Cliente → Pedido → Item Pedido → Pagamento → Atualização Estoque → Reabastecimento