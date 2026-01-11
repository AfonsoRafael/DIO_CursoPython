# Conversão e formatação de datas em Python
# Para formatar datas, usamos o método strftime e para converter strings em datas usamos o strptime
from datetime import datetime
data_atual = datetime.now()
print("Data atual:", data_atual)
# Formatando a data para o formato dia/mês/ano hora:minuto:segundo
# É possivel criar uma mascara personalizada
mascara_ptbr = "%d/%m/%Y %H:%M:%S"
data_str = "2025/11/25 15:45:30"
mascara_en = "%Y/%m/%d %H:%M:%S" # mascara para converter a string acima, precisa ser igual ao formato da string
print(f"Data formatada: ",data_atual.strftime(mascara_ptbr))

# Convertendo string para data usando a mesma máscara
print("data em string:", data_str)
print("Convertendo string para data:", datetime.strptime(data_str, mascara_en))



# resumo dos principais códigos de formatação:
# %d - Dia do mês com dois dígitos (01 a 31)
# %m - Mês com dois dígitos (01 a 12)
# %Y - Ano com quatro dígitos (ex: 2024)
# %H - Hora em formato 24 horas (00 a 23)
# %M - Minutos com dois dígitos (00 a 59)
# %S - Segundos com dois dígitos (00 a 59)
# %a - Abreviação do dia da semana (ex: Mon, Tue)
# %A - Nome completo do dia da semana (ex: Monday, Tuesday)
# %b - Abreviação do mês (ex: Jan, Feb)
# %B - Nome completo do mês (ex: January, February)
