sexo = str(input('informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('sexo Invalido, Informe seu sexo: [M/F]')).upper()
if sexo == 'M':
    print('Obrigado Masculino selecionado')
elif sexo == 'F':
    print('Obrigado sexo Feminino selecionado')

