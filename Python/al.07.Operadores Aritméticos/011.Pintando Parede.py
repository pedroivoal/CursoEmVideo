larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area =  larg*alt
lit_tint = area/2

print('Sua parede tem {} m².'.format(area))
print('Você precisa de {} listros de tinta.'.format(lit_tint))