import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

df = pd.read_csv('relatorio2.csv')
print(df.describe())

# Obter lista de perguntas únicas
perguntas = df['Indicador'].unique().tolist()
print(perguntas)

# Loop para criar um gráfico por vez para cada pergunta
for pergunta in perguntas:
    # Filtrar as respostas para a pergunta atual
    df_pergunta = df[df['Indicador'] == pergunta]

    # Calcula a contagem das respostas por segmento
    respostas_por_segmento = df_pergunta.groupby(['Segmento', 'Resposta']).size().unstack(fill_value=0)

    # Calcula as porcentagens
    percentual_respostas = respostas_por_segmento.div(respostas_por_segmento.sum(axis=1), axis=0) * 100

    # Criar a figura para o gráfico 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Definir as posições no eixo Y
    y_pos = np.arange(len(percentual_respostas))

    # Definir as cores para cada resposta
    colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a']

    # Inicializar as variáveis para as barras
    x_pos = np.zeros(len(percentual_respostas))  # Começar todas as barras na posição zero
    width = 0.5  # Largura da barra

    # Plotar as barras 3D
    for i, resposta in enumerate(percentual_respostas.columns):
        # Para cada resposta, empilhar as barras na direção do eixo Z
        ax.bar3d(x_pos, y_pos, np.zeros(len(percentual_respostas)), width, np.ones(len(percentual_respostas)), percentual_respostas[resposta],
                 color=colors[i], alpha=0.8, label=resposta)

        # Atualizar a posição X para a próxima barra
        x_pos += percentual_respostas[resposta].values

    # Ajustar a aparência do gráfico
    ax.set_xlabel('Porcentagem')
    ax.set_ylabel('Segmento')
    ax.set_zlabel('Respostas')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(percentual_respostas.index)

    # Adicionar as porcentagens dentro das barras
    for i, resposta in enumerate(percentual_respostas.columns):
        for j in range(len(percentual_respostas)):
            ax.text(x_pos[j] - percentual_respostas[resposta].iloc[j] / 2, y_pos[j], percentual_respostas[resposta].iloc[j] / 2,
                    f'{percentual_respostas[resposta].iloc[j]:.1f}%', ha='center', va='center', color='white', fontweight='bold')

    # Configurar o título e legendas
    plt.title(f'{pergunta}')
    ax.legend(title='Resposta', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.show()
