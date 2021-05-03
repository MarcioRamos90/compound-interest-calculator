# Juros Compostos

Sistema de calculo de juros compostos.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.9
3. Ative seu virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes

```console
git clone https://github.com/MarcioRamos90/compound-interest-calculator.git compound-interest-calculator
cd compound-interest-calculator
python -m venv .pack
source .pack/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```