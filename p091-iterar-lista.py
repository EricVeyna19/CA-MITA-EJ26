# p091-iterar-lista.py
# Iterar por los elementos de una lista

print('\033[H\033[J')
print('Iterar por los elementos de una lista:\n')

nums = [2, 4, 6, 8, 10, 12, 14, 16]
print(f'Numeros a procesar: {nums}\n')

print('1. Iteracion por elemento:')
for n in nums:
    print(n, end=' ')

print('\n\n2. Iteracion por indice:')
for i in range(len(nums)):
    print(nums[i], end=' ')

print('\n\n3. Iteracion por elemento para sumar 2:')
for n in nums:
    print(n + 2, end=' ')

print('\n\n4. Iteracion por indice para sumar 10:')
for i in range(len(nums)):
    nums[i] += 10
    print(nums[i], end=' ')

print('\n\n5. Iteracion con enumerate:')
print('Pos\tValor')
for i, n in enumerate(nums):
    print(i, '\t', n)
print()