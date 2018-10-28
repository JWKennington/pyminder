'''
This module contains base class definitions for reminders
'''


class Reminder(object):
    '''
    The reminder class outlines the key functionality of a Reminder
    '''
    def __init__(self, name: str, trigger, action):
        self.name = name
        self.trigger = trigger
        self.action = action
