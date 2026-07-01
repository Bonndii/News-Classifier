from transformers import pipeline

def classify_sentiment(items):
    """Батчевый инференс: одна загрузка модели, один проход списком, а не по одному."""
    if not items:
        return items
 
    sentiment_classifier = pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-roberta-base-sentiment-latest"
    )
 
    titles = [i["title"] for i in items]
    results = sentiment_classifier(titles)
    for item, res in zip(items, results):
        item["sentiment"] = res["label"]

def classify_svo(items):
    if not items:
        return items
    
    topic_classifier = pipeline(
        "zero-shot-classification",
        model="MoritzLaurer/deberta-v3-large-zeroshot-v2.0",
    )

    labels = ["related to military conflict between Russia and Ukraine", "unrelated to military conflict between Russia and Ukraine"]
    svo_label = labels[0]

    titles = [i["title"] for i in items]
    results = topic_classifier(titles, labels)
    for item, res in zip(items, results):
        item["about_svo"] = res["labels"][0] == svo_label