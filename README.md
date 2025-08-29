# Btime API

Este projeto coleta dados meteorológicos das capitais brasileiras a partir da API do INMET e salva os resultados em um arquivo CSV.

## Pré-requisitos

- Python 3.12 ou superior
- [pip](https://pip.pypa.io)

## Instalação

1. Clone o repositório e entre na pasta do projeto:
   ```bash
   git clone <url-do-repositorio>
   cd Btime_API
   ```
2. Crie e ative um ambiente virtual (opcional, porém recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux ou macOS
   .venv\Scripts\activate     # Windows
   ```
3. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```
4. Instale os navegadores necessários do Playwright:
   ```bash
   playwright install
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

Um arquivo CSV será gerado na pasta `output` com o nome `inmet_<YYYYMMDD_HHMMSS>.csv` e os logs serão armazenados em 
`logs/`.

## Observações

- É necessário ter conexão com a internet para acessar a API do INMET.
- Os arquivos gerados são salvos na pasta `output` (criada automaticamente).
