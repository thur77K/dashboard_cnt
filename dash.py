import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Dashboard Epidemiológico", layout="wide")

# Título
st.title("📊 Dashboard Epidemiológico - Canetas Emagrecedoras")

# KPIs principais
col1, col2, col3 = st.columns(3)
col1.metric("Internações", "343.992")
col2.metric("Óbitos", "9.933", delta="- impacto crítico")
col3.metric("Letalidade", "4,92%")

st.markdown("---")

# Abas para organização
tab1, tab2, tab3 = st.tabs(["⚠️ Alertas", "📊 Perfil Epidemiológico", "📌 Conclusão"])

# ---------------- TAB 1 ----------------
with tab1:
    st.subheader("Notificações vs Mortes (Eventos Adversos)")

    dados_alerta = pd.DataFrame({
        "Categoria": ["Notificações", "Mortes"],
        "Valores": [225, 6]
    })

    grafico_alerta = alt.Chart(dados_alerta).mark_bar().encode(
        x=alt.X("Categoria", sort=None),
        y="Valores",
        color=alt.Color(
            "Categoria",
            scale=alt.Scale(
                domain=["Notificações", "Mortes"],
                range=["#1f77b4", "#d62728"]
            )
        ),
        tooltip=["Categoria", "Valores"]
    ).properties(
        width=500,
        height=400,
        title="⚠️ Notificações de Eventos Adversos vs Mortes"
    )

    st.altair_chart(grafico_alerta, use_container_width=True)

    st.warning("""
    Os dados apresentados podem estar subestimados. Nem todos os eventos adversos
    relacionados ao uso de medicamentos emagrecedores são obrigatoriamente notificados,
    o que pode resultar em subnotificação e dificultar a real dimensão do problema.
    """)

    st.info("""
    Esses dados referem-se a eventos adversos associados ao uso de medicamentos
    para emagrecimento (como semaglutida, liraglutida e tirzepatida), que podem
    representar fatores de risco para complicações de saúde.
    """)

# ---------------- TAB 2 ----------------
with tab2:
    st.subheader("Perfil Epidemiológico da Pancreatite")

    pizza = pd.DataFrame({
        "Tipo": ["Internações", "Óbitos"],
        "Valores": [343992, 9933]
    })

    grafico_pizza = alt.Chart(pizza).mark_arc(innerRadius=50).encode(
        theta="Valores",
        color=alt.Color(
            "Tipo",
            scale=alt.Scale(
                domain=["Internações", "Óbitos"],
                range=["#1f77b4", "#d62728"]
            )
        ),
        tooltip=["Tipo", "Valores"]
    ).properties(
        width=500,
        height=400,
        title="📊 Proporção de Internações e Óbitos por Pancreatite"
    )

    st.altair_chart(grafico_pizza, use_container_width=True)

    st.info("""
    - Maior incidência em homens  
    - Faixa etária crítica: 40–49 anos  
    - Óbitos mais comuns entre 60–69 anos  
    """)

    st.markdown("""
    **Importante:**  
    Os dados apresentados referem-se ao perfil epidemiológico da pancreatite no Brasil.
    Em paralelo, observa-se o aumento do uso de medicamentos emagrecedores, que podem
    estar associados a eventos adversos e possíveis complicações, embora não representem
    necessariamente a causa direta de todos os casos.
    """)

# ---------------- TAB 3 ----------------
with tab3:
    st.subheader("Conclusão")

    st.success("""
    O uso de medicamentos injetáveis para emagrecimento tem crescido de forma significativa
    nos últimos anos, acompanhado por registros de eventos adversos, incluindo casos graves
    e óbitos. Paralelamente, os dados epidemiológicos da pancreatite indicam impacto relevante
    na saúde pública, com milhares de internações e mortes ao longo do período analisado.

    Embora não seja possível estabelecer uma relação causal direta em todos os casos,
    a associação entre o uso desses medicamentos e possíveis complicações reforça a necessidade
    de atenção e monitoramento.

    Além disso, a possível subnotificação dos eventos adversos representa um desafio importante,
    podendo ocultar a real dimensão dos riscos envolvidos. Dessa forma, torna-se essencial
    promover o uso responsável desses fármacos, com acompanhamento médico adequado,
    além do fortalecimento das estratégias de vigilância em saúde.

    O equilíbrio entre os benefícios e os riscos deve ser constantemente avaliado,
    visando garantir a segurança dos pacientes e reduzir impactos à saúde pública.
    """)

    st.markdown("**Fontes:**")
    st.markdown("- https://revistas.ifmsabrazil.org/eventos/article/view/1243")
    st.markdown("- https://periodicorease.pro.br/rease/article/view/25181")
