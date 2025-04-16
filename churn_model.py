import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Carregar dados
df = pd.read_csv("telco_churn.csv")

# Pré-processamento simples
df_encoded = pd.get_dummies(df.drop(columns=["clienteID"]), drop_first=True)

# Separar features e target
X = df_encoded.drop("cancelou", axis=1)
y = df_encoded["cancelou"]

# Treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Avaliação
y_pred = modelo.predict(X_test)
print("Relatório de Classificação:\n")
print(classification_report(y_test, y_pred))

# Importância das variáveis
importancias = modelo.feature_importances_
plt.figure(figsize=(10,6))
plt.bar(X.columns, importancias, color='orange')
plt.title("Importância das Variáveis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("imagens/feature_importance.png")

print("\n✅ Modelo treinado e gráfico salvo em 'imagens/feature_importance.png'")
