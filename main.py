import re
from typing import Union
from datetime import datetime

from fastapi import FastAPI, Depends, HTTPException
import httpx
from sqlalchemy import create_engine, Column, Integer, String, DateTime , ARRAY
import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

from .translation_service import convert_emojis_to_text
app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()


class EmojiStory(Base):
    __tablename__ = "emoji_stories"
    id = Column(Integer, primary_key=True, index=True)
    emojiSequence = Column(String)  # Storing as comma-separated string to avoid error.
    translation = Column(String)
    authorNickname = Column(String)
    likes = Column(Integer)
    createdAt = Column(DateTime, default=datetime.utcnow)

class Translation(Base):
    __tablename__ = "translations"
    id = Column(Integer, primary_key=True, index=True)
    storyId = Column(Integer, ForeignKey("emoji_stories.id"))
    translation = Column(String)
    votes = Column(Integer)



Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class StoryCreate(BaseModel):
    emojiSequence: str
    translation: str
    authorNickname: str
    likes: int = 0
    createdAt: datetime = None

class StoryResponse(BaseModel):
    id: int
    emojiSequence: str
    translation: str
    authorNickname: str
    likes: int
    createdAt: datetime


    
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/stories/", response_model=StoryResponse)
async def create_story(story: StoryCreate, db: Session = Depends(get_db)):
    db_story = EmojiStory(**story.model_dump())
    emoji_sequence = story.emojiSequence

    #post request to /translations
    
    response = await httpx.post("http://localhost:8000/translations", json=story.model_dump())
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Translation failed")
    translation_data = response.json()
    db_story.translation = translation_data['translation']
    
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story

@app.get("/stories/{story_id}", response_model=StoryResponse)
async def read_story(story_id: int, db: Session = Depends(get_db)):
    db_story = db.query(EmojiStory).filter(EmojiStory.id == story_id).first()
    if not db_story:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story


@app.post("/translations")
async def create_translation(story: EmojiStory, db: Session = Depends(get_db)):
    emojiSequence = story.emojiSequence
    translation = convert_emojis_to_text(emojiSequence)
    db_translation = Translation(storyId=story.id, translation=translation, votes=0)
    db.add(db_translation)
    db.commit()
    db.refresh(db_translation)
    return db_translation

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)