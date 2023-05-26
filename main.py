from api.google_play_scraper import get_reviews
from manage.csv import save_to_csv

# Variables
APP_ID = ""
LANGUAGE = "pt-br"
COUNTRY = "br"

if __name__ == "__main__":
    reviews = get_reviews(app=APP_ID, lang=LANGUAGE, country=COUNTRY)
    save_to_csv(df=reviews)
