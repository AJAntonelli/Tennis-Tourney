import json
import player
import unittest

class Test_Player(unittest.TestCase):
    
    #TODO move test to test_data_layer.py
    def test_io(self):
        f = open('players.json')
        players = json.load(f)
        f.close()
        self.assertIsNotNone(players)        

    def test_initialize(self):
        expectedName = "D. Medvedev"
        expectedRating = 215
        actual = player.Player(expectedName, expectedRating)
        self.assertEqual(expectedName, actual.name) 
        self.assertEqual(expectedRating, actual.rating)

    def test_is_bye_true(self):
        p = player.Player('BYE', 0)
        self.assertTrue(p.is_bye())

    def test_is_bye_false(self):
        p = player.Player('notbye', 0)
        self.assertFalse(p.is_bye())