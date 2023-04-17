# teste-fasters
Este repositório contém o código em python como resposta para o desafio de avaliação da fasters - netuno
Este é um script em Python que implementa uma lista de tópicos, onde o usuário pode realizar várias operações, tais como cadastrar um novo tópico, listar todos os tópicos, selecionar um tópico específico, excluir todos os tópicos, excluir um tópico específico ou selecionar tópicos em um intervalo.

O script começa importando as bibliotecas "os" e "platform". Em seguida, há uma lista de tópicos chamada "lista". A função "limpar_tela()" é definida para limpar a tela do console, dependendo do sistema operacional em que o script está sendo executado. Se o sistema operacional for Windows, a função usa o comando "os.system('cls')" para limpar a tela, caso contrário, usa o comando "os.system('clear')".

Em seguida, há um loop while infinito que imprime um menu com várias opções de operações que o usuário pode realizar na lista de tópicos. O usuário é solicitado a inserir o número da opção que deseja escolher. Dependendo da opção escolhida pelo usuário, o script executa uma das várias funções que permitem ao usuário realizar a operação desejada na lista de tópicos.

A primeira opção permite que o usuário cadastre um novo tópico. A função "append()" é usada para adicionar o novo tópico à lista.

A segunda opção permite que o usuário liste todos os tópicos existentes na lista. Se a lista estiver vazia, o script imprime uma mensagem informando que a lista está vazia. Caso contrário, o script imprime todos os tópicos na lista.

A terceira opção permite que o usuário selecione um tópico específico da lista, com base no índice. Se a lista estiver vazia, o script imprime uma mensagem informando que a lista está vazia. Caso contrário, o script solicita ao usuário que digite o índice do tópico que deseja selecionar. O script trata exceções que possam ocorrer e, em seguida, exibe o tópico selecionado.

A quarta opção permite que o usuário exclua todos os tópicos da lista. O script verifica se a lista está vazia e, em seguida, solicita ao usuário que confirme se deseja excluir todos os tópicos. Se o usuário confirmar a exclusão, a lista é limpa. Caso contrário, o script retorna ao menu principal.

A quinta opção permite que o usuário exclua um tópico específico da lista. O script trata exceções que possam ocorrer e, em seguida, solicita ao usuário que confirme se deseja excluir o tópico selecionado. Se o usuário confirmar a exclusão, o tópico é excluído da lista. Caso contrário, o script retorna ao menu principal.

A sexta opção permite que o usuário selecione tópicos em um intervalo especificado. O script trata exceções que possam ocorrer e, em seguida, exibe os tópicos selecionados.

A sétima opção permite que o usuário saia do script. O loop while infinito é interrompido e o script é finalizado.
