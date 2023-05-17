# estudo de caso: SISREF

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard - Student Dataset", page_icon=":books:")

# sidebar
st.sidebar.title("Estudo de Caso 04: SISREF")

st.sidebar.subheader("Informações do Aluno:")
st.sidebar.markdown("- Nome: Raimundo G. de S. Júnior")
st.sidebar.markdown("- Matrícula: 20191035000227")
st.sidebar.markdown("- Universidade: IFCE Campus Cedro")
st.sidebar.markdown("- Curso: Sistemas de Informação")

# carregando o dataset
st.title("Dataset:")
show_id = "1378939680"
gsheets_url = 'https://docs.google.com/spreadsheets/d/1Xr6uPNAlT4n9FDuR91JyY2QwFGLGmMICPE5WqjW-s1k/export?format=csv&gid=' + show_id
data = pd.read_csv(gsheets_url, on_bad_lines='skip')

# dataframe
st.dataframe(data)

# gráfico de barras: quantidade de alunos por refeição
st.title("Quantidade de alunos por refeição:")
fig, ax = plt.subplots()
ax = sns.countplot(x="Refeicao", hue="Compareceu", data=data)
st.pyplot(fig)

# gráfico de barras: quantidade de alunos que não compareceram por refeição
st.title("Quantidade de alunos que não compareceram por refeição:")
fig, ax = plt.subplots()
ax = sns.countplot(x="Refeicao", hue="Compareceu", data=data[data["Compareceu"] == "Não"])
st.pyplot(fig)

# gráfico de barras: quantidade de refeições por mês
st.title("Quantidade de refeições por mês:")
refeicoes_por_mes = data["Mes_da_Refeicao"].value_counts().sort_index()
fig, ax = plt.subplots()
ax = sns.barplot(x=refeicoes_por_mes.index, y=refeicoes_por_mes.values)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.set_xlabel("Mês")
ax.set_ylabel("Quantidade de Refeições")
st.pyplot(fig)

# gráfico de barras: pessoas de um curso específico que foram para a refeição
curso_selecionado = "Bacharelado em Sistemas de Informação"
curso_data = data[data["Curso"] == curso_selecionado]
if not curso_data.empty:
    st.title(f"Quantidade de alunos de {curso_selecionado} que foram para a refeição:")
    fig, ax = plt.subplots()
    ax = sns.countplot(x="Refeicao", hue="Compareceu", data=curso_data)
    st.pyplot(fig)
else:
    st.warning(f"Não há dados para o curso {curso_selecionado}.")