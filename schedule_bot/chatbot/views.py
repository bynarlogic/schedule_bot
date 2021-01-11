import json
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from chatterbot import ChatBot


@method_decorator(csrf_exempt, name='dispatch')
class ChatBotApiView(View):
    chatbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        input = json.loads(request.body.decode('utf-8'))

        if 'text' not in input:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatbot.get_response(input['text'])

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)
    
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'name': self.chatbot.name
        })

