from sqlalchemy import Column, String, Integer

from db.setup import Base


class Subreddit(Base):
    __tablename__ = 'subreddits'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
