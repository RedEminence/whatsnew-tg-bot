from collections import defaultdict

import praw

from settings import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET

subreddits = [
    'eldenring',
    'persona'
]


class API():
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent="Python App",
        )

    def collect_hot_submissions_by_subreddit(self, limit: int = 10) -> dict:
        submissions_by_subreddits = {subreddit: [] for subreddit in subreddits}

        for subreddit in subreddits:
            for submission in self.reddit.subreddit(subreddit).hot(limit=limit):
                submissions_by_subreddits[subreddit].append({
                    'title': submission.title,
                    'permalink': submission.permalink
                })

        return submissions_by_subreddits
