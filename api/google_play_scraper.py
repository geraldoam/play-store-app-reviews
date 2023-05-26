from google_play_scraper import reviews, Sort
import pandas as pd


def get_reviews(app, lang, country):
    results, _ = reviews(
        app,
        lang=lang,
        country=country,
        sort=Sort.NEWEST,
        count=1000,
        filter_score_with=None,
    )

    data = []

    for result in results:
        review_id = result["reviewId"]
        user_name = result["userName"]
        user_image = result["userImage"]
        content = result["content"]
        score = result["score"]
        thumbs_up_count = result["thumbsUpCount"]
        review_created_version = result["reviewCreatedVersion"]
        at = result["at"]
        reply_content = result["replyContent"]
        replied_at = result["repliedAt"]
        app_version = result["appVersion"]

        data.append(
            {
                "Review ID": review_id,
                # "User Name": user_name,
                # "User Image": user_image,
                "Content": content,
                "Score": score,
                "Thumbs Up Count": thumbs_up_count,
                "Review Created Version": review_created_version,
                "At": at,
                "Reply Content": reply_content,
                "Replied At": replied_at,
                "App Version": app_version,
            }
        )

    df = pd.DataFrame(data)
    return df
