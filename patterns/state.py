# State Design Pattern
from abc import ABCMeta, abstractmethod


class MP3PlayerContext(object):

    def __init__(self):
        self.state = StandbyState()

    def play(self):
        self.state.press_play(self)

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state


class State(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def press_play(self, context):
        pass


class StandbyState(State):
    def press_play(self, context):
        context.set_state(PlayingState())


class PlayingState(State):
    def press_play(self, context):
        context.set_state(StandbyState())
