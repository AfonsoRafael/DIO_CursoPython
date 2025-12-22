# Entrada do número de pacientes
def entrada():
    return int(input().strip())

# Lista para armazenar pacientes
def loop(n):
    pacientes = []

    for _ in range(n):
        nome, idade, status = input().strip().split(", ")
        idade = int(idade)
        pacientes.append((nome, idade, status))

    return pacientes

# Ordenar por prioridade: urgente > idosos > demais
def ordenando(pacientes):
    pacientes.sort(key=lambda x: (x[2] != "urgente", -x[1]))
    
    return [paciente[0] for paciente in pacientes]

def main():
    n = entrada()
    pacientes = loop(n)
    atendimento = ordenando(pacientes)

    print("Ordem de Atendimento: " + ", ".join(atendimento))

main()