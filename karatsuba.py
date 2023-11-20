import sys
import time
import csv

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    x_high, x_low = divmod(x, 10 ** m)
    y_high, y_low = divmod(y, 10 ** m)

    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)

    return z2 * 10 ** (2 * m) + (z1 - z2 - z0 * 10) ** m + z0

def salvar_resultados(nome_teste, x, y, elapsed_time, resultado):
    with open('resultados.txt', 'a') as file:
        file.write(f'Nome do Teste: {nome_teste}\n')
        file.write(f'Total de Digitos (x): {len(str(x))}\n')
        file.write(f'Total de Digitos (y): {len(str(y))}\n')
        file.write(f'Tempo de Execucao: {elapsed_time:.5f} milissegundos\n')
        file.write(f'Resultado: {resultado}\n\n')

# Aumentando o limite de recursão
sys.set_int_max_str_digits(100000000000000000)

# Testando o algoritmo com cronômetro
x = 1234567892123456789212345678921234567892123456789212345678921234567892123456789212345678921234567892
y = 1234567892123456789212345678921234567892123456789212345678921234567892123456789212345678921234567892

start_time = time.time()
resultado = karatsuba(x, y)
end_time = time.time()

elapsed_time = (end_time - start_time) * 1000  # Convertendo para milissegundos
print(f'Resultado: {resultado}')
print(f'Tempo de execução: {elapsed_time:.5f} milissegundos')

# Salvando os resultados em um arquivo
nome_teste = 'solved_by_karatsuba'
salvar_resultados(nome_teste, x, y, elapsed_time, resultado)
