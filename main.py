import streamlit as st
from tratamento import Tratamento
from modelo import GerenciadorModelos

st.set_page_config(page_title='Análise de Qualidade de Maçãs', layout='wide')
st.title('🍎 Previsão de Qualidade de Maçãs')


@st.cache_data
def inicializar_dados():
    tratamento = Tratamento('apple_quality.csv')
    df = tratamento.carregar_e_limpar()
    X, y, colunas_features = tratamento.obter_features_labels()
    return df, X, y, colunas_features

@st.cache_resource
def inicializar_modelos(X, y):
    gerenciador = GerenciadorModelos()
    gerenciador.treinar(X, y)
    return gerenciador


df, X, y, features = inicializar_dados()
gerenciador_modelos = inicializar_modelos(X, y)


st.sidebar.header("Insira os dados da maçã")
novo_dado = []

for col in features:
   
    min_val = float(df[col].min())
    max_val = float(df[col].max())
    mean_val = float(df[col].mean())
    
    valor = st.sidebar.slider(col, min_value=min_val, max_value=max_val, value=mean_val, step=0.1)
    novo_dado.append(valor)


if st.sidebar.button('Fazer Previsão'):
    st.subheader("📊 Resultados da Previsão")
    
   
    previsoes = gerenciador_modelos.prever_novo_dado(novo_dado)
    
    
    cols = st.columns(len(gerenciador_modelos.resultados))
    
    for idx, (nome, info) in enumerate(gerenciador_modelos.resultados.items()):
        acc = info['accuracy']
        previsao_atual = previsoes[nome]
        
        with cols[idx]:
            st.markdown(f"**{nome}**")
            st.metric(label="Acurácia do Modelo", value=f"{acc*100:.1f}%")
            
            if previsao_atual.lower() == 'good':
                st.success(f"Previsão: **{previsao_atual.upper()}**")
            else:
                st.error(f"Previsão: **{previsao_atual.upper()}**")
else:
    st.info("Ajuste os parâmetros na barra lateral e clique em 'Fazer Previsão'.")

st.write("---")
st.write("### Amostra do Dataset")
st.dataframe(df.head())