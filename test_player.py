import json
import player
import unittest

class Test_Player(unittest.TestCase):

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