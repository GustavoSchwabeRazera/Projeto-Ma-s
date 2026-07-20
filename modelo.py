import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class GerenciadorModelos:
    def __init__(self):
        self.scaler = StandardScaler()
        self.modelos = {
            'Naive Bayes': GaussianNB(),
            'KNN': KNeighborsClassifier(n_neighbors=5),
            'Decision Tree': DecisionTreeClassifier(random_state=42),
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'SVC': SVC(kernel='rbf', random_state=42)
        }
        self.resultados = {}
        self.foi_treinado = False

    def treinar(self, X, y):
        """Divide os dados, aplica o scaler e treina todos os modelos."""
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
        
        
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        for nome, modelo in self.modelos.items():
            modelo.fit(X_train_scaled, y_train)
            previsao_teste = modelo.predict(X_test_scaled)
            acc = accuracy_score(y_test, previsao_teste)
            
            
            self.resultados[nome] = {
                'modelo': modelo, 
                'accuracy': acc
            }
            
        self.foi_treinado = True
        return self.resultados

    def prever_novo_dado(self, novo_dado):
        
        if not self.foi_treinado:
            raise Exception("Os modelos precisam ser treinados antes da previsão.")
            
       
        dado_array = np.array([novo_dado])
        dado_escalonado = self.scaler.transform(dado_array)
        
        previsoes = {}
        for nome, info in self.resultados.items():
            modelo = info['modelo']
            previsoes[nome] = modelo.predict(dado_escalonado)[0]
            
        return previsoes