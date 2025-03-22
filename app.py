import streamlit as st
from utils import fetch_news, analyze_sentiment, generate_tts

def main():
    st.title("News Summarization and TTS Application")
    company_name = st.text_input("Enter Company Name:")
    
    if st.button("Fetch News"):
        articles = fetch_news(company_name)
        if articles:
            sentiment_report = analyze_sentiment(articles)
            st.json(sentiment_report)
            audio_file = generate_tts(sentiment_report)
            st.audio(audio_file)

if __name__ == "__main__":
    main()
