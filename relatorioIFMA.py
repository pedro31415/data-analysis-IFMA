import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt

df = pd.read_csv('relatorio2.csv')
print(df.describe())

# Obter lista de perguntas únicas
perguntas = df['Indicador'].unique().tolist()
print(perguntas)
x = 1

# Loop para criar um gráfico por vez para cada pergunta
for pergunta in perguntas:

    # Filtrar as respostas para a pergunta atual
    df_pergunta = df[df['Indicador'] == pergunta]

    # Calcula a contagem das respostas por segmento 
    respostas_por_segmento = df_pergunta.groupby(['Segmento', 'Resposta']).size().unstack(fill_value=0)

    # Calcula as porcentagens
    percentual_respostas = respostas_por_segmento.div(respostas_por_segmento.sum(axis=1), axis=0) * 100

    # Cria o gráfico empilhado
    # ax = percentual_respostas.plot(kind='barh', stacked=True, figsize=(10,7), color=['#1b9e77', '#d95f02', '#7570b3', '#e7298a'])
    ax = percentual_respostas.plot(
    kind='barh', 
    stacked=True, 
    figsize=(12,8), 
    color=['#1b9e77', '#d95f02', '#7570b3', '#e7298a'],
    alpha=0.8,      # Transparência das barras
    title="Distribuição das Respostas por Segmento",
    xlabel="Porcentagem (%)",
    ylabel="Segmentos",
    grid=True,      # Adiciona linhas de grade
    legend=True,    # Exibe a legenda
    edgecolor='black',  # Adiciona contorno às barras
    linewidth=1.5   # Espessura do contorno das barras
    )

    #Adicona as porcentagens dentro das barras
    for i in ax.containers:
        ax.bar_label(i, label_type='center', fmt='%.1f%%')
    
    # Configurar a fonte dos rótulos e o titulo
    font = {'family': 'serif','fontweight': 'bold', 'color': 'darkblue', 'weight': 'bold', 'size': 14}
    
    # Obter eixo atual
    ax = plt.gca()
    # ax.set_yticklabels(ax.get_yticklabels(), fontsize=12, va='center', ha='right', rotation=0,labelpad=10) 
    ax.tick_params(axis='y', pad=15)
    # Ajusta os rotulos e o titulo 
    plt.xlabel('Porcentagem')
    plt.ylabel('Segmento', labelpad=10)
    plt.title(f'{pergunta}')
    plt.legend(title='Resposta', bbox_to_anchor=(1.05,1), loc='upper left')
    plt.show()
   
print(x)