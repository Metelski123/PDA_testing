import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    
    def setUp(self):
        self.card = Card ("spades", 9)
        self.card_game = CardGame()   

    def test_check_for_ace_result_is_true(self):
        card1 = Card('hearts', 6)
        self.assertEqual(False, self.card_game.check_for_ace(card1))
    
    def test_check_for_ace_result_is_false(self):
        card2 = Card('diamonds', 1)
        self.assertEqual(True,self.card_game.check_for_ace(card2))


    def test_highest_card(self):
        card1 = Card('hearts', 9)
        card2 = Card('clubs', 3)
        self.assertEqual(card1,CardGame.highest_card(self,card1,card2))


    def test_cards_total(self):
        card1 = Card('diamonds', 7)
        card2 = Card('spades', 10)
        card3 = Card('clubs', 5)
        cards = [card1, card2, card3]
        self.assertEqual("You have a total of 22",self.card_game.cards_total(cards))