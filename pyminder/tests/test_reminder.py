import unittest
from pyminder import reminder


class ReminderTests(unittest.TestCase):
    def test_create_reminder(self):
        r = reminder.Reminder('Sample', 1, 0)
        self.assertIsInstance(r, reminder.Reminder)
