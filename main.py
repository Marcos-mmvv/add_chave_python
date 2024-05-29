# Adicionar Campo ou valor ao novo campo

pessoa = {
    'Nome: ': input('Digite o seu nome: '),
    'Idade: ': int(input('Informe a sua idade: ')),
    'Profissão: ': input('Informe a sua profissão: ')
}

nova_chave = input('Digite o nome do campo adicional: ') 
novo_valor = input('Informe o valor do novo campo: ')
pessoa[nova_chave] = novo_valor

for cad in pessoa:
    print(f'{cad}: {pessoa.get(cad)}')