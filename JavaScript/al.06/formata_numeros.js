n1 = 1545.5
n1.toFixed(2)
n1.toFixed(2).replace('.', ',')
n1.toLocalString('pt-br', {style: 'currency', currency: 'BRL'})
n1.toLocalString('pt-br', {style: 'currency', currency: 'USD'})
h = n1.toLocalString('pt-br', {style: 'currency', currency: 'EUR'})
console.log(h)