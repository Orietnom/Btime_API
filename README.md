# Btime API

Este projeto coleta dados meteorológicos das capitais brasileiras a partir da API do INMET e salva os resultados em um arquivo CSV.

## Pré-requisitos

- Python 3.12 ou superior
- [pip](https://pip.pypa.io)

## Instalação

1. Clone este repositório e acesse a pasta do projeto.
2. (Opcional) Crie e ative um ambiente virtual.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

O script utiliza variáveis de ambiente lidas a partir de um arquivo `.env` (opcional):

```env
URL=https://apitempo.inmet.gov.br/condicao/capitais/{0}
DAYS_BEFORE=0
```

- `URL` permite alterar o endpoint da API (padrão: INMET).
- `DAYS_BEFORE` define quantos dias antes da data atual serão usados na consulta.

Crie um arquivo `.env` na raiz do projeto com as variáveis desejadas.

## Execução

Execute o script principal:

```bash
python main.py
```

Um arquivo CSV será gerado na pasta `output` com o nome `inmet_<YYYYMMDD_HHMMSS>.csv`.

## Observações

- É necessário ter conexão com a internet para acessar a API do INMET.
- Os arquivos gerados são salvos na pasta `output` (criada automaticamente).
