from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = MetaData()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    decks = relationship("Deck", back_populates="user")

class Deck(Base):
    __tablename__ = 'decks'

    deck_id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship("User", back_populates="decks")
    cards = relationship("Card", back_populates="deck")

class Card(Base):
    __tablename__ = 'cards'

    card_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)
    deck_id = Column(Integer, ForeignKey('decks.deck_id'))
    deck = relationship("Deck", back_populates="cards")