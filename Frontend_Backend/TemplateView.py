import streamlit as st
import pandas as pd
import time

#________________________________________________________________Interface do usuário
class UInav:
    def menu_usuario():  
        st.sidebar.write("Comedouro Inteligente " + macadress)          
        op = st.sidebar.selectbox("Menu", ["Ver Dados", "Configurar"])
        if op == "Ver Dados": UInav.ver_dados()
        if op == "Configurar": UInav.criar_dados()
        if st.sidebar.button("Salvar"): pass 
        #salvar dados no banco
    
    def ver_dados():
        st.title(f"Analisar Dados")
        tab1, tab2, tab3 = st.tabs(["Reposição da Ração", "Nível da Ração", "Rotina de alimentação"])
        with tab1: UIoutput.reposicaoOut()
        with tab2: UIoutput.sensorOut()
        with tab3: UIoutput.rotinaOut() #terá tbm as informações do footer caso eu não encontre o meio de fazer um footer

    def criar_dados():
        st.title(f"Configurações")
        tab1, tab2, tab3 = st.tabs(["Criar Rotina", "Personalisar Tela", "Confirmar Limpeza"])
        with tab1: UIinput.rotinaIn()
        with tab2: UIinput.telaIn()
        with tab3: UIinput.limpezaIn()

class UIoutput:
    def reposicaoOut(): #tabela de reposições e se o sistema precisa ser limpo
        reposi = View.Reposicao_listar()
        if len(reposi) == 0: st.write("Sem dados disponíveis")
        else:
            #Avaliação de limpeza do pote
            racao = View.Reposicao_vencida()
            if Reposicao_vencida() == True: st.html("<p> O pote deve ser limpo: Sim</p>")
            else: st.html("<p> O pote deve ser limpo: em "+racao+" dias</p>")

            #Reposições cadastradas do pote em tabela
            list_dic = []
            for obj in reposi: list_dic.append(obj.to_df())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def sensorOut():
        # nível da ração atual em porcentagem e quantos gramas equivale 1%
        # nível da ração com tabela de linhas e baseado no tempo anotado na reposição (queda padrão conforme a programação de quanto cairá nas rotações)
        pass
    def rotinaOut():
        #--(int) gramas --(rotina) vezes ao dia
        #rotina 1                      ...    rotina X
        #rotina 1(h:m)-horaAtualRobo   ...   rotina X(h:m)-horaAtualRobo
        pass

class UIinput():
    def rotinaIn():
        st.markdown(f"""Preencha as informações pedidas abaixo para criar as rotinas de alimentação personalizadas.""")
        input_RacaoGramas = st.number_input("Ração diária(g): " min_value=10, max_value=100, value=30)
        input_Rotinas = st.number_input("Rotinas por dia: " min_value=1, max_value=10, value=3)
        if st.button("Gerar Rotinas"): 
            #gramas por rotação - quantas rotações terá - média queda de gramas por rotação
            Gramas, Rotacoes, RcRts, li_json_horaRotinas = 0, 0, 20, []
            while Gramas < input_RacaoGramas: #rotações devem estar baseado em quanto de ração caí em cada rotação
                Rotacoes += 1
                Gramas += RcRts
            for i in range(input_Rotinas): #vai receber os horários de cada rotina que haverá durante o dia
                dic_li["id"] = i
                dic_li["hora"] = {st.time_input(f"Informe o horário {i}: ")}
                li_json_horaRotinas.append(dic_li)
            if st.button("Enviar"):
                #enviar 
                pass
    def telaIn():
        pass
    def limpezaIn():
        if st.button("Submit"):pass
#________________________________________________________________VIEW-CONTROLLER
class View:
    '''
    
    '''
    pass




UIcomedouro.menu_usuario()

with open("estilo.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)