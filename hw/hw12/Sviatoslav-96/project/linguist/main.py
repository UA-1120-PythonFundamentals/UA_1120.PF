from linguist import LinguistApp

if __name__ == "__main__":
    db_uri = 'sqlite:///linguist.db'
    app = LinguistApp(db_uri)

if __name__ == "__main__":
    user1 = app.user_create("Аліна", "alina@example.ua", "password")
    print("Created user:", user1.name)

    user3 = app.user_create("Георгій", "georgiy@example.ua", "123456")
    deck3 = app.deck_create("Phrases", user3.user_id)
    print("Created deck:", deck3.name)

    user_updated = app.user_update_name(user1.user_id, "Олександр")
    print("Updated user name:", user_updated.name)

    password_changed = app.user_change_password(user3.user_id, "123456", "new_password")
    if password_changed:
        print("Password changed successfully")
    else:
        print("Failed to change password")

    card1 = app.card_create(user3.user_id, "Hello", "Привіт", "Greeting")
    card2 = app.card_create(user3.user_id, "Goodbye", "До побачення", "Farewell")
    print("Created cards:", card1.word, card2.word)

    filtered_cards = app.card_filter("Привіт")
    filtered_card_texts = [f"{card.word}: {card.translation} ({card.tip})" for card in filtered_cards]
    print("Filtered cards:", filtered_card_texts)

    app.card_update(card1.card_id, translation="Привітання")
    updated_card = app.card_get_by_id(card1.card_id)
    print("Updated card translation:", updated_card.translation)

    deck_by_id = app.deck_get_by_id(deck3.deck_id)
    if deck_by_id:
        print("Deck found by ID:", deck_by_id.name)

    deck_updated = app.deck_update(deck3.deck_id, "Updated Phrases")
    print("Updated deck name:", deck_updated.name)

    success = app.card_delete_by_id(card1.card_id)
    print("Deleted card:", card1.word)

    success = app.card_delete_by_id(card2.card_id)
    print("Deleted card:", card2.word)

    success = app.deck_delete_by_id(deck3.deck_id)
    print("Deleted deck:", deck3.name)

    success = app.user_delete_by_id(user3.user_id)
    print("Deleted user:", user3.name)