from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Deck, Card

class LinguistApp:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def user_create(self, name, email, password):
        user = User(name=name, email=email, password=password)
        self.session.add(user)
        self.session.commit()
        return user

    def card_create(self, user_id, word, translation, tip):
        card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
        self.session.add(card)
        self.session.commit()
        return card
    
    def card_filter(self, sub_word):
        filtered_cards = self.session.query(Card).filter(
            Card.word.like(f"%{sub_word}%")
        ).all()
        return tuple(filtered_cards)
    
    def card_update(self, card_id, word=None, translation=None, tip=None):
        card = self.session.query(Card).filter_by(card_id=card_id).first()
        if card:
            if word is not None:
                card.word = word
            if translation is not None:
                card.translation = translation
            if tip is not None:
                card.tip = tip
            self.session.commit()
            return card
        else:
            raise ValueError(f"Card with id {card_id} not found.")
        
    def card_get_by_id(self, card_id):
        card = self.session.query(Card).filter_by(card_id=card_id).first()
        if card:
            return card
        else:
            raise ValueError(f"Card with id {card_id} not found.")
        
    def user_delete_by_id(self, user_id):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        else:
            return False

    def user_get_by_id(self, user_id):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        return user
    
    def user_update_name(self, user_id, name):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        if user:
            user.name = name
            self.session.commit()
            return user
        else:
            raise ValueError(f"User with id {user_id} not found.")
        
    def user_change_password(self, user_id, old_password, new_password):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        if user:
            if user.password == old_password:
                user.password = new_password
                self.session.commit()
                return True
            else:
                return False
        else:
            raise ValueError(f"User with id {user_id} not found.")

    def deck_create(self, name, user_id):
        deck = Deck(name=name, user_id=user_id)
        self.session.add(deck)
        self.session.commit()
        return deck
    
    def deck_get_by_id(self, deck_id):
        deck = self.session.query(Deck).filter_by(deck_id=deck_id).first()
        return deck
    
    def deck_update(self, deck_id, name):
        deck = self.session.query(Deck).filter_by(deck_id=deck_id).first()
        if deck:
            deck.name = name
            self.session.commit()
            return deck
        else:
            raise ValueError(f"Deck with id {deck_id} not found.")

    def deck_delete_by_id(self, deck_id):
        deck = self.session.query(Deck).filter_by(deck_id=deck_id).first()
        if deck:
            self.session.delete(deck)
            self.session.commit()
            return True
        return False
    
    def card_delete_by_id(self, card_id):
        card = self.session.query(Card).filter_by(card_id=card_id).first()
        if card:
            self.session.delete(card)
            self.session.commit()
            return True
        else:
            return False
    
    def delete_all_cards(self):
        self.session.query(Card).delete()
        self.session.commit()

    def delete_all_decks(self):
        self.session.query(Deck).delete()
        self.session.commit()

    def delete_all_users(self):
        self.session.query(User).delete()
        self.session.commit()
        
    @staticmethod
    def test_linguist_app():
        db_uri = 'sqlite:///linguist.db'
        app = LinguistApp(db_uri)

        user1 = app.user_create("Аліна", "alina@example.ua", "password")
        print("Created user:", user1.name)

        user3 = app.user_create("Георгій", "georgiy@example.ua", "123456")
        deck3 = app.deck_create("Phrases", user3.user_id)
        print("Created deck:", deck3.name)

        card1 = app.card_create(user3.user_id, "Hello", "Привіт", "Greeting")
        card2 = app.card_create(user3.user_id, "Goodbye", "До побачення", "Farewell")
        print("Created cards:", card1.word, card2.word)

        filtered_cards = app.card_filter("Привіт")
        filtered_card_texts = [f"{card.word}: {card.translation} ({card.tip})" for card in filtered_cards]
        print("Filtered cards:", filtered_card_texts)

        app.card_update(card1.card_id, translation="Привітання")
        updated_card = app.card_get_by_id(card1.card_id)
        print("Updated card translation:", updated_card.translation)

        success = app.card_delete_by_id(card1.card_id)
        print("Deleted card:", card1.word)

        success = app.card_delete_by_id(card2.card_id)
        print("Deleted card:", card2.word)

        success = app.deck_delete_by_id(deck3.deck_id)
        print("Deleted deck:", deck3.name)

        success = app.user_delete_by_id(user3.user_id)
        print("Deleted user:", user3.name)