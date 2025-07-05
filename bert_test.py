from transformers import pipeline
import streamlit as st

classifier = pipeline("sentiment-analysis")
result = classifier("This inverter system is excellent and reliable.")
print(result)

st.title("BERT Sentiment Analyzer")

# Load sentiment pipeline
classifier = pipeline("sentiment-analysis")

text = st.text_area("Enter text:")

if text:
    result = classifier(text[:512])   # truncate if text is too long
    sentiment = result[0]["label"]
    score = result[0]["score"]

    st.write(f"**Sentiment:** {sentiment}")
    st.write(f"**Confidence:** {score:.2f}")