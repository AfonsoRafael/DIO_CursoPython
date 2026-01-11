# Trabalhando com fusos horários em Python
# Usamos o módulo datetime junto com o módulo pytz para manipular fusos horários
# O pytz fornece suporte completo para fusos horários, incluindo horário de verão
# O timezone permite converter datas entre diferentes fusos horários

# Necessário instalar o pytz se ainda não estiver instalado
# pip install pytz

import pytz
from datetime import datetime

# Obtendo a data e hora atual em UTC
utc = pytz.utc
data_utc = datetime.now(utc)
print("Data e hora em UTC:", data_utc)

# Convertendo para um fuso horário específico (exemplo: América/São_Paulo)
fuso_sao_paulo = pytz.timezone("America/Sao_Paulo") # timezone do pytz para São Paulo
data_sao_paulo = data_utc.astimezone(fuso_sao_paulo) # astimezone converte a data para o fuso horário desejado
print("Data e hora em Sao Paulo:", data_sao_paulo)
print("Fuso horário de São Paulo:", data_sao_paulo.tzinfo)# Mostra o fuso horário associado à data
print("Hora de sao paulo:", datetime.now(fuso_sao_paulo)) # Mostra a hora local em São Paulo