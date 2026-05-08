# Python Ecommerce Simulator

Simulador transacional de ecommerce desenvolvido em Python para geração contínua de dados operacionais em banco relacional MySQL.

O projeto foi criado para reproduzir operações típicas de um ambiente de ecommerce, simulando fluxo de pedidos, pagamentos, movimentação de estoque e processos de reabastecimento.

Os dados gerados são utilizados como origem operacional para pipelines de Data Engineering baseados em arquitetura Medallion e Lakehouse.

---

# Objetivo do Projeto

O principal objetivo do projeto é fornecer uma fonte de dados transacionais para estudos e implementação de:

- Engenharia de Dados
- Arquitetura Medallion
- Arquitetura Lakehouse
- Processamento distribuído
- Ingestão incremental
- Modelagem dimensional
- Data Lakes
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
- Geração contínua de dados operacionais para pipelines analíticos

---

# Modelo Relacional

Diagrama relacional utilizado para representar as operações transacionais do ecommerce.

![Modelo Relacional](docs/images/modelo_relacional.png)

O modelo relacional foi estruturado com entidades típicas de ecommerce:

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
```

---

# Integração com Data Engineering

Os dados gerados pelo simulador são utilizados como origem operacional para pipelines analíticos desenvolvidos com:

- Apache Spark
- Apache Airflow
- Delta Lake
- HDFS

Os pipelines seguem arquitetura Medallion:

```text
Landing → Raw → Trusted → Refined
```

---

# Fluxo Arquitetural

```text
Python Simulator
       ↓
MySQL (OLTP)
       ↓
Landing
       ↓
Spark Pipeline
       ↓
Delta Lake / Medallion
```

---

# Tecnologias Utilizadas

- Python
- MySQL
- SQL
- Faker
- Modelagem Relacional

---

# Estrutura do Projeto

```text
.
├── docs
│   └── images
│       └── modelo_relacional.png
├── src
│   ├── data_generators.py
│   ├── db.py
│   ├── order_flow.py
│   ├── restock.py
│   └── scheduler.py
├── run.py
├── .gitignore
└── README.md
```

---

# Próximas Evoluções

- Integração com streaming de eventos
- Simulação em tempo real
- APIs REST
- Observabilidade e métricas operacionais
- Integração com Apache Kafka
- Geração distribuída de eventos