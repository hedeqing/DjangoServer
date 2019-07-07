# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

from schoolteam.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('receive text_data: ' + text_data)
        fromName = text_data_json['fromName']
        room = text_data_json['room']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'fromName': fromName,
                'room': room,
            }
        )
    # Receive message from room group
    async def chat_message(self, event, fromName=None, room=None):
        message = event['message']
        fromName = event['fromName']
        room = event['room']

        # messages = Message.objects.create(content= message,fromName=fromName,room = room)
        # message.save()
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'fromName' : fromName,
            'room' : room,
        }))

