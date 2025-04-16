# 📉 churn_prediction_telco

Projeto de Machine Learning para previsão de **cancelamento de clientes (churn)** em uma operadora fictícia de telecom.

---

## 💡 Objetivo

Criar um modelo preditivo capaz de identificar clientes com maior probabilidade de cancelamento com base em dados de uso e comportamento.

---

## 🧠 Técnicas utilizadas

- Manipulação de dados com **pandas**
- Codificação de variáveis categóricas
- Modelo de classificação com **Random Forest**
- Avaliação com **classification report**
- Visualização da importância das variáveis com **matplotlib**

---

## ▶️ Como executar

```bash
pip install -r requisitos.txt
python churn_model.py
```

O modelo será treinado e o gráfico de variáveis mais importantes será salvo na pasta `imagens`.

---

## 📊 Exemplo de colunas no dataset

- `plano`: tipo de plano contratado (Pré, Pós, Controle)
- `minutos`: total de minutos usados no mês
- `internet_GB`: uso de dados móveis
- `valor_fatura`: valor da fatura em reais
- `atraso_pagamento`: 1 se atrasou pagamento, 0 caso contrário
- `cancelou`: 1 se o cliente cancelou, 0 se está ativo

---

## 🙋‍♂️ Autor

Bruna Gouvêa  
🔗 [https://www.linkedin.com/in/bmedeirosgouvea/](https://www.linkedin.com/in/bmedeirosgouvea/)
