def escolhe_categoria(idade):
    
    if idade < 10:
        categoria = 'MIRIM'
    elif idade < 15:
        categoria = 'INFANTIL'
    elif idade < 20:
        categoria = 'JÚNIOR'
    elif idade < 21:
        categoria = 'SÉNIOR'
    else:
        categoria = 'MASTER'
    
    return categoria
    


idade = int(input('Digite sua idade: '))

print(escolhe_categoria(idade))