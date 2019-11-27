from flask import Flask, jsonify, request
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import json
#import mglearn

#%matplotlib inline

app = Flask(__name__)   
ia = ["mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness", "mean compactness", "mean concavity", "mean concave points", "mean symmetry", "mean fractal dimension", "radius error", "texture error", "perimeter error", "area error", "smoothness error", "compactness error", "concavity error", "concave points error", "symmetry error","fractal dimension error", "worst radius", "worst texture", "worst perimeter", "worst area", "worst smoothness", "worst compactness", "worst concavity","worst concave points", "worst symmetry", "worst fractal dimension"]

@app.route('/teste1', methods=['GET'])
def PrimeiroTeste():
    data = load_breast_cancer()
    
    label_names = data['target_names']
    labels = data['target']
    feature_names = data['feature_names']
    features = data['data']
    train, test, train_labels, test_labels = train_test_split(features,labels,test_size=0.33,random_state=42)
    gnb = GaussianNB()
    
    model = gnb.fit(train, train_labels)
    
    preds = gnb.predict(test)
    preds1 = np.array2string(preds)
    preds2 = preds1.replace('\n','')
    preds3 = preds2.replace(' ',',')
    
    avaliacaoPrev = accuracy_score(preds,test_labels)
    
    devs = [{
               'Avaliação no Teste' : '{:.3f}'.format(gnb.score(test, test_labels)),
               'Avaliação no Treino' : '{:.3f}'.format(gnb.score(train, train_labels)),
               'Previsão': preds3,
               'Avaliação da Previsão': avaliacaoPrev
           }]
    return jsonify(devs),200

@app.route('/teste2', methods=['GET'])
def SegundoTeste():
    cancer = load_breast_cancer()
    
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=66)
    
    training_accuracy = []
    test_accuracy = []
    
    neighbors_settings = range(1,11)
    
    for n_neighbors in neighbors_settings:
        clf = KNeighborsClassifier(n_neighbors=n_neighbors)
        clf.fit(X_train, y_train)
        training_accuracy.append(clf.score(X_train, y_train))
        test_accuracy.append(clf.score(X_test, y_test))
    
    preds = clf.predict(X_test)
    preds1 = np.array2string(preds)
    preds2 = preds1.replace('\n','')
    preds3 = preds2.replace(' ',',')
    
    avaliacaoPrev = accuracy_score(preds,y_test)
    
    plt.plot(neighbors_settings, training_accuracy, label='Accuracy of the training set')
    plt.plot(neighbors_settings, test_accuracy, label='Accuracy of the test set')
    plt.ylabel('Accuracy')
    plt.xlabel('Number of Neighbors')
    plt.legend()
    devs = [{
               'Avaliação no Teste': '{:.3f}'.format(clf.score(X_test, y_test)),
               'Avaliação no Treino': '{:.3f}'.format(clf.score(X_train, y_train)),
               'Previsão' : preds3,
               'Avaliação da Previsão' : avaliacaoPrev
           }]
    return jsonify(devs),200

#Esse app.route não funciona no POSTMAN poís depende do uso do "Submit"
@app.route('/apiForm', methods=['POST','GET'])
def GetRequestForm():
    cancer = load_breast_cancer()
    
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=66)
    
    training_accuracy = []
    test_accuracy = []
    
    neighbors_settings = range(1,11)
    
    for n_neighbors in neighbors_settings:
        clf = KNeighborsClassifier(n_neighbors=n_neighbors)
        clf.fit(X_train, y_train)
        training_accuracy.append(clf.score(X_train, y_train))
        test_accuracy.append(clf.score(X_test, y_test))
    
    strings = ""
    
    for k in ia:
        strings = strings + k +  '  <input type ="text" name = "{}"> </br>'.format(k)
    
    if request.method == 'POST':
        data = []
        
        for k in ia:
            data.append(float(request.form.get(k)))
        
        data = np.array(data)
    
        print(data)
        preds = clf.predict([data])
        preds1 = np.array2string(preds)
        preds2 = preds1.replace('\n','')
        preds3 = preds2.replace(' ',',')
    
        #print(request.__dict__)
    
        preds3 = "Maligno" if preds == 0 else "Benigno"
    
        return '<h1> PREVISÃO : {}.</h1>'.format(preds3)
    
    return '''<form method = "POST">
    {}
    <input type = "submit">
    </form> '''.format(strings)

@app.route('/api', methods=['POST'])
def GetRequest():
    cancer = load_breast_cancer()
    
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=66)
    
    training_accuracy = []
    test_accuracy = []
    
    neighbors_settings = range(1,11)
    
    for n_neighbors in neighbors_settings:
        clf = KNeighborsClassifier(n_neighbors=n_neighbors)
        clf.fit(X_train, y_train)
        training_accuracy.append(clf.score(X_train, y_train))
        test_accuracy.append(clf.score(X_test, y_test))
    
    values = []
    
    data = request.data
    data = json.loads(data)
    
    for k in ia:
        values.append(data[k])
    
    #print(data)
    preds = clf.predict([values])
    preds1 = np.array2string(preds)
    preds2 = preds1.replace('\n','')
    preds3 = preds2.replace(' ',',')
    
    #print(request.__dict__)
    
    preds3 = ["Maligno" if p == 0 else "Benigno" for p in preds]
    
    devs = [{
                'Previsão' : preds3
           }]
    
    return jsonify(devs)

if __name__ == '__main__':
    app.run(debug=True)
    
