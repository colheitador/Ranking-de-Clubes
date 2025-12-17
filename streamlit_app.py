import streamlit as st
from streamlit_option_menu import option_menu

# Importações dos tópicos
import ranking
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Configurações da página
st.set_page_config(
    page_title="Ranking de clubes",
    layout="wide",
    # initial_sidebar_state="expanded",
    page_icon=":soccer:",
)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# aprendizado_supervisionado_classificacao.carrega_supervisionado_classificacao()
ranking.carrega_ranking()

# # Lista de tópicos em ordem
# topicos = [
#     "1 - Página Inicial",
#     # "2.1 - Introdução: Conceitos básicos",
# ]

# # Guarda o índice atual
# if "topico_index" not in st.session_state:
#     st.session_state.topico_index = 0

# # Menu lateral
# with st.sidebar:
#     selected = option_menu(
#         "",
#         topicos,
#         default_index=st.session_state.topico_index
#     )

# # ⚠️ Atualiza o índice **somente se mudou**
# novo_index = topicos.index(selected)
# if novo_index != st.session_state.topico_index:
#     st.session_state.topico_index = novo_index
#     st.rerun()

# # Qual tópico foi selecionado
# topico_atual = topicos[st.session_state.topico_index]

# # # # Renderiza a página correspondente
# # # if topico_atual == "1 - Página Inicial":
# # #     inicial.carrega_inicial()
# # # elif topico_atual == "2.1 - Introdução: Conceitos básicos":
# # #     introducao.carrega_introducao()
# # # elif topico_atual == "2.2 - Próximos passos: Mãos à obra!":
# # #     maos_a_obra.carrega_maos_a_obra()
# if topico_atual == "3.1 - Aprendizado supervisionado: Classificação":
#     aprendizado_supervisionado_classificacao.carrega_supervisionado_classificacao()
# # # elif topico_atual == "3.2 - Aprendizado supervisionado: Regressão":
# # #     aprendizado_supervisionado_regressao.carrega_supervisionado_regressao()
# # # elif topico_atual == "3.3 - Quiz sobre aprendizado supervisionado":
# # #     app_perguntas_supervisionado.perguntas_aprendizado_supervisionado()
# # # elif topico_atual == "4.1 - Aprendizado não supervisionado: Clusterização":
# # #     ans_clusterizacao.carrega_nao_supervisionado_clusterizacao()
# # # elif topico_atual == "4.2 - Aprendizado não supervisionado: Redução de dimensionalidade":
# # #     ans_reducao_dimensionalidade.carrega_nao_supervisionado_reducao_dimensionalidade()
# # # elif topico_atual == "4.3 - Quiz sobre aprendizado não supervisionado":
# # #     app_quiz_nao_supervisionado.perguntas_aprendizado_nao_supervisionado()