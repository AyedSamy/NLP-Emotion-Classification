# NLP Emotion Classification
![Kaggle](https://img.shields.io/static/v1?label=Dataset&message=Kaggle&color=20BEFF&logo=kaggle) ![Python 3.7](https://img.shields.io/static/v1?label=Python&message=3.7&color=3776AB&logo=python) ![Streamlit](https://img.shields.io/static/v1?label=Framework&message=Streamlit&color=FF4B4B&logo=streamlit) ![Scikit-learn](https://img.shields.io/static/v1?label=Library&message=Scikit-learn&color=F7931E&logo=scikit-learn) ![Seaborn](https://img.shields.io/badge/Library-Seaborn-success.svg)

This project is about **emotion classification** of messages sent by thousands of people via their mobile phone.
To be more precise, the dataset we use is devided into 3 parts (training dataset, test dataset & validation dataset) and contains details of **20 000 messages** labeled with an emotion. It includes following fields:

| **Field** | **Description** |
|-------|-------------|
|**Message**|*Message sent by the user*|
|**Emotion**|*Anger, Fear, Joy, Love, Sadness or Surprise*|

Working on this dataset, we have compared several methods to deal with text data.
Indeed, converting the messages in our datasets into numerical features was needed to use machine learning algorithms and perform classification.
Then, we compared **Bag-of-words** approach to **TF-IDF** (**CountVectorizer** / **TfidfTransformer**) from Scikit-learn library.

It was also important to define the **stopwords**, a list of words which couldn't help our models to make good predictions, because too common or too shared between different emotions in the dataset.

To perform the classification, we used a selection of **Supervised Machine Learning** algorithms for **Natural Language Processing**.
Thus, we compared the performance of **Multinomial Naive Bayes** models to **Logistic Regression** models, before and after **hyperparameter tuning** using Cross Validation / GridSearchCV.

Finally, the objective was to create an **end-to-end** Web Application: the Emotion Classifier allows us to make a new prediction, given a new input message.

The App has been built with **Streamlit** and is available on **Heroku** : https://nlp-emotion-classifier.herokuapp.com/
