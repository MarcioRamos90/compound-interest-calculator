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
git clone https://github.com/MarcioRamos90/compound-interest.git interest-compound-calculator
cd interest-compound-calculator
python -m venv .pack
source .pack/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configuracões para o heroku.
3. Defina um SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o servico de email.
6. Envie o código para o heroku.


```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o Email
git push heroku master --force
```