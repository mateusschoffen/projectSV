
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

#### Class: Criteria
##### Função __init__():
*Recebe a string criterio, que é o nome do critério.
*Recebe uma lista de provedores e valores.

*Cria o atributo name, que é o nome string do critério inserido
*Cria o atributo values, que são os valores de cada provedor relacionado aquele critério.

#### Class: Recommendation
##### Função __init__():
*Recebe uma lista de objetos do tipo providers
*Cria um array de critérios - Futuramente será enviado pelo usuários
*Cria o atributo table_df e a variável table a partir da função create_main_dataframe()
*Cria o atributo crit_df a partir da função create_ponderation_vector()

##### Função create_main_dataframe()
*Recebe a lista de objetos do tipo provider

*A variável criteria recebe a função create_Criteria(), que é uma lista de objetos do tipo 'Classe Criteria' com todos os critérios encontrados na lista providers.

*A variável name_df é uma lista que recebe o atributo 'name' de cada item em providers

*Cria-se o dicionário table, para cada item na lista criteria, cria-se uma chave com o nome do item que recebe a lista de valores do item.

*A variável table_df é um dataframe que possui o valor 'data' associada aos valores da variável 'table', e 'index' associados a variável 'name_df'.

*A função retorna o dataframe 'table_df', e a lista 'table'

##### Função create_ponderation_vector()

*Recebe o valor 'table', que é um dicionário com nomes de critérios e os valores associados baseados em cada provedor.

*Recebe o valor 'crit_array', que é uma matriz de pesos relacionais de relevância entre cada critério.

*A variável crit_df é um dataframe que possui como valor 'data' a matriz 'crit_array', e os valores 'index' e 'columns' como as chaves descritas no dicionário 'table'.

*Cria-se uma variável auxiliar do tipo 'None' chamada vet.

*Para cada item nas chaves do dataframe 'crit_df', se a variável 'vet' não for do tipo 'None', soma-se a 'vet' a proporção de cada item de cada chave em relação a todos do mesmo tipo de chave. Caso a variável 'vet' seja do tipo None, 'vet' recebe a proporção de cada item de cada chave em relação a todos do mesmo tipo de chave.

*A variável 'vet_pon' recebe o o valor armazenado em 'vet' e o dívide pelo número de critérios existentes.

*O dataframe crit_df cria a coluna 'Vect' e associa os valores de 'vet_pon' a ele.

*Retorna o dataframe crit_df

##### Função create_Criteria()
*Recebe a lista de objetos do tipo providers

*ignored_valures recebe uma lista que descreve os valores estáticos que espera-se ignorar ao análisar os provedores.

*Cria-se um vetor 'aux' vazio.

*Usando o primeiro provedor encontrado na lista providers, para atributo desse provedor, se o atributo não estiver na lista 'ignored_values' cria-se um objeto do tipo 'Criteria' e o adiciona ao vetor 'aux'.

*Retorna a lista 'aux'.

##### Função calc_all
*A varíavel values tem os valores ordenados de 'min' ou 'max', que são o interesse no valor relacionado em cada critério.

*Cria-se a lista crit_array

*Para cada critério no dataframe table_df, adiciona o valor retornado pela função calc_criter() relacioado ao critério atual.

*Retorna o crit_array

##### Função calc_criter()
*Recebe o valor 'parity', que é uma string que determina o critério a ser calculado.
*Recebe o valor 'value' que determina se os valores relevantes do critério devem ser os de mínimo ou máximo.

*Recebe booleano opt que determina a ordenação de uma lista.

*A variável c1, recebe o valor retornado pela função parity_array_change()

*A variável c1_min recebe o valor retornado por optimizing_crit()

*A variável c1 recebe o valor retornado pela função scale_Saaty_values()

*A variável tc1 recebe o valor retornado pela função dataframe_transpose()

*A variável c1 recebe o resultado da função merged_dataframes()

*Retorna o valor de c1

##### Função parity_array_change()
*Recebe a string crterion, que é o criterio a ser utilizado.
*Recebe a variável dataframe, que é o dataframe que vai receber operações sobre.
*Recebe o booleano debug, que é uma alternativa para exibir o resultado.

*A variável new_df é um dataframe com todos os índices da variável 'dataframe', sem nenhum valor associado.

*Para cada índice (provedor) em new_df, se insere uma nova coluna em new_df. Essa coluna tem o nome do índice atual, na nova coluna segue a seguinte forma de associação: todos os provedores do dataframe em relação ao critério (criterion) declarado são subtraidos do valor atribuido ao índice atual levando em consideração o critério do mesmo, e depois divididos pelo valor atribuido ao índice atual levando em consideração o critério do mesmo. Multiplicando-se por 100. É uma proporção relativa de cada provedor em relação ao outro, em relação ao valor do mesmo.

*Se debug for true, exibe-se o resultado no terminal.

*Retorna new_df

##### Função optimizing_crit()

*Recebe a variável 'arr', que é um dataframe.

*Recebe o booleano descending, que determina se o valor retornado devem ser os maiores ou os menores.

*Recebe o booleano debug, que é uma alternativa para exibir o resultado.

*A variável num_providers recebe o tamanho contabilizado pelo número de colunas do dataframe 'table_df'.

*O dataframe 'arr', é transformado em um array único numpy.

*Se o valor de descending for True, 'arr' é ordenado de forma decrescente, caso False é ordenado de forma crescente.

*A variável 'arr' é reduzida a N elementos, sendo $N=(num_providers^2-num_providers)/2$.

*Se debug for true, exibe-se o resultado no terminal.

*Retorna 'arr'.

##### Função scale_Saaty_values()
*Recebe o valor 'dataframe' que vai ser utilizado a escala saaty

*Recebe o valor case_type, sendo 'min' ou 'max'.

*Recebe o booleano debug, que é uma alternativa para exibir o resultado.

*A variável 'matrix' recebe a variável dataframe em formato de matriz.

*case_type: max (Trata valores positivos); min (Trata valores negativos)

*Baseado em cada case_type, para cada valor dentro dentro de matrix, se o valor atual estiver dentro de uma lista de intervalos, obtem-se o índice que o valor está e altera-se o valor na matrix com o índice correspondente para corroborar com a tabela Saaty. Caso contrário o índice atual é transformado em NaN (Not and Number).

*A matriz 'matrix' é transformada em um dataframe na variável 'df', seguindo o mesmo escopo dos índices e colunas da variável 'dataframe'.

*Se debug for true, exibe-se o resultado no terminal.

*Retorna 'df'.

##### Função dataframe_transpose()

*Recebe a variável 'dataframe' que representa um dataframe

*Recebe o booleano debug, que é uma alternativa para exibir o resultado.

*A variável array, recebeu a variável 'dataframe' em forma de matriz.

*A matriz 'array', recebe a transpoosta de 'array'.

*Cada índice de 'array' é alterado para: $(i = i^-1)$

*Cria-se um dataframe 'new_df' com os mesmo índices e colunas de 'dataframe' e utilizando dados de 'array'.

*Se debug for true, exibe-se o resultado no terminal.

*Retorna 'new_df'.

##### Função vector_medium()

*Recebe a variável 'crit_list', que são as listas de critérios.

*Recebe o booleano debug, que é uma alternativa para exibir o resultado.

*Cria-se o array 'aux_array' vazio.

*Para cada critério em 'crit_list', a variável auxiliar 'var' é marcada como zero. Aninhado a isso,para cada um desses critérios, percorresse os provedores dele, var soma a si mesmo a proporção do peso daquele critério daquele provedor, em relação ao total de todos os critérios em relação ao critério. Por fim, adiciona ao vetor 'aux_array' o valor em 'var' dividido pelo número de critérios e continua até percorrer todos os critérios.

*Se debug for true, exibe-se o resultado no terminal.

*Retorna o 'aux_array'.

##### Função main_dataframe_criteries()

*Recebe a variável 'dataframe' no formato de um dataframe.

*Recebe uma lista de critérios na variável 'criteria_array'.

*Recebe o booleano debug, que é uma alternativa para exibir o resultado.

*Para cada critério em 'criteria_array', adiciona-se uma coluna 'criterion'+iteração, e os valores associados a ele em 'dataframe'.

*Se debug for true, exibe-se o resultado no terminal.

*Retorna o 'dataframe'.

##### Função define_provider()

*Recebe a variável dataframe, que é o dataframe principal.

*Recebe o dataframe 'criteria', que representa os pesos de cada critério.

*Recebe o booleano debug, que é uma alternativa para exibir o resultado.

*A variável 'only_criteria_from_df', recebe somente as colunas que tem o nome 'criterion'.

*A variável 'matrix_criteria' transforma a variável 'only_criteria_from_df' em uma matriz.

*A variável 'crit_weight' recebe em formato de matriz a colunar 'Vect' do dataframe 'criteria'.

*O 'dataframe' exclui todos os valores correspondentes em 'only_criteria_from_df'

*A variável 'result' recebe a multiplicação das matrizes 'matrix_criteria' e 'crit_weight'.

*A variável 'result' é arredondada em até 5 casas de precisão.

*Em 'dataframe' é criada uma nova coluna 'Selection', e adiciona os valores em result a mesma.

* 'dataframe' é ordenada em função da coluna 'Selection' de forma decrescente.

*Se debug for true, exibe-se o resultado no terminal.

*Retorna o 'dataframe' em formato de dicionário.