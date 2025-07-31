# BERT Sentiment Analysis Web App

This project features two interactive web applications built with Streamlit that use the Hugging Face `transformers` library to perform sentiment analysis with a BERT-based model.

## Project Summary

The goal is to apply BERT to real-world sentiment classification tasks using a no-code front-end built with Streamlit. The project includes:

1. **Text Input Analyzer (`bert_test.py`)**: An app for analyzing sentiment of user-typed text.
2. **CSV Analyzer (`BERT Sentiment Analysis on CSV.py`)**: An app that performs batch sentiment analysis on uploaded CSV files.

## Features

### `bert_test.py`
- Enter a custom sentence or paragraph.
- Uses a pretrained BERT sentiment pipeline.
- Displays:
  - **Sentiment label** (POSITIVE/NEGATIVE)
  - **Confidence score**

### `BERT Sentiment Analysis on CSV.py`
- Upload a `.csv` file containing text data.
- Automatically detects text columns.
- Lets you choose which column to analyze.
- Outputs sentiment label and confidence score for each row.
- Allows result download as a new CSV file.

## How It Works

- Loads Hugging Face `pipeline("sentiment-analysis")`, which defaults to `distilbert-base-uncased-finetuned-sst-2-english`.
- Truncates input text to 512 tokens (BERT's max input length).
- Outputs:
  - `label`: POSITIVE or NEGATIVE
  - `score`: Model confidence

## Requirements

- Python 3.7+
- streamlit
- transformers
- pandas



# How to Run
1. Sentiment on Text Input
bash
Copy
Edit
streamlit run bert_test.py
2. Sentiment on CSV File
bash
Copy
Edit
streamlit run "BERT Sentiment Analysis on CSV.py"
Then open the local URL provided by Streamlit (usually http://localhost:8501).

# Skills Demonstrated
Natural Language Processing (NLP)

BERT and Hugging Face Transformers

Streamlit app development

File I/O and DataFrame manipulation with pandas

Deployment-ready front-end for real users

# Author
Raghda Haikal
NLP with BERT – Sentiment Analysis Project
