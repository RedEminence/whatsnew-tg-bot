from collections import defaultdict

import praw

from db.repositories import SubredditRepository
from db.utils import get_db
from config.settings import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET


class API():
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent="Python App",
        )

    def collect_hot_submissions_by_subreddit(self, limit: int = 10) -> dict:
        session = next(get_db())
        subreddits = SubredditRepository(session).list_of_names()
        submissions_by_subreddits = {subreddit: [] for subreddit in subreddits}

        for subreddit in subreddits:
            for submission in self.reddit.subreddit(subreddit).hot(limit=limit):
                submissions_by_subreddits[subreddit].append({
                    'title': submission.title,
                    'permalink': submission.permalink
                })

        return submissions_by_subreddits
