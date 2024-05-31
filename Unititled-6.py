
tarefa = {
    'nome': '',
    'descrição': '',
    'prioridade': '',
    'categoria': '',
    'concluída': False
}

# Função para adicionar uma nova tarefa
def adicionar_tarefa(lista_de_tarefas, nova_tarefa):
    lista_de_tarefas.append(nova_tarefa)

# Função para listar todas as tarefas
def listar_tarefas(lista_de_tarefas):
    for index, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f"Tarefa {index}: {tarefa['nome']} - {tarefa['descrição']}")

# Função para marcar uma tarefa como concluída
def marcar_como_concluída(lista_de_tarefas, index):
    lista_de_tarefas[index]['concluída'] = True

# Função para exibir tarefas por prioridade
def exibir_por_prioridade(lista_de_tarefas, prioridade):
    for tarefa in lista_de_tarefas:
        if tarefa['prioridade'] == prioridade:
            print(f"{tarefa['nome']} - {tarefa['descrição']}")

# Função para exibir tarefas por categoria
def exibir_por_categoria(lista_de_tarefas, categoria):
    for tarefa in lista_de_tarefas:
        if tarefa['categoria'] == categoria:
            print(f"{tarefa['nome']} - {tarefa['descrição']}")
            
def menu():
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Exibir tarefas por prioridade")
    print("5. Exibir tarefas por categoria")
    print("0. Sair")

# Exemplo de loop para o menu
def main():
    tarefas = []
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nova_tarefa = tarefa.copy()
            nova_tarefa['nome'] = input("Nome da tarefa: ")
            nova_tarefa['descrição'] = input("Descrição da tarefa: ")
            nova_tarefa['prioridade'] = input("Prioridade da tarefa: ")
            nova_tarefa['categoria'] = input("Categoria da tarefa: ")
            adicionar_tarefa(tarefas, nova_tarefa)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            index = int(input("Digite o índice da tarefa concluída: ")) - 1
            marcar_como_concluída(tarefas, index)
        elif opcao == "4":
            prioridade = input("Digite a prioridade desejada: ")
            exibir_por_prioridade(tarefas, prioridade)
        elif opcao == "5":
            categoria = input("Digite a categoria desejada: ")
            exibir_por_categoria(tarefas, categoria)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()     