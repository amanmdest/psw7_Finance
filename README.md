<h1 align='center'>FINAN.CE</h1>
<p align='center'>Plataforma de gestão, planejamento e registros financeiros, desenvolvida durante a sétima edição do evento PyStack Week, conduzido pelo professor Caio Sampaio.</p>

<div align='center'>
  <img alt="Django" src="https://img.shields.io/badge/Django-092E20.svg?&logo=django&logoColor=green">
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-07405E?style=flat&compact=true&logo=sqlite&logoColor=white">
  <img alt="Creative Commons License" src="https://img.shields.io/badge/License-Creative%20Commons-red">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/amanmdest/psw3_Freelaway?color=purple">
</div>

## Interface da Aplicação
<kbd>
  <img src="media/home.png" alt="home" width="280"/>
</kbd>
<kbd>
  <img src="media/gerenciar.png" alt="gerenciar" width="280"/>
</kbd>  
</kbd>
<kbd>
  <img src="media/novo_valor.png" alt="novo_valor" width="280"/>
</kbd>  
<kbd>
  <img src="media/definir_contas.png" alt="definir_contas" width="280"/>  
</kbd>
<kbd>  
  <img src="media/ver_contas.png" alt="ver_contas" width="280"/>  
</kbd>
<kbd>
  <img src="media/definir_planejamento.png" alt="definir_planejamento" width="280"/>  
</kbd>  
<kbd>
  <img src="media/ver_planejamento.png" alt="ver_planejamento" width="280"/>  
</kbd>
<kbd>
  <img src="media/dashboard.png" alt="dashboard" width="280"/>  
</kbd>
<kbd>
  <img src="media/admin.png" alt="admin" width="280"/>  
</kbd>  

## Rode localmente
1. Clone o repositório:
```
  git clone https://github.com/amanmdest/psw7_Finance.git
```
2. Crie e ative um *virtualenv*(Linux):
```
  python -m venv venv
  source venv/bin/activate
```
3. Instale as dependências:
```
  pip install -r requirements.txt
```
4. Migrações Banco de Dados:
```
  python manage.py makemigrations
  python manage.py migrate
```
5. Para poder usar o painel do admin é preciso criar um superuser:
```
  python manage.py createsuperuser
```
6. Rode o projeto localmente:
```
  python manage.py runserver
```
e acesse: http://127.0.0.1:8000/
