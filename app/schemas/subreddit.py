from pydantic import BaseModel


class SubredditCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Subreddit(SubredditCreate):
    id: int
