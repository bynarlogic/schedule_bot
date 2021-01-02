from chatterbot.logic import LogicAdapter
from delorean import parse
from re import search
import spacy

class Schedule(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if search('(make|schedule).*appointment', statement.text):
            return True
        else: 
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement

        nlp = spacy.load('en_core_web_sm')
        doc = nlp(input_statement.text)

        entities = {}
        for ent in doc.ents:
            entities[ent.label_] = ent.text

        date = entities.get('DATE')
        time = entities.get('TIME')

        if date and time:
            appointment = parse(date+" "+time, dayfirst=False).datetime.strftime("%m/%d/%y at %H:%M:%S")
        elif date:
            appointment = parse(date, dayfirst=False).date.strftime("%m/%d/%y")
        elif time:
            appointment = parse(time).datetime.strftime("%m/%d/%y at %H:%M:%S")
        else:
            return Statement(text="please provide a preferred date and time for your appointment", confidence=1)

        response = "scheduling appointment for {}".format(appointment)
        return Statement(text=response, confidence=1)