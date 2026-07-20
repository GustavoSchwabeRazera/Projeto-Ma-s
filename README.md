# 🍎 Previsão de Qualidade de Maçãs (Machine Learning)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://projeto-ma-s-abfhet9md4ebhspjsx7fkv.streamlit.app/)

Este projeto é uma aplicação web interativa de Machine Learning desenvolvida em Python. O sistema simula a inserção de dados das características físicas de uma maçã e prevê a sua qualidade utilizando cinco algoritmos diferentes de classificação simultaneamente.

Acesse a aplicação rodando na nuvem: **[Testar o App ao vivo](https://projeto-ma-s-abfhet9md4ebhspjsx7fkv.streamlit.app/)**

## ✨ Funcionalidades

* **Múltiplos Modelos de IA:** O sistema treina e compara a performance de 5 modelos do Scikit-Learn: `Naive Bayes`, `KNN`, `Decision Tree`, `Random Forest` e `SVC`.
* **Comparativo de Acurácia:** Exibe lado a lado a acurácia de teste de cada modelo e a previsão específica gerada por eles.
* **Interface Dinâmica:** Os limites (mínimo, máximo e média) dos dados inseridos pelo usuário na barra lateral são lidos diretamente do dataset original de forma dinâmica.
* **Código Orientado a Objetos (POO):** A lógica de negócio e os modelos de IA estão separados em classes, garantindo um código limpo, escalável e de fácil manutenção.

## 🛠️ Tecnologias Utilizadas

* **[Python 3](https://www.python.org/):** Linguagem principal.
* **[Streamlit](https://streamlit.io/):** Criação da interface gráfica interativa web e deploy.
* **[Scikit-Learn](https://scikit-learn.org/):** Criação, treinamento e avaliação dos modelos de Machine Learning.
* **[Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/):** Limpeza, manipulação e tratamento e estruturação dos dados numéricos.

## 📁 Estrutura do Projeto

O projeto foi refatorado utilizando as melhores práticas de Engenharia de Software, separando as responsabilidades:

* `main.py`: Arquivo principal que gerencia o fluxo do Streamlit, cacheamento e renderização da interface.
* `modelos.py`: Classe que gerencia o escalonamento dos dados (`StandardScaler`), o treinamento em lote e as previsões da IA.
* `tratamento.py`: Classe responsável pelo carregamento e limpeza do dataset (tratamento de nulos, conversão de tipos e separação de features/labels).
* `apple_quality.csv`: Dataset original contendo o histórico com as características das maçãs.

## 🚀 Como executar o projeto localmente

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
