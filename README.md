# ETL de Produtos (CSV)

Projeto 1 do meu percurso de estudo autodidata em Engenharia de Dados.

Script simples que lê um arquivo CSV de produtos, valida os dados e gera um novo CSV apenas com os registros válidos.

## O que ele faz

1. **Extract** — lê `produtos.csv` usando `csv.DictReader`.
2. **Transform** — valida cada produto (o preço precisa existir, ser numérico e maior que zero) e mantém apenas as colunas `nome`, `preco` e `quantidade`.
3. **Load** — grava os produtos válidos em `produtos_validados.csv`.

Ao final, o script imprime um resumo:

```
8 produtos lidos, 4 válidos, 4 descartados
```

## Como rodar

```bash
python etl_produtos.py
```

Certifique-se de que o arquivo `produtos.csv` esteja na mesma pasta do script.

## Exemplo

**Entrada (`produtos.csv`)**

| nome | preco | quantidade |
|---|---|---|
| Teclado Mecânico | 199.90 | 15 |
| Monitor 24 polegadas | -50.00 | 5 |
| Cadeira Escritório | *(vazio)* | 8 |
| Headset Bluetooth | grátis | 12 |

**Saída (`produtos_validados.csv`)**

| nome | preco | quantidade |
|---|---|---|
| Teclado Mecânico | 199.90 | 15 |
| Mouse Gamer | 89.50 | 30 |
| Webcam Full HD | 149.00 | 20 |
| Mousepad | 25.00 | 50 |

Registros com preço negativo, vazio ou não numérico são descartados automaticamente pela função `validar_produto`.

## Próximos passos

Este é o primeiro de uma série de projetos de ETL. Os próximos vão evoluir para:
- Carregar os dados validados em um banco SQLite
- Consolidar múltiplas fontes de dados
- Adicionar logging e tratamento de erros mais robusto
- Subir os dados para AWS S3
- Orquestrar o pipeline com Airflow
