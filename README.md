# API Medicar 
> A API medicar é baseada em um sistema para gestão de consultas em uma clínica médica, na qual o administrador pode cadastrar médicos, agendas e especialidades, e o cliente pode marcar consultas para agenda e médico desejado.

## Diagrama de Classe
<p align="center">
  <img src="/gifs/diagrama-classe.png">
</p>
## Instalação
O processo de instalação apresentado a seguir é para máquinas com o sistema operacional Linux.   

### Configuração da Máquina

Passo 1:

Antes de iniciar a instalação do projeto, deve-se configurar a máquina com os pré-requisitos. Deve-se verificar se o Python3, pip e virtualenv estão instalados na máquina.

```sh
$ python3 –-version
```

```sh
$ python3 -m pip --version
```

```sh
$ virtualenv --version
```

Passo 2:

Caso algum não estiver instalado, deve ser instalado, através dos seguintes comandos:

```sh
$ sudo apt-get install python3.7
```

```sh
$ sudo apt-get install python3-pip
```

```sh
$ sudo pip install virtualenv
```
### Instalação do Projeto

Após a configuração da máquina, pode-se instalar o projeto.

Passo 1 - Download do projeto:

![](/gifs/download-projeto.gif)

Passo 2 - Criar virtualenv:

![](/gifs/criar-env.gif)

Passo 3 - instalar dependências:

![](/gifs/instalar-dependencias.gif)

Passo 4 - Executar migrate:

![](/gifs/exec-migrate.gif)

Passo 5 - Criar super usuário:

![](/gifs/exec-createsuperuser.gif)

Passo 6 - Executar aplicação:

![](/gifs/exec-runserver.gif)

Passo 7 - Acessar aplicação:

Para abrir a aplicação basta acessar http://127.0.0.1:8000/ no seu navegador.

## Documentação

Para consultar a documentação da aplicação basta acessar a página https://medicar-app.herokuapp.com/docs/ no seu navegador.

## Meta

Jacques Nier – [@Facebook](https://facebook.com/jacques.nier) – jacquesnier@gmail.com

## Tecnologias

- <img src="https://camo.githubusercontent.com/e34e1fd8b88a76ad738eff256a773aa6c69b412c/68747470733a2f2f7777772e646a616e676f70726f6a6563742e636f6d2f732f696d672f6c6f676f732f646a616e676f2d6c6f676f2d6e656761746976652e706e67" width="90">
- <img src="https://www.django-rest-framework.org/img/logo.png" width="90">
- <img src="https://www.python.org/static/community_logos/python-logo.png" width="90">
