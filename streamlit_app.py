import streamlit as st
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
ranking.carrega_ranking()
