import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where author_id == viewer_id (self-view)
    self_views = views[views['author_id'] == views['viewer_id']]
    
    # Select distinct author_ids and rename the column to 'id'
    return pd.DataFrame(sorted(self_views['author_id'].unique()), columns=['id'])
