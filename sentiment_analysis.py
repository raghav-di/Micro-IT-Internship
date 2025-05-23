import streamlit as st
import matplotlib.pyplot as plt
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon (if not already done)
nltk.download('vader_lexicon')

# Create the analyzer
sia = SentimentIntensityAnalyzer()

# Input text

st.title("SEntiment Analysis App")

user_input = st.text_input("Enter some text:")

# Get sentiment scores
scores = sia.polarity_scores(user_input)


compound = scores['compound']
if scores['pos']> scores['neu'] and scores['pos']>scores['neg']:
    sentiment = "The sentiment is Positive"
elif scores['neg']> scores['pos'] and scores['neg']>scores['neu']:
    sentiment = "The sentiment is Negative"
elif scores['neu']> scores['pos'] and scores['neu']>scores['neg']:
    sentiment = "The sentiment is Neutral"

if user_input != "":
    saisfaction_percent=round((1+scores['compound'])*50,3)
    st.write("Satisfaction Percentage:", saisfaction_percent,"%")
    st.write("Result:", sentiment)

fig, ax = plt.subplots(figsize=(8, 4))
labels = ['Negative', 'Neutral', 'Positive']
values = [scores['neg'], scores['neu'], scores['pos']]
ax.bar(labels, values, color=['red', 'yellow', 'green',])
ax.set_title('Sentiment Distribution')
ax.set_xlabel('sentiments')
ax.set_ylabel('Values')

st.pyplot(fig)