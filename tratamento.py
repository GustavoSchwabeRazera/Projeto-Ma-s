import pandas as pd
import numpy as np

class Tratamento:
    def __init__(self, caminho_arquivo='apple_quality.csv'):
        self.caminho_arquivo = caminho_arquivo
        self.df = None

    def carregar_e_limpar(self):
        """Carrega o CSV e realiza a limpeza padrão dos dados."""
        self.df = pd.read_csv(self.caminho_arquivo, dtype_backend='numpy_nullable')
        self.df.drop(4000, inplace=True, errors='ignore')
        self.df.drop('A_id', axis=1, inplace=True, errors='ignore')
        self.df['Acidity'] = self.df['Acidity'].astype('float')
        self.df = self.df.dropna()
        return self.df

    def obter_features_labels(self):
        """Separa o dataframe em X (features) e y (target)."""
        if self.df is None:
            self.carregar_e_limpar()
            
       
        colunas_features = self.df.drop(columns=['Quality']).columns.tolist()
        
       
        X = self.df.drop(columns=['Quality']).apply(pd.to_numeric, errors='coerce').to_numpy()
        y = self.df['Quality'].to_numpy()
        
        return X, y, colunas_features