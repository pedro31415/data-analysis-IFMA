import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt

df = pd.read_csv('relatorio2.csv')
print(df.describe())

#Indicador,Subsídio p/ Avaliações,Modalidade,ID Respondente,Eixo,Dimensão,Macroprocesso,Segmento,Campus,Curso,Resposta
df1 = df.drop(['Indicador','Subsídio p/ Avaliações', 'Modalidade', 'ID Respondente', 'Eixo', 'Dimensão', 'Macroprocesso', 'Campus'], axis=1)
print(df1)

#Quantidade de respostas
gestor = (df1['Segmento'] == 'Gestor').sum()
print("GESTORES: \n")
print(gestor)
estudante = (df1['Segmento'] == 'Estudante').sum()
print("ALUNOS: \n")
print(estudante)
print("TECNICO: \n")
tecnico = (df1['Segmento'] == 'Técnico').sum()
print(tecnico)
print("DOCENTE: \n")
docente = (df1['Segmento'] == 'Docente').sum()
print(docente)

df_segmento = df.drop(['Indicador','Subsídio p/ Avaliações','Modalidade','ID Respondente','Eixo','Dimensão','Macroprocesso','Campus','Curso','Resposta'], axis=1)
print(df_segmento)

#quantidade de pessoas que participaram do questionario 
quantidade_gestor = ((df['Indicador'] == 'Como você avalia o processo de Autoavaliação Institucional conduzido pela Comissão Própria de Avaliação (CPA)?') & ( df['Segmento'] == 'Gestor')).sum()
print(quantidade_gestor)
quantidade_aluno = ((df['Indicador'] == 'Como você avalia o processo de Autoavaliação Institucional conduzido pela Comissão Própria de Avaliação (CPA)?') & (df['Segmento'] == 'Estudante')).sum()
print(quantidade_aluno)
qunatidade_aluno_med = ((df['Indicador'] == 'Como você avalia as ações de valorização do meio ambiente desenvolvidas pelo IFMA?') & (df['Segmento'] == 'Estudante')).sum()
print(qunatidade_aluno_med)
qunatidade_tecnico = ((df['Indicador'] == 'Como você avalia o processo de Autoavaliação Institucional conduzido pela Comissão Própria de Avaliação (CPA)?') & (df['Segmento'] == 'Técnico')).sum()
print(qunatidade_tecnico)
quantidade_docente = ((df['Indicador'] == 'Como você avalia o processo de Autoavaliação Institucional conduzido pela Comissão Própria de Avaliação (CPA)?') & (df['Segmento'] == 'Docente')).sum()
print(quantidade_docente)
quantidade_pessoas = quantidade_aluno + quantidade_gestor + qunatidade_tecnico + quantidade_docente
print("Pessoas: \n")
print(quantidade_pessoas)

#['Satisfatório', 'Parcialmente satisfatório', 'Insatisfatório', 'Sim', 'Não', 'Parcialmente', nan, 'insatisfatório', 'reuniões', 'e-mails', 'interação com alunos e ou servidores', 'ofícios, memorandos e processos físicos', 'redes sociais', 'site e feed de notícias', 'SUAP', 'boletins eletrônicos']
respostas_possiveis = df['Resposta'].unique().tolist()
print(respostas_possiveis)
respostas_total = 0
for values_rep in respostas_possiveis:
    respostas_total += 1
    print(respostas_total, values_rep) 
avaliacao_gestor = ((df['Segmento'] == 'Gestor') & (df['Resposta'])).sum()
print(avaliacao_gestor)

#gráfico das repostas dos gestores
respostas_gestores = df.loc[df['Segmento'] == 'Gestor', 'Resposta']
print(respostas_gestores)
contagem_repostas = respostas_gestores.value_counts()
contagem_repostas.plot(kind='bar')
plt.xlabel('Resposta')
plt.ylabel('Quantidade')
plt.title('Respostas dos Gestores')
plt.show()

#gráfico das repostas dos estudantes
respostas_estudantes = df.loc[df['Segmento'] == 'Estudante', 'Resposta']
contagem_repostas_estudantes = respostas_estudantes.value_counts()
contagem_repostas_estudantes.plot(kind='bar')
plt.xlabel('Resposta')
plt.ylabel('Quantidade')
plt.title('Respostas dos Estudantes')
plt.show()

#grafico das repostas do técnicos
respostas_tecnico = df.loc[df['Segmento'] == 'Técnico', 'Resposta']
contagem_repostas_tecnico = respostas_tecnico.value_counts()
contagem_repostas_tecnico.plot(kind='bar')
plt.xlabel('Resposta')
plt.ylabel('Quantidade')
plt.title('Respostas dos Técnico')
plt.show()

#grafico das repostas do docentes
respostas_docente = df.loc[df['Segmento'] == 'Docente', 'Resposta']
contagem_repostas_docente = respostas_docente.value_counts()
contagem_repostas_docente.plot(kind='bar')
plt.xlabel('Resposta')
plt.ylabel('Quantidade')
plt.title('Respostas dos Docentes')
plt.show()



# Tentando fazer multiplos graficos de uma vez
pessoas = df['Segmento']
print(pessoas)
indicador = df['Indicador']
print(indicador)
print(indicador.unique())
print(indicador.unique().tolist())

respostas_gestor =  df.loc[df['Segmento'] == 'Gestor']
perguntas_unicas_gestores = respostas_gestor['Indicador'].unique()
print("\n")
print(perguntas_unicas_gestores)
print(len(perguntas_unicas_gestores))

respostas_estudante = df.loc[df['Segmento'] == 'Estudante']
perguntas_unicas_estudante = respostas_estudante['Indicador'].unique()
print("\n")
print(perguntas_unicas_estudante)
print(len(perguntas_unicas_estudante))

respostas_docente = df.loc[df['Segmento'] == 'Docente']
perguntas_unicas_docente = respostas_docente['Indicador'].unique()
print("\n")
print(perguntas_unicas_docente)
print(len(perguntas_unicas_docente))

respostas_tecnico = df.loc[df['Segmento'] == 'Técnico']
perguntas_unicas_tecnico = respostas_tecnico['Indicador'].unique()
print("\n")
print(perguntas_unicas_tecnico)
print(len(perguntas_unicas_tecnico))


# perguntas_para_todo = respostas_gestor['Indicador'].unique() == respostas_docente['Indicador'].unique()
# print(perguntas_para_todo)

perguntas_unicas_docente1 = set(df.loc[df['Segmento'] == 'Docente', 'Indicador'].unique())
perguntas_unicas_estudante1 = set(df.loc[df['Segmento'] == 'Estudante', 'Indicador'].unique())
perguntas_unicas_tecnico1 = set(df.loc[df['Segmento'] == 'Técnico', 'Indicador'].unique())
perguntas_unicas_gestor1 = set(df.loc[df['Segmento'] == 'Gestor', 'Indicador'].unique())

# Agora, encontre a interseção para ver quais perguntas ambos os grupos responderam
perguntas_comum = perguntas_unicas_docente1.intersection(
    perguntas_unicas_estudante1,
    perguntas_unicas_docente1,
    perguntas_unicas_gestor1,
    perguntas_unicas_tecnico1
    )

print("Perguntas que docentes e estudantes responderam juntos:")
print(perguntas_comum)
print(len(perguntas_comum))


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
    ax = percentual_respostas.plot(kind='barh', stacked=True, figsize=(10,7), color=['#1b9e77', '#d95f02', '#7570b3', '#e7298a'])

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