import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from gtts import gTTS
import os
def fetch_news(company_name):
    api_key = "edf899f184d246f08f4369bc3be7a7ce"  # Replace with your NewsAPI key
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={api_key}"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Unable to fetch news, Status Code: {response.status_code}")
        return []

    # Parse the JSON response
    data = response.json()
    articles = data.get("articles", [])[:10]

    formatted_articles = []
    for article in articles:
        formatted_articles.append({
            "title": article["title"],
            "summary": article["description"] or "No summary available",
            "link": article["url"],
            "content": article["content"] or article["description"],
        })

    return formatted_articles


def analyze_sentiment(articles):
    # Load sentiment analysis pipeline from Hugging Face
    sentiment_pipeline = pipeline("sentiment-analysis")

    # Prepare report for analysis
    report = {"Company": "Unknown Company", "Articles": []}

    for article in articles:
        sentiment = sentiment_pipeline(article["content"])[0]
        report["Articles"].append({
            "Title": article["title"],
            "Summary": article["summary"],
            "Sentiment": sentiment["label"],
            "Score": round(sentiment["score"], 2),
            "Topics": []  # You can add topic extraction logic later if needed
        })

    return report

from googletrans import Translator
def generate_tts(report):

    # Create a summary from all articles
    summary = " ".join([article["Summary"] for article in report["Articles"] if article["Summary"] != "No summary available"])

    if not summary:
        summary = "कोई सारांश उपलब्ध नहीं है।"

    # Translate the summary to Hindi using googletrans
    translator = Translator()
    translated_summary = translator.translate(summary, dest="hi").text

    # Generate Hindi text-to-speech using gTTS
    tts = gTTS(text=translated_summary, lang="hi")
    audio_file = "summary.mp3"
    tts.save(audio_file)

    return audio_file


# Get top 10 news articles about Tesla
articles = fetch_news("Tesla")
print(articles)

# Analyze the sentiment of the articles
report = analyze_sentiment(articles)

# Generate the Hindi TTS
audio_file = generate_tts(report)

# Print the report and confirm audio
print(report)
print(f"Audio file generated: {audio_file}")

