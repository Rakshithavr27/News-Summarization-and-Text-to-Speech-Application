from flask import Flask, jsonify, request
from utils import fetch_news, analyze_sentiment

app = Flask(__name__)

@app.route('/news', methods=['GET'])
def get_news():
    company_name = request.args.get('company')
    articles = fetch_news(company_name)
    sentiment_report = analyze_sentiment(articles)
    return jsonify(sentiment_report)

if __name__ == "__main__":
    app.run(debug=True)
