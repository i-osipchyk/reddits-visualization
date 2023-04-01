import pandas as pd
import datetime as dt
from pmaw import PushshiftAPI

api = PushshiftAPI()
subreddits = ['sydney', 'melbourne', 'brisbane']

for subreddit in subreddits:
    for year in range(2019, 2023):
        since = int(dt.datetime(year, 1, 1, 0, 0).timestamp())
        until = int(dt.datetime(year + 1, 1, 1, 0, 0).timestamp())

        comments = api.search_comments(subreddit=subreddit, limit=None, since=since, until=until)

        comments_df = pd.DataFrame(comments)
        year_str = str(year)
        comments_df.to_csv(f'../../data/raw/{subreddit.capitalize()}/{subreddit}_{year}.csv', header=True, index=False,
                           columns=list(comments_df.axes[1]))
