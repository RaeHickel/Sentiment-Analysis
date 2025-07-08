import streamlit as st
import pandas as pd
from transformers import pipeline

# Load the sentiment pipeline
classifier = pipeline("sentiment-analysis")

st.title("BERT Sentiment Analysis on CSV")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    # Read CSV
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data Preview", df.head())

    # Let the user pick which column has text
    text_columns = df.select_dtypes(include=['object']).columns.tolist()

    if not text_columns:
        st.error("No text columns found in your CSV.")
    else:
        text_col = st.selectbox("Select the text column for analysis:", text_columns)

        if st.button("Analyze Sentiment"):
            # Analyze each row
            sentiments = []
            scores = []

            for text in df[text_col]:
                # Prevent errors from empty rows
                if pd.isna(text) or str(text).strip() == "":
                    sentiments.append("No Text")
                    scores.append(0.0)
                    continue

                result = classifier(str(text)[:512])
                sentiments.append(result[0]['label'])
                scores.append(result[0]['score'])

            # Add results to DataFrame
            df["Predicted Sentiment"] = sentiments
            df["Sentiment Score"] = scores

            st.write("### Results Preview", df.head())

            # Provide download link
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download Results CSV",
                csv,
                file_name="sentiment_results.csv",
                mime="text/csv"
            )
