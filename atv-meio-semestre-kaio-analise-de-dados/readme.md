Alternativa: procure “Student Performance Dataset UCI” no Kaggle.
data set utilizado : https://www.kaggle.com/datasets/tejas14/student-final-grade-prediction-multi-lin-reg


Lembrete geral: se seu target é numérico, o Cenário A é linear e o Cenário B transforma
em binário (↑ Q3 =1, resto =0) para logística. Se o target é binário, o Cenário A é
logística e o Cenário B trata 0/1 como número para linear. Em ambos, calcule RMSE,
matriz de confusão, ROC/AUC e teste 3 thresholds(Limites).

Features: studytime, failures, absences, G1, G2.
## 9.10. PERGUNTAS FREQUENTES 173
Contexto: Modelo com notas anteriores fica “bom demais”?
Guia: Cenário A: R2 com G1+G2 vai ser muito alto. Retire G1 e G2 e recalcule —
o quanto caiu? É “justo” incluir notas anteriores se queremos prever antes de tê-las?
No Cenário B, compare AUC com e sem G1/G2.

## 9.5 O que o infográfico deve conter
O infográfico é 1 página PDF (Canva, PowerPoint, Google Slides, ou até papel escaneado).
Ele deve ter, visualmente:
1. Nome, problema e base de dados.
2. Pergunta de negócio (1 frase).
3. Cenário A (modelo natural): métricas, coeficientes, interpretação.
4. Cenário B (truque): métricas cruzadas, o que mudou.

5. Curva ROC e AUC (cole a imagem do gráfico).

6. Tabela comparando 3 thresholds (com VP, FP, FN, VN de cada).

7. Conclusão: qual modelo é melhor para este problema? Por quê?

## 9.4 Código-base que todo aluno deve usar
Copie e adapte conforme sua base e features. Não precisa decorar — precisa entender
cada linha e saber explicar no vídeo.

```
1 import numpy as np
2 import pandas as pd
3 from sklearn.model_selection import train_test_split
4 from sklearn.linear_model import (LinearRegression ,
5 LogisticRegression)
6 from sklearn.metrics import (mean_squared_error ,
7 confusion_matrix , classification_report ,
8 roc_curve , roc_auc_score)
9 import matplotlib.pyplot as plt
10
11 # 1. Carregar dados (adapte para sua base)
12 df = pd.read_csv("insurance.csv")
13 print (df.shape , df.dtypes)
14
15 # 2. Separar X e y
16 X = df[["age", "bmi"]] # suas features
17 y = df["charges"] # seu target
18
19 # 3. Split 80/20
20 X_train , X_test , y_train , y_test = train_test_split(
21 X, y, test_size=0.2, random_state =42)
22 # Se logistica: acrescente stratify=y
23
24 # 4a. Regressao Linear
25 reg = LinearRegression()
26 reg.fit(X_train , y_train)
27 y_pred = reg.predict(X_test)
28 rmse = np.sqrt(mean_squared_error(y_test , y_pred))
29 print (f"RMSE = {rmse:.2f}")
30 print (f"R2 = {reg.score(X_test , y_test):.4f}")
31 print ("Coeficientes:", reg.coef_)
32
33 # 4b. Transformar target em binario (Q3)
34 q3 = y_train.quantile (0.75)
35 y_train_bin = (y_train >= q3).astype(int )
36 y_test_bin = (y_test >= q3).astype(int )
37
38 # 4c. Regressao Logistica
39 log = LogisticRegression(max_iter =5000)
40 log.fit(X_train , y_train_bin)
41 prob = log.predict_proba(X_test)[:, 1]
42 print (f"AUC = {roc_auc_score(y_test_bin , prob):.4f}")
43
44 # 5. Matriz de confusao com threshold 0.5
45 pred = (prob >= 0.5).astype(int )
46 print (confusion_matrix(y_test_bin , pred))
47 print (classification_report(y_test_bin , pred))
48
49 # 6. Testar 3 thresholds
50 for th in [0.3, 0.5, 0.7]:
51 pred_th = (prob >= th).astype(int )
52 print (f"--- Threshold = {th} ---")
53 print (confusion_matrix(y_test_bin , pred_th))
54
55 # 7. Curva ROC
56 fpr , tpr , ths = roc_curve(y_test_bin , prob)
57 plt.figure(figsize=(6,6))
58 plt.plot(fpr , tpr , "b-",
59 label=f"Modelo (AUC={roc_auc_score(y_test_bin , prob)

:.2f})")

60 plt.plot([0,1],[0,1],"k--", label="Aleatorio")
61 plt.xlabel("FPR (Falso Positivo)")
62 plt.ylabel("TPR (Recall)")
63 plt.title("Curva ROC")
64 plt.legend()
65 plt.grid(True , alpha =0.3)
66 plt.show()
67
68 # 8. Coeficientes e OR (logistica)
69 for nome , beta in zip (X.columns , log.coef_[0]):
70 print (f"{nome}: beta={beta:.4f}, OR={np.exp(beta):.4f}")
```