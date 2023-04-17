import streamlit as st
import pandas as pd
import numpy as np
import spacy

# st.image("nlp.jpg", width=200)

st.set_page_config(
    page_title="NLP-WebApp",
    page_icon="🧊",
    layout='wide',
    initial_sidebar_state='expanded'
    )
st.title("NLP")

nav = st.sidebar.selectbox('Navigation',['Lemmatizer', 'POS_Tagging', 'Noun Phrase Chunking'])

if nav == "Lemmatizer":
    nlp = spacy.load("en_core_web_sm")
    sentence = st.text_input("Enter your Sentence")

    if st.button("Generate"):
        res = nlp(sentence)
        output = {}
        for token in res:
                if token.pos_ not in output:
                    output[token.pos_] = []
                output[token.pos_].append(token)
        st.dataframe(output)

if nav == "POS_Tagging":
    nlp = spacy.load("en_core_web_sm")
    sentence = st.text_input("Enter your sentence")
    sentence = sentence.lower()
    doc = nlp(sentence)

    if st.button("Generate"):
        output = {}
        for token in doc:
            if token.pos_ not in output:
                output[token.pos_] = []
            output[token.pos_].append(token)
        st.dataframe(output)
if nav == "Noun Phrase Chunking":
    nlp = spacy.load("en_core_web_sm")
    sentence = st.text_input("Enter your Sentence")
    sentence = sentence.lower()
    doc = nlp(sentence)

    if st.button("Generate"):
            output = {}
            for token in doc:
                if token.pos_ not in output:
                    output[token.pos_] = []
                output[token.pos_].append(token)
            st.dataframe(output)