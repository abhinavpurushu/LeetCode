import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter tweets with content length > 15
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]
