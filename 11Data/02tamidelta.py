# Podemos adicionar e subtrair datas
# O timedelta representa a diferença entre duas datas ou tempos
# Serve para realizar estimativas de datas futuras ou passadas
from datetime import datetime, timedelta
data_atual = datetime.now()
print("Data atual:", data_atual)

# Realizando sistema de entrega de limpeza de carros

tipo_carro = 'P' # P: Popular, M: Médio, G: Grande

tempo_pequeno = 30 # minutos
tempo_medio = 40  # minutos
tempo_grande = 50  # minutos

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print("Data estimada para carro popular:", data_estimada)
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print("Data estimada para carro médio:", data_estimada)
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print("Data estimada para carro grande:", data_estimada)

# explicando o uso do timedelta
# Possui os parâmetros days(Altera dias), seconds(Altera segundos), microseconds, milliseconds, minutes, hours(Altera horas) e weeks(Altera semanas)
# + incrementa a data
# - decrementa a data
# /* multiplica a diferença
# // divide a diferença

# É possivel pegar so data ou hora
data_exemplo = datetime(2024, 6, 15, 14,30, 0)
print("Data exemplo:", data_exemplo)
print("Data exemplo - só data:", data_exemplo.date())
print("Data exemplo - só hora:", data_exemplo.time())