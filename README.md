# Apresentação
Durante a disciplina de Estruturas de Dados fiz a implementação de duas estruturas como trabalho final: Árvores Binárias e Tabela Hash. Depois de realizar modificações e correções, disponibilizo o projeto finalizado. Além dessas implementações, inclui outras estruturas que desenvolvi para estudos e projetos relacionados.

## Sobre a realização dos projetos 
Programar cada uma dessas estruturas é um processo desafiador. Algumas são mais simples, enquanto outras demandam um nível maior de complexidade. Entretanto, em cada uma delas é interessante poder observar melhor o real processo de funcionamento que se esconde por tras de tantas funções e propriedades que tanto usamos ao trabalhar com linguagens de programação.

Obs.: Vale resaltar que as implementações de Arvore Binárias e Tabela Hash foram pensadas para alocação de dados do tipo string, assim para alocação de outros tipos de dados as funcionalidades implementadas podem não ocorrer com o esperado. Ademais, ambas estruturas tem implementadas uma propriedade em cada nó de armazenadamento que representa o número de consultas que foram feitas sobre aquele dado armazenado naquele nó em especifico. 

## Estruturas Implementadas

### Árvores Binárias
Descrição: Estruturas de dados onde cada nó pode ter no máximo dois filhos, facilitando operações como busca, inserção e remoção.
Métodos disponíveis: inserirPalavra, consultarPalavra, palavrasMaisConsultadas, removerPalavra e outras.
Complexidade de tempo: As operações de busca, inserção e remoção podem ser realizadas em tempo O(log n) em média, em uma árvore balanceada.
Casos de uso: Ideal para representação hierárquica de dados, como em sistemas de arquivos.

### Tabela Hash
Descrição: Estruturas que permitem o armazenamento e a recuperação eficiente de dados, utilizando uma função hash.
Métodos disponíveis: inserir, consultas, maisConsultada, imprimirTabela e outras.
Complexidade de tempo: A operação de busca é, em média, O(1) com uma boa função hash.
Casos de uso: Usada em bancos de dados, caches e sistemas que requerem acesso rápido a dados.

### Lista Estática
Descrição: Estruturas de dados que utilizam um array de tamanho fixo.
Métodos: inserção, remoção e consulta.
Vantagens: Acesso direto por índice rápido, mas tamanho fixo limita a flexibilidade.

### Lista Simplesmente Encadeada
Descrição: Estrutura onde cada elemento aponta para o próximo, permitindo um funcionamento dinâmico.
Métodos: inserção, remoção e consulta.
Vantagens: Tamanho dinâmico, fácil inserção e remoção.

### Lista Duplamente Encadeada
Descrição: Estrutura semelhante à lista simplesmente encadeada, mas com ponteiros para o próximo e o anterior.
Métodos: inserção, remoção e consulta.
Vantagens: Navegação fácil em ambas as direções.

## Conclusão
Neste repositório, não apenas compartilho as implementações das estruturas de dados, mas também minhas reflexões sobre o aprendizado durante todo o processo de desenvolvimento. Cada estrutura retrata não só conhecimento técnico, mas também a evolução na forma de resolver problemas.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para me enviar pull requests ou abrir issues para aperfeiçoar as implementações.