from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pymongo import MongoClient

analyzer = SentimentIntensityAnalyzer()

def update_review(uniq_id, review, collection):
    score = analyzer.polarity_scores(str(review))["compound"]
    sentiment = "positive" if score > 0.2 else "negative" if score < -0.2 else "neutral"

    collection.update_one(
        {"Uniq Id": uniq_id},
        {"$set": {
            "review": review,
            "sentiment": sentiment,
            "sentiment_score": float(score)
        }},
        upsert=True
    )

def update_bulk(df, collection):
    for index, row in df.iterrows():
        uniq_id = row["Uniq Id"]
        review_text = row["review"]
        update_review(uniq_id, review_text, collection)
