import unittest
from python.state import MP3PlayerContext, State, StandbyState, PlayingState


class StateTest(unittest.TestCase):

    def test_mp3_play_state(self):
        mp3_player = MP3PlayerContext()
        self.assertTrue(isinstance(mp3_player.get_state(), StandbyState))
        mp3_player.play()
        self.assertTrue(isinstance(mp3_player.get_state(), PlayingState))
        mp3_player.play()
        self.assertTrue(isinstance(mp3_player.get_state(), StandbyState))
        mp3_player.play()
        self.assertTrue(isinstance(mp3_player.get_state(), PlayingState))
