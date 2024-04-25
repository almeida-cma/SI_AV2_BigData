import pandas as pd
import random
from datetime import datetime, timedelta

# Função para gerar uma data aleatória em janeiro de 2024
def random_date():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 1, 31)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Função para gerar uma hora aleatória
def random_time():
    return "{:02d}:{:02d}:{:02d}".format(random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))

# Gerar base de dados com 1000 registros
data = {
    'usuario': [random.randint(1, 20) for _ in range(1000)],
    'tipo': [random.choice(['imagem', 'video', 'texto']) for _ in range(1000)],
    'assunto': [random.choice(['esportes', 'moda', 'finanças', 'educação', 'saúde']) for _ in range(1000)],
    'data': [random_date().strftime('%Y-%m-%d') for _ in range(1000)],
    'hora': [random_time() for _ in range(1000)],
    'interacoes': [random.randint(1, 50) for _ in range(1000)]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Salvar DataFrame como CSV
df.to_csv('postagens.csv', index=False)

# Mostrar tipo com maior interação
tipo_maior_interacao = df.groupby('tipo')['interacoes'].sum().idxmax()
print("Tipo com maior interação:", tipo_maior_interacao)

# Mostrar assunto com maior interação
assunto_maior_interacao = df.groupby('assunto')['interacoes'].sum().idxmax()
print("Assunto com maior interação:", assunto_maior_interacao)

# Converter hora para formato datetime
df['hora'] = pd.to_datetime(df['hora'], format='%H:%M:%S')

# Calcular faixa de horário com maior interações (em intervalos de 1 hora)
df['hora_intervalo'] = df['hora'].dt.floor('H')
faixa_horario_maior_interacao = df.groupby('hora_intervalo')['interacoes'].sum().idxmax()
print("Faixa de horário com maior interações:", faixa_horario_maior_interacao.time(), "-", (faixa_horario_maior_interacao + timedelta(hours=1)).time())

# Calcular 3 dias do mês com maior interação
top_3_dias = df.groupby('data')['interacoes'].sum().nlargest(3)
print("3 dias do mês com maior interação:")
for date, interactions in top_3_dias.items():
    print(date, "- Interactions:", interactions)
