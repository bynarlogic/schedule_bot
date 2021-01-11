from chatterbot import ChatBot
from freezegun import freeze_time
import unittest

from schedule_bot.chatbot.logic.schedule_adapter import Schedule

@freeze_time('2020-01-01 04:00:00')
class TestSchedule(unittest.TestCase):
    def setUp(self):
        self.bot = ChatBot(
            'Bot',
            logic_adapters=[
                'schedule_bot.chatbot.logic.schedule_adapter.Schedule',
            ],
            preprocessors=[
                'schedule_bot.chatbot.preprocessors.format_dates',
                'schedule_bot.chatbot.preprocessors.capitalize_months'
            ]
        )
        self.schedule = Schedule(self.bot)
        from datetime import date
        self.assertEqual(date.today().isoformat(),'2020-01-01')
    
    def test_processes_appointment_request_with_date_and_time(self):
        result = self.bot.get_response('I would like to make an appointment for october 5th at 5 PM')
        self.assertEqual(result.text, 'scheduling appointment for 10/05/20 at 17:00:00')
    
    def test_processes_appointment_request_with_date_only(self):
        result = self.bot.get_response('I would like to make an appointment for October 5th')
        self.assertEqual(result.text, 'scheduling appointment for 10/05/20')
    
    def test_processes_appointment_request_with_downcased_date_only(self):
        result = self.bot.get_response('I would like to make an appointment for october 5th')
        self.assertEqual(result.text, 'scheduling appointment for 10/05/20')
    
    def test_processes_appointment_request_with_time_only(self):
        result = self.bot.get_response('I would like to schedule an appointment for 5 PM')
        self.assertEqual(result.text, 'scheduling appointment for 01/01/20 at 17:00:00')
    
    def test_processes_appointment_with_american_date(self):
        result = self.bot.get_response('I would like to schedule an appointment for 10-5-2020')
        self.assertEqual(result.text, 'scheduling appointment for 10/05/20')
    
    def test_handles_request_with_no_date_or_time(self):
        result = self.bot.get_response('I would like to schedule an appointment')
        self.assertEqual(result.text, 'please provide a preferred date and time for your appointment')

if __name__ == '__main__':
    unittest.main()