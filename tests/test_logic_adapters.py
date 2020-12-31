from chatterbot import ChatBot
import unittest

from chatbot.logic.schedule_adapter import Schedule

class InputStatement():
    text: 'Hello'

class TestSchedule(unittest.TestCase):
    def setUp(self):
        bot = ChatBot('bot')
        self.schedule = Schedule(bot)
        self.input_statement = InputStatement()
    
    def test_can_process_appointment(self):
        self.input_statement.text = 'make an appointment for november 5th at 8 PM'
        result = self.schedule.can_process(self.input_statement)
        self.assertTrue(result)
    
        self.input_statement.text = 'can I make an appointment?'
        result = self.schedule.can_process(self.input_statement)
        self.assertTrue(result)

        self.input_statement.text = 'can I schedule an appointment?'
        result = self.schedule.can_process(self.input_statement)
        self.assertTrue(result)
    
    def test_processes_appointment_request_with_date_and_time(self):
        self.input_statement.text = 'I would like to make an appointmenet for october 5th at 5 PM'
        result = self.schedule.process(self.input_statement, {})
        self.assertEqual(result.text, 'scheduling appointment for october 5th at 5 PM')
    
    def test_processes_appointment_request_with_date_only(self):
        self.input_statement.text = 'I would like to schedule an appointement for october 5th'
        result = self.schedule.process(self.input_statement, {})
        self.assertEqual(result.text, 'scheduling appointment for october 5th')
    
    def test_processes_appointment_request_with_time_only(self):
        self.input_statement.text = 'I would like to schedule an appointement for 5 PM'
        result = self.schedule.process(self.input_statement, {})
        self.assertEqual(result.text, 'scheduling appointment at 5 PM')

if __name__ == '__main__':
    unittest.main()