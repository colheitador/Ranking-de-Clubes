import streamlit as st
# import time
# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

def carrega_ranking():

    st.markdown("""
    <div style='text-align: center; color: darkorange; font-weight: bold; font-size: 25px;'>
        Ranking de Clubes
    </div>
    """, unsafe_allow_html=True)
    st.write("") # pula linha

    if "titulos" not in st.session_state:
        st.session_state.titulos = [
            {"nome": "Brasileirão", "valor": 10, "ativo": True},
            {"nome": "Copa do Brasil", "valor": 7, "ativo": True},
            {"nome": "Libertadores", "valor": 30, "ativo": True},
            {"nome": "Estadual", "valor": 1, "ativo": False},
        ]

    # Inicializar o estado
    if "times" not in st.session_state:
        st.session_state.times = []


    

    # # Se quiser começar com 1 time automaticamente:
    if len(st.session_state.times) == 0:
        st.session_state.times.append({"nome": "", "titulos": {}})


    # Definir os títulos e valores
    titulos = {
        t["nome"]: t["valor"]
        for t in st.session_state.titulos
        if t["ativo"] and t["nome"].strip() != ""
    }


    #-----
    with st.expander(":orange[**🏆 Configurar títulos**]"):
        # st.subheader("⚙️ Configuração dos Títulos")

        remover_titulo = None

        for i, titulo in enumerate(st.session_state.titulos):
            col1, col2, col3, col4 = st.columns([4, 2, 2, 1])

            with col1:
                nome = st.text_input(
                    "Nome do título",
                    value=titulo["nome"],
                    key=f"titulo_nome_{i}"
                )
                st.session_state.titulos[i]["nome"] = nome

            with col2:
                valor = st.number_input(
                    "Valor (pontos)",
                    min_value=0,
                    value=titulo["valor"],
                    step=1,
                    key=f"titulo_valor_{i}"
                )
                st.session_state.titulos[i]["valor"] = valor

            with col3:
                ativo = st.checkbox(
                    "Contabilizar",
                    value=titulo["ativo"],
                    key=f"titulo_ativo_{i}"
                )
                st.session_state.titulos[i]["ativo"] = ativo

            with col4:
                if st.button(":red[**❌ Eliminar título**]", key=f"remover_titulo_{i}"):
                    remover_titulo = i

            st.write("---")

        if remover_titulo is not None:
            st.session_state.titulos.pop(remover_titulo)
            st.rerun()

        if st.button(":orange[**➕ Adicionar novo título**]"):
            st.session_state.titulos.append({
                "nome": "",
                "valor": 1,
                "ativo": True
            })
            st.rerun()
    #-----

    with st.expander(":orange[**👚 Configurar clubes**]"):

        # Inputs dinâmicos por time (com selectboxes)
        dados = []

        # Criar variável de controle para remover clube
        remover_indice = None


        for i, time in enumerate(st.session_state.times):
            # st.subheader(f"Time {i+1}")

            col_nome, col_remover = st.columns([4, 1])

            with col_nome:
                nome = st.text_input(
                    "Nome do Clube",
                    value=time["nome"],
                    key=f"nome_{i}"
                )
                st.session_state.times[i]["nome"] = nome

            with col_remover:
                if st.button(":red[**➖ Remover clube**]", key=f"remover_{i}"):
                    remover_indice = i


            total_pontos = 0
            info_titulos = {}

            titulos_lista = list(titulos.items())

            N_COLS = 4
            for j in range(0, len(titulos_lista), N_COLS):
                cols = st.columns(N_COLS)

                for col, (titulo, valor) in zip(cols, titulos_lista[j:j+N_COLS]):
                    with col:
                        st.write(f"**{titulo}**")
                        # st.caption(f"vale {valor} pts")

                        qtd = st.selectbox(
                            "Quantidade",
                            options=range(0, 51),
                            key=f"{titulo}_{i}"
                        )

                        pontos = qtd * valor
                        st.write(f"Pontos: {pontos}")
                        st.write("") # pula linha (estética)
                        st.write("") # pula linha (estética)


                        info_titulos[titulo] = qtd
                        total_pontos += pontos


            dados.append({
                "Clube": nome,
                "Pontos": total_pontos,
                **info_titulos
            })

            st.write("---")

            # Botão para adicionar time
        if st.button(":orange[**➕ Adicionar novo clube**]"):
            st.session_state.times.append({
                "nome": "",
                "titulos": {}
            })

            # botão para remover time

        if remover_indice is not None:
            st.session_state.times.pop(remover_indice)
            st.rerun()


    # Mostrar ranking
    if dados:
        df = pd.DataFrame(dados)

        # st.subheader("Ranking")

        

        df = df.sort_values("Pontos", ascending=False).reset_index(drop=True)
        df.insert(0, "Posição", df.index + 1)
        st.dataframe(df, use_container_width=True, hide_index=True)

        atualizar = st.button(":orange[**Atualizar**]")
        if atualizar:
            st.rerun()


