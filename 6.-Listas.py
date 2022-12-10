# Declarar lista
mi_lista=['Javier','Manuel','Braulio','Emmanuel']
# Imprimir toda la lista
print(mi_lista[:])
# Imprimir una posicion de la lista
print(mi_lista[2])
# Imprimir ciertas posiciones de las listas
print(mi_lista[1:3])

# agregar un elemento nuevo a la lista
mi_lista.append('Virkov')
print(mi_lista[:])

# agregar a una posicion 
mi_lista.insert(2,'Adbiel')
print(mi_lista[:])

# agregar varios elementos a la lista
mi_lista.extend(['Jeremy','Alex','Pedro'])
print(mi_lista[:])

# buscar un elemento de la lista
print(mi_lista.index('Alex'))

# remover un elemento de la lis
mi_lista.remove('Adbiel')
print(mi_lista)

# remover el ultimo elemento de la lista
mi_lista.pop()
print(mi_lista)

# Imprimir cuantos objetos hay lista
n = len(mi_lista)
print(n)