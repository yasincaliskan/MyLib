import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, Imputer, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

#1) Veri Önişleme
#1.1) Veri Yükleme
veriler = pd.read_csv('Wine.csv')

X = veriler.iloc[:,0:13].values
y = veriler.iloc[:,13].values

# Verilerin train-test olarak bölünmesi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

# Verilerin ölçeklenmesi - Standartlaştırma
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# PCA
pca = PCA(n_components = 2)

X_train2 = pca.fit_transform(X_train)
X_test2 = pca.transform(X_test)

# PCA dönüşümünden önce gelen Logistic Regression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# PCA dönüşümünden sonra gelen Logistic Regression
classifier2 = LogisticRegression(random_state = 0)
classifier2.fit(X_train2, y_train)

# Tahminler
y_pred = classifier.predict(X_test)
y_pred2 = classifier2.predict(X_test2)

# Actual / PCA olmadan
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Actual / PCA sonrası
cm2 = confusion_matrix(y_test, y_pred)
print(cm2)

# PCA sonrası / PCA öncesi
cm3 = confusion_matrix(y_pred, y_pred2)
print(cm3)

# LDA
lda = LDA(n_components = 2)
X_train_lda = lda.fit_transform(X_train, y_train)
X_test_lda = lda.transform(X_test)

# LDA dönüşümünden sonra
classifier_lda = LogisticRegression(random_state = 0)
classifier_lda.fit(X_train_lda, y_train)

# LDA tahmin et
y_pred_lda = classifier_lda.predict(X_test_lda)

cm4 = confusion_matrix(y_pred, y_pred_lda)
print(cm4)






    