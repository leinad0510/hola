#Se sugiere diseñar la app antes de escribir el código
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('datos.csv')
st.title("Primera app") #crea el título de la página

tab1, tab2 = st.tabs(['Tab1', 'Tab2']) #crea las pestañas de mi página
#tab1
with tab1:
    st.header('Análisis gráfico')

    # Análsis univariado
    fig, ax = plt.subplots(1, 3, figsize = (10,4))  #crea lienzos donde se va a graficar, 1 fila 3 columnas, tamaño alto 10 ancho 4
    #edad
    ax[0].hist(df['edad']) 
    #sexo
    conteo = df['sexo'].value_counts() 
    ax[1].bar(conteo.index, conteo.values) 
    #salario
    ax[2].hist(df["salario"])
    fig.tight_layout()
    st.pyplot(fig)

    fig, ax= plt.subplots(1,2, figsize=(10,4))
    #edad vs salario
    sns.scatterplot(data=df, x='edad', y='salario', ax=ax[0]) 
    sns.violinplot(data=df, x='sexo', y='salario', ax=ax[1]) 
    fig.tight_layout()
    st.pyplot(fig)

with tab2:
    pass
