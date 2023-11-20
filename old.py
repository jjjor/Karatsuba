import time
import sys

def karatsuba(x, y):
    
        return x * y
    
start_time = time.time()
end_time = time.time()

elapsed_time = (end_time - start_time) * 1000  # Convertendo para milissegundos
    
resultado = karatsuba(1234567892123456789212345678921234567892123456789212345678921234567892123456789212345678921234567892, 1234567892123456789212345678921234567892123456789212345678921234567892123456789212345678921234567892)
print(f'Resultado: {resultado}')
print(f'Tempo de execução: {elapsed_time:.5f} milissegundos')