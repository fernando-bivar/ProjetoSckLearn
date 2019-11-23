# API Flask para modelo de Classificação em Scikit-Learn
### Colaboradores
Bruno Lucas Pereira (GIT - BrunoPereira1) (e-mail - brunolpereira17@hotmail.com)                                                         
Caio Romulo Alves de Carvalho (GIT - caio-romulo) (e-mail - caioromulo1@gmail.com)                                                       
Fernando Bivar Ramos de Melo (GIT - fernando-bivar) (e-mail - fernandobivar123@gmail.com)
### Orientador
Jamisson Freitas
### Disciplina
Tópicos Integradores 2 (Ciências de Dados)
### Descrição do Projeto
Uma simples aplicação Flask em conjunto com o Scikit-Learn, com o propósito de Classificar tulmores encontrados na mama através de suas determinadas caractéristicas, como, raio do tulmor, textura, suavidade, e área, em prol de realizar previsões sobre o mesmo, sendo ele "Benigno", que não apresenta ou apresenta pouco perigo, ou "Maligno", que dependendo da situação pode se caracterizar como um Câncer.

### Dependencies
- scikit-learn
- Flask
- pandas (No momento não sendo usado)
- numpy

```
pip install -r requirements.txt
```

### Running API
```
python app.py
#Colocar o caminho para o diretorio de acordo com sua máquina.
```



### /teste1 (GET)
Modelo de Classificação através do GaussianNB, importado do "sklearn.naive_bayes", e usado para treinar, testar e fazer previsões.

### /teste2 (GET)
Modelo de Classificação através do KNeighborsClassifier, importado do "sklearn.neighbors", e usado para treinar, testar e fazer previsões.

### END
