def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))
    confirmadas = []
    recusadas = []

    # TODO: Crie o processamento das reservas:
    for i in range(0 , len(reservas_solicitadas)):
      if reservas_solicitadas[i] in quartos_disponiveis:
        confirmadas.append(reservas_solicitadas[i])
      else:
        recusadas.append(reservas_solicitadas[i])

    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos: 
    

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()