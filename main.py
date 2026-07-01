import rss_handler
import db_handler
import classifier
import time

def main():
    t0 = time.time()
    conn = db_handler.get_connection(db_handler.DB_CONFIG)
    try:
        items = rss_handler.fetch_feed_items(rss_handler.rss_url)
        print(f"Получено из RSS: {len(items)}")

        new_items = db_handler.filter_new_items(conn, items)
        print(f"Новых для обработки: {len(new_items)}")

        classifier.classify_sentiment(new_items)

        classifier.classify_svo(new_items)

        db_handler.bulk_insert(conn, new_items)
        
        print(f"Готово за {time.time() - t0:.2f} сек.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()