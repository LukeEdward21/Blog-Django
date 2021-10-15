## como usar
Primeira vez usando docker
```bash
docker-compose up --build
```
próxima vez, não precisa do "--build"
```bash
docker-compose up
```

Se for usar diretamente na máquina, edite DATABASES em blog/settings.py e instale os requirements.txt
```bash
pip3 install -r requirements.txt
```

## aplique as migrations
no diretório raiz do projeto:
```bash
docker-compose exec web bash
python3 manage.py migrate
```
ou
```bash
docker-compose exec web ./manage.py migrate
```
se for usar sem o docker
```bash
python3 manage.py migrate
```

## Referências
Baseado nas aulas de [Fábio Ruicci](https://www.youtube.com/c/FabioRuicciCursos)
Templates do [Blog](https://getbootstrap.com/docs/4.0/examples/blog/)
Template para [login](https://getbootstrap.com/docs/4.0/examples/floating-labels/) e [registro](https://getbootstrap.com/docs/4.0/examples/floating-labels/)
