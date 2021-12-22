var = input('Digite algo: ')
#var = int(var)

print('Tipo da variável: ', type(var))

print('É somente composta por espaços', var.isspace())
print('É somente numérico(inclui string)',  var.isnumeric())
print('É somente alfabético',  var.isalpha())
print('É somente alfanumérico', var.isalnum())
#print('É somente numérico(não string)',  var.isalnum())
print('É somente maiusculo',  var.isupper())