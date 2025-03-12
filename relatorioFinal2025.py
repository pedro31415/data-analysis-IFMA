import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Dados de exemplo
df = pd.read_csv('relatorio.csv')

# Obter lista de perguntas únicas
perguntas = df['Indicador'].unique().tolist()

# Definir cores, e garantimos que o número de cores seja suficiente
colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

# Loop para criar gráficos para cada pergunta
for pergunta in perguntas:
    df_pergunta = df[df['Indicador'] == pergunta]
    respostas_por_segmento = df_pergunta.groupby(['Segmento', 'Resposta']).size().unstack(fill_value=0)
    percentual_respostas = respostas_por_segmento.div(respostas_por_segmento.sum(axis=1), axis=0) * 100

    # Configura o gráfico 3D
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Posições no eixo Y (segmentos)
    y_pos = np.arange(len(percentual_respostas))

    # Barra Y começa em 0, depois vamos empilhar as barras
    y_pos_stack = np.zeros(len(percentual_respostas))

    # Largura das barras
    width = 0.8

    # Garantir que o número de cores seja suficiente
    for i, resposta in enumerate(percentual_respostas.columns):
        # Ajustar a cor para garantir que não ultrapasse o número de cores
        color = colors[i % len(colors)]  # Repete as cores caso haja mais respostas que cores

        # Plotando as barras 3D
        ax.bar3d(np.zeros(len(percentual_respostas)), y_pos, y_pos_stack, width, np.ones(len(percentual_respostas)), percentual_respostas[resposta],
                 color=color, alpha=0.8, label=resposta)

        # Atualizar a posição Y para a próxima barra (empilhamento)
        y_pos_stack += percentual_respostas[resposta].values  # Empilha as barras ao longo do eixo Y

    # Adiciona rótulos e título
    ax.set_xlabel('Respostas')
    ax.set_ylabel('Segmento')
    ax.set_zlabel('Porcentagem')
    ax.set_title(f'Gráfico 3D - {pergunta}')
    ax.legend()

    # Exibe o gráfico
    plt.show()

    # Fechar a figura para liberar memória
    plt.close(fig)

