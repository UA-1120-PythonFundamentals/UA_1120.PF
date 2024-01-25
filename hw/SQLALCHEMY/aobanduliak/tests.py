import unittest
from linguist import user_create, user_get_by_id, user_update_name, user_change_password, user_delete_by_id
from linguist import deck_create, deck_get_by_id, deck_update, deck_delete_by_id
from linguist import card_create, card_get_by_id, card_filter, card_update, card_delete_by_id


class TestLinguistFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_functions(self):
        user1 = user_create("Alice", "alice@example.com", "password")

        user2 = user_get_by_id(user1.id)
        self.assertEqual(user2.name, user1.name)
        self.assertEqual(user2.email, user1.email)
        self.assertEqual(user2.password, user1.password)

        user_update_name(user1.id, "Bob")
        user2 = user_get_by_id(user1.id)
        self.assertEqual(user2.name, "Bob")

        self.assertTrue(user_change_password(
            user1.id, "password", "new_password"))
        user2 = user_get_by_id(user1.id)
        self.assertEqual(user2.password, "new_password")

        self.assertTrue(user_delete_by_id(user1.id))
        self.assertIsNone(user_get_by_id(user1.id))

    def test_deck_functions(self):
        user1 = user_create("Alice", "alice@example.com", "password")

        deck1 = deck_create("Deck 1", user1.id)
        self.assertEqual(deck1.name, "Deck 1")
        self.assertEqual(deck1.user_id, user1.id)

        deck2 = deck_get_by_id(deck1.id)
        self.assertEqual(deck2.name, deck1.name)
        self.assertEqual(deck2.user_id, deck1.user_id)

        deck_update(deck1.id, "Deck 2")
        deck2 = deck_get_by_id(deck1.id)
        self.assertEqual(deck2.name, "Deck 2")

        self.assertTrue(deck_delete_by_id(deck1.id))
        self.assertIsNone(deck_get_by_id(deck1.id))

    def test_card_functions(self):
        user1 = user_create("Alice", "alice@example.com", "password")
        deck1 = deck_create("Deck 1", user1.id)

        card1 = card_create(user1.id, "Hello", "Привіт", "Tip 1")
        self.assertEqual(card1.word, "Hello")
        self.assertEqual(card1.translation, "Привіт")
        self.assertEqual(card1.tip, "Tip 1")

        card2 = card_get_by_id(card1.id)
        self.assertEqual(card2.word, card1.word)
        self.assertEqual(card2.translation, card1.translation)
        self.assertEqual(card2.tip, card1.tip)

        cards = card_filter("Hello")
        self.assertIn(card1, cards)

        card_update(card1.id, word="Goodbye",
                    translation="До побачення", tip="Tip 2")
        card2 = card_get_by_id(card1.id)
        self.assertEqual(card2.word, "Goodbye")
        self.assertEqual(card2.translation, "До побачення")
        self.assertEqual(card2.tip, "Tip 2")

        self.assertTrue(card_delete_by_id(card1.id))
        self.assertIsNone(card_get_by_id(card1.id))


if __name__ == '__main__':
    unittest.main()
