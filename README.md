# IMDB Sentiment Analysis using NLP and Machine Learning

## Project Overview

This project is an End-to-End Natural Language Processing (NLP) application that predicts whether a movie review is Positive or Negative.

The project uses TF-IDF feature extraction and compares multiple Machine Learning models to identify the best-performing classifier.

## Dataset

* Dataset: IMDB Movie Reviews Dataset
* Total Reviews: 50,000
* Classes:

  * Positive
  * Negative

## Models Compared

1. Logistic Regression
2. Multinomial Naive Bayes
3. LinearSVC
4. Random Forest Classifier

## Model Performance

| Model               | Train Accuracy | Test Accuracy |
| ------------------- | -------------- | ------------- |
| Logistic Regression | 88.32%         | 87.32%        |
| MultinomialNB       | 89.15%         | 87.02%        |
| LinearSVC           | 98.35%         | 90.07%        |
| Random Forest       | 84.96%         | 82.76%        |

### Best Model

LinearSVC achieved the highest test accuracy of 90.07% and was selected as the final model.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* TF-IDF Vectorization
* Streamlit
* Joblib

## Project Workflow

1. Data Loading
2. Data Preprocessing
3. Feature Engineering using TF-IDF
4. Model Training
5. Model Evaluation
6. Model Selection
7. Model Saving
8. Streamlit Deployment

## Features

* Sentiment Prediction
* Multiple Model Comparison
* Machine Learning Pipeline
* Deployment Ready
* User-Friendly Web Interface

## How to Run

1. Clone the repository
2. Install dependencies

pip install -r requirements.txt

3. Run Streamlit application

streamlit run app.py

## Author

Harshit Sharma

## Future Improvements

* Hyperparameter Tuning
* BERT-based Sentiment Analysis
* Advanced Text Preprocessing
* Docker Deployment

