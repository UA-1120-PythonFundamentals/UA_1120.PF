users = []
decks = []
cards = []


class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password


class Deck:
    def __init__(self, id, name, user_id):
        self.id = id
        self.name = name
        self.user_id = user_id


class Card:
    def __init__(self, id, user_id, word, translation, tip):
        self.id = id
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip


def user_create(name, email, password):
    if not name or not email or not password:
        raise ValueError("Name, email, and password are required.")
    id = len(users) + 1
    user = User(id, name, email, password)
    users.append(user)
    return user


def user_get_by_id(user_id):
    for user in users:
        if user.id == user_id:
            return user
    raise ValueError(f"No user found with id {user_id}")


def user_update_name(user_id, name):
    user = user_get_by_id(user_id)
    if not name:
        raise ValueError("Name is required.")
    user.name = name
    return user


def user_change_password(user_id, old_password, new_password):
    user = user_get_by_id(user_id)
    if user.password != old_password:
        raise ValueError("Old password is incorrect.")
    if not new_password:
        raise ValueError("New password is required.")
    user.password = new_password
    return True


def user_delete_by_id(user_id):
    user = user_get_by_id(user_id)
    users.remove(user)
    return True


def deck_create(name, user_id):
    if not name:
        raise ValueError("Name is required.")
    user_get_by_id(user_id)  # Will raise an error if user doesn't exist
    id = len(decks) + 1
    deck = Deck(id, name, user_id)
    decks.append(deck)
    return deck


def deck_get_by_id(deck_id):
    for deck in decks:
        if deck.id == deck_id:
            return deck
    raise ValueError(f"No deck found with id {deck_id}")


def deck_update(deck_id, name):
    deck = deck_get_by_id(deck_id)
    if not name:
        raise ValueError("Name is required.")
    deck.name = name
    return deck


def deck_delete_by_id(deck_id):
    deck = deck_get_by_id(deck_id)
    decks.remove(deck)
    return True


def card_create(user_id, word, translation, tip):
    if not word or not translation or not tip:
        raise ValueError("Word, translation, and tip are required.")
    user_get_by_id(user_id)  # Will raise an error if user doesn't exist
    id = len(cards) + 1
    card = Card(id, user_id, word, translation, tip)
    cards.append(card)
    return card


def card_get_by_id(card_id):
    for card in cards:
        if card.id == card_id:
            return card
    raise ValueError(f"No card found with id {card_id}")


def card_filter(sub_word):
    if not sub_word:
        raise ValueError("Sub-word is required.")
    return [card for card in cards if sub_word in card.word or sub_word in card.translation or sub_word in card.tip]


def card_update(card_id, word=None, translation=None, tip=None):
    card = card_get_by_id(card_id)
    if word is not None:
        card.word = word
    if translation is not None:
        card.translation = translation
    if tip is not None:
        card.tip = tip
    return card


def card_delete_by_id(card_id):
    card = card_get_by_id(card_id)
    cards.remove(card)
    return True
