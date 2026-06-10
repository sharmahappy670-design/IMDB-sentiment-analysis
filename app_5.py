import streamlit as st
import joblib
model=joblib.load("imdb_sentiment_model.joblib")
st.title("IMDB Sentiment Analysis")
review=st.text_area("Enter movie review")
if st.button("Predict"):
    prediction=model.predict([review])[0]
    if prediction == 1:
        st.success("Positive review")
    else:
        st.error("Negative review")
