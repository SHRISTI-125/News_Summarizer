import streamlit as st
from transformers import pipeline
import re

summarizer = pipeline("summarization")

st.title("The News Summarizer by Shristi")

#text input 
article_text = st.text_area("📝 Write news here...", height=410)

def capitalize_word(text):
    text = text.strip().capitalize()
    return re.sub(r'(?<=[\.\?!])\s*(\w)', lambda m: m.group(1).upper(), text)
#button
if st.button("Summarize"):
    if article_text.strip() != "":
        summary = summarizer(article_text, max_length=150, min_length=25, do_sample=False)
        summarized_text = (summary[0]['summary_text']).capitalize()
        summarized_text = capitalize_word(summarized_text)
        st.subheader("🔍 Recap")
        st.write(summarized_text)
    else:
        st.error("Write text in blank area.")
