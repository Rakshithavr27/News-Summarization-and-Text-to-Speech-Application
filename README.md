# News-Summarization-and-Text-to-Speech-Application
This web-based application extracts key details from multiple news articles related to a specified company, performs sentiment analysis, and generates a text-to-speech (TTS) output in Hindi. Users can input a company name and receive a structured sentiment report along with an audio output.
Features
News Extraction: Fetches and displays titles, summaries, and metadata from at least 10 unique news articles.
Sentiment Analysis: Analyzes the sentiment of the articles (positive, negative, neutral).
Comparative Analysis: Provides insights on how the company's news coverage varies.
Text-to-Speech: Converts the summarized content into Hindi speech.
User Interface: Simple web-based interface using Streamlit.
API Development: Communication between frontend and backend via APIs.

Installation
To run this application locally, follow these steps:

Clone the repository:
 git clone <repository-url>
 cd <repository-directory>

Install dependencies: Create a virtual environment (optional but recommended) and install the required packages:
   pip install -r requirements.txt

Set up API Key:
Replace the placeholder in fetch_news function with your own NewsAPI key.

Run the application:
    For the Streamlit app
    streamlit run app.py

Usage
Open your web browser and navigate to the Streamlit app (usually at http://localhost:8501).
Enter the company name in the input field and click "Fetch News".
The application will display the sentiment report and provide an audio file summarizing the report in Hindi.

API Endpoints
GET /news: Fetch news articles and sentiment analysis for a specified company.
Query Parameters:
company: The name of the company to fetch news for.

Example
To fetch news for Tesla, you can use the following API call:
GET http://localhost:5000/news?company=Tesla

Assumptions & Limitations
The application relies on the availability of news articles from the NewsAPI.
The sentiment analysis is based on the content provided by the articles, which may vary in quality.
The Google Translate API may have limitations on the number of requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
NewsAPI for providing news articles.
Hugging Face for sentiment analysis models.
gTTS for text-to-speech conversion.

Contact
For any inquiries, please contact at [rakshithavanakudure@gmail.com].
