from chatterbot.logic import LogicAdapter
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

        confidence = 1
        response = "scheduling appointment"
        if date:
            response = "{} for {}".format(response,date)
        if time:
            response = "{} at {}".format(response,time)

        response_statement = Statement(text=response)
        response_statement.confidence = 1

        return response_statement