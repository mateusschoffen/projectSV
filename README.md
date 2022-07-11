
:construction: Projeto em construção :construction:

## Instruções

Este repositório é um template de um projeto Python minimo  
O programa se chama `fornecedorlog` e está organizado com pastas 
e módulos, porém a maioria dos arquivos encontra-se vazio.

## Requisitos

Este template utiliza o gerenciador de pacotes **poetry**

### Se estiver rodando no Linux no seu ambiente local

`execute o comando abaixo para instalar o Poetry no Linux`
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

`Em outros ambientes pode instalar com `
```bash
pip install --user poetry
```

>  No replit.com o poetry já está disponível e no gitpod será instalado assim que o ambiente iniciar.

## Instalando o ambiente

```bash
poetry install
poetry shell
```


Executando
```bash
fornecedorlog
# ou
python -m fornecedorlog
```

Se apareceu `Hello from fornecedorlog` então está tudo certo.


## Executando o projeto através do Docker
Dentre as possibilidades de executar o projeto, existe a alternativa de executar ele em containers que já estão desenvolvidos no projeto, estamos utilizando no caso o Docker para isso.

Container Docker é o componente do software de código aberto que automatiza a implementação de aplicativos em Containers LINUX, o famoso Docker. Esse modelo funciona ao contrário da virtualização de hipervisor, em que uma ou mais máquinas independentes executam virtualmente o hardware físico por meio de uma camada de intermediação.

## Instalando Docker no Ubuntu

A documentação oficial encontra-se nesse link [Docker Engine on ubuntu](https://docs.docker.com/engine/install/ubuntu/), mas o passo a passo geral está descrito abaixo.

Desde que os requisitos de versão linux estejam sendo respeitados, basta executar os comandos a seguir no terminal.

Abra o terminal (Ctrl+Alt+T) e faça o update do `apt` e depois faça a instalação da última versão do Docker Engine, containerd e Docker Compose:

```bash
sudo apt-get update
```

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

## Verificando se o Docker Engine está instalando corretamente

Novamente com o terminal aberto (Ctrl+Atl+T) execute o comando abaixo para rodar o hello-world versão docker.

```bash
sudo docker run hello-world
```

Uma mensagem de que o container não foi encontrado localmente deve aparecer, e após baixar o container da plataforma o código deve ser executado e uma mensagem "Hello from Docker!" deve aparecer, seguido de outras informações e dicas interessantes.

## Buildando o projeto com Docker
Com um clone do repositório na sua máquina, acesse a pasta do projeto e abra um terminal dentro dela, desta forma o terminal já vai estar realizando operações dentro da própria pasta `ou` abra um terminal e navegue até a pasta do projeto por qualquer terminal aberto.

Depois execute o seguinte comando:

```bash
docker build --target development -t project/dev --file docker/Dockerfile .
```

## Executando o projeto com Docker
Com o container criado, basta executar ele atráves de qualquer terminal aberto através do seguinte comando que vai reservar o endereço a `porta 8000`.

```bash
docker run -p 8000:8000 project/dev
```

# recommend.py
Consta toda descrição do que está sendo executada no programa recommend.py, que trata como base o modelo AHP (Analytic Hierarchy Process) e utiliza a escala de Saaty como parâmetros de conversão.

## Classes
Listagem das classes utilizadas no arquivo de código, sendo elas:

### Class: Recommendation
Funções

