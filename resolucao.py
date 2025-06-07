# Dicionário para armazenar o nome da palestra como chave e a duração em minutos como valor
palestras = {}

# Abre o arquivo 'proposals.txt' para leitura
with open('proposals.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        # Remove espaços extras no começo/fim da linha
        linha = linha.strip()  

        # Divide a linha em palavras
        partes = linha.split()  

         # Última palavra é o tempo 
        tempo_str = partes[-1] 

        # O restante é o nome da palestra
        nome = ' '.join(partes[:-1])  

        # Verifica se é uma palestra "lightning" (5 minutos)
        if tempo_str.lower() == "lightning":
            duracao = 5
        else:
            # Remove o "min" para ficar só com o número e converte para inteiro
            duracao = int(tempo_str.replace("min", ""))

        # Adiciona o nome e duração no dicionário
        palestras[nome] = duracao


# Total de minutos disponíveis pela manhã 9 as 12
tempo_restante_manha = 180  
horas = 9  
minutos = 0  # Começa no minuto zero
manha = []  # Lista para guardar as palestras alocadas na manhã

# Transformamos o dicionário em uma lista de tuplas para iterar melhor
lista_palestras = list(palestras.items())  # [(nome, duracao), ...]

for nome, duracao in lista_palestras:
    # Verifica se a palestra cabe no tempo restante da manhã
    if duracao <= tempo_restante_manha:
        # Imprime o horário e o nome da palestra
        print(f"{horas:02d}:{minutos:02d} - {nome} ({duracao}min)")

        # Adiciona essa palestra na lista da manhã
        manha.append((nome, duracao))

        # Atualiza o tempo restante e o relógio
        tempo_restante_manha -= duracao
        minutos += duracao
        # Ajusta as horas se os minutos passarem de 59
        while minutos >= 60:
            minutos -= 60
            horas += 1

        # Remove a palestra do dicionário para não usar novamente
        palestras.pop(nome)

# Indica o horário do almoço após a manhã
print("12:00 - Almoço")

tempo_restante_tarde = 180  # Total de minutos disponíveis na tarde 13 as 17
horas = 13  
minutos = 0  # Começa no minuto zero
tarde = []  # Lista para guardar as palestras alocadas na tarde

# Atualiza a lista com as palestras que sobraram após a manhã
lista_palestras = list(palestras.items())

for nome, duracao in lista_palestras:
    # Verifica se a palestra cabe no tempo restante da tarde
    if duracao <= tempo_restante_tarde:
        # Imprime o horário e o nome da palestra
        print(f"{horas:02d}:{minutos:02d} - {nome} ({duracao}min)")

        # Adiciona essa palestra na lista da tarde
        tarde.append((nome, duracao))

        # Atualiza o tempo restante e o relógio
        tempo_restante_tarde -= duracao
        minutos += duracao
        # Ajusta as horas se os minutos passarem de 59
        while minutos >= 60:
            minutos -= 60
            horas += 1

        # Remove a palestra do dicionário para não usar novamente
        palestras.pop(nome)

# Indica o horário do evento de networking no fim da tarde
print("16:00 - Evento de Networking")
