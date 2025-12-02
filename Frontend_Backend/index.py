import streamlit as st
import pandas as pd

class UIcomedouro:

    def menu_usuario():  
        st.sidebar.write("Comedouro Inteligente " + macadress)          
        op = st.sidebar.selectbox("Menu", ["Ver Dados", "Configurar"])
        if op == "Ver Dados": UIcomedouro.ver_dados()
        if op == "Configurar": UIcomedouro.criar_dados()
    
    def ver_dados():
        st.title(f"Analisar Dados")
        tab1, tab2, tab3 = st.tabs(["Reposição da Ração", "Leitura dos sensores", "Rotina de alimentação"])
        with tab1: UIcomedouro.reposicaoOut()
        with tab2: ProfissionalUI.sensoresOut()
        with tab3: ProfissionalUI.rotinaOut()

    def criar_dados():
        st.title(f"Configurações")
        tab1, tab2, tab3 = st.tabs(["Criar Rotina", "Personalisar Tela", "Confirmar Limpeza"])
        with tab1: UIcomedouro.reposicaoIn()
        with tab2: ProfissionalUI.sensoresIn()
        with tab3: ProfissionalUI.rotinaIn()

UIcomedouro.menu_usuario()

with open("estilo.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)