from typing import List

from sqlalchemy.orm import Session

from models import Subreddit
from schemas.subreddit import SubredditCreate


class SubredditRepository():
    model = Subreddit

    def __init__(self, db: Session):
        self.db = db

    def list(self) -> List[Subreddit]:
        return self.db.query(self.model).all()

    def create(self, schema: SubredditCreate) -> Subreddit:
        subreddit = Subreddit(**schema.dict())
        self.db.add(subreddit)
        self.db.commit()
        self.db.refresh(subreddit)

        return subreddit

    def delete(self, subreddit_id: int) -> None:
        self.db.query(self.model).filter(self.model.id == subreddit_id).delete()
        self.db.commit()
