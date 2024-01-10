import unittest
from task import user_create, user_get_by_id, user_update_name, user_change_password, user_delete_by_id
from task import deck_create, deck_get_by_id, deck_update, deck_delete_by_id
from task import card_create, card_get_by_id, card_filter, card_update, card_delete_by_id


class TestYourCode(unittest.TestCase):

    def test_user_operations(self):
        # Test User Creation
        user1 = user_create("John Doe", "john@example.com", "password123")
        self.assertIsNotNone(user1.id)

        # Test Get User by ID
        retrieved_user = user_get_by_id(user1.id)
        self.assertEqual(retrieved_user, user1)

        # Test Update User Name
        updated_user = user_update_name(user1.id, "John Smith")
        self.assertEqual(updated_user.name, "John Smith")

        # Test Change Password
        self.assertTrue(user_change_password(
            user1.id, "password123", "newpassword456"))

        # Test Delete User
        self.assertTrue(user_delete_by_id(user1.id))

        # Try to get the deleted user (expecting an error)
        with self.assertRaises(ValueError):
            user_get_by_id(user1.id)

    def test_deck_operations(self):
        # Assuming you have a user created for deck operations
        user1 = user_create("Alice", "alice@example.com", "password456")

        # Test Deck Creation
        deck1 = deck_create("Vocabulary", user1.id)
        self.assertIsNotNone(deck1.id)

        # Test Get Deck by ID
        retrieved_deck = deck_get_by_id(deck1.id)
        self.assertEqual(retrieved_deck, deck1)

        # Test Update Deck Name
        updated_deck = deck_update(deck1.id, "New Vocabulary")
        self.assertEqual(updated_deck.name, "New Vocabulary")

        # Test Delete Deck
        self.assertTrue(deck_delete_by_id(deck1.id))

        # Try to get the deleted deck (expecting an error)
        with self.assertRaises(ValueError):
            deck_get_by_id(deck1.id)

    def test_card_operations(self):
        # Assuming you have a user and a deck created for card operations
        user1 = user_create("Bob", "bob@example.com", "password789")
        deck1 = deck_create("Phrases", user1.id)

        # Test Card Creation
        card1 = card_create(user1.id, "Hello", "Привіт", "Greeting")
        self.assertIsNotNone(card1.id)

        # Test Get Card by ID
        retrieved_card = card_get_by_id(card1.id)
        self.assertEqual(retrieved_card, card1)

        # Test Filter Cards
        filtered_cards = card_filter("Hello")
        self.assertIn(card1, filtered_cards)

        # Test Update Card
        updated_card = card_update(
            card1.id, translation="Привіт!", tip="Common greeting")
        self.assertEqual(updated_card.translation, "Привіт!")
        self.assertEqual(updated_card.tip, "Common greeting")

        # Test Delete Card
        self.assertTrue(card_delete_by_id(card1.id))

        # Try to get the deleted card (expecting an error)
        with self.assertRaises(ValueError):
            card_get_by_id(card1.id)


if __name__ == '__main__':
    unittest.main()
