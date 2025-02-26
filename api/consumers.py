import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import os
from message.settings import STATIC_URL

class ChatConsumer(AsyncWebsocketConsumer):

    databse_url = os.path.join(STATIC_URL,'database.json')

    @database_sync_to_async
    def get_message(self,username,message):
        return_back_message = json.dumps({'username':username,'message':message})
        databse = open(self.databse_url)
        data = json.load(databse)
        data['message'].append({'username':username,'message':message})


        
        with open(self.databse_url, "w") as outfile:
            json.dump(data, outfile,indent=4)

        return return_back_message

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        
        print(f"Connecting to room: {self.room_name}")
        print(self.channel_name)
        self.roomGroupName = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )   
        print(f"Connecting to room: {self.roomGroupName}")
        await self.accept()
    
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_name 
        )
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        
        data = await self.get_message(username,message)
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message":data
                
            })
        
        
    async def sendMessage(self , event) : 
        
        message = event['message']
        if message:
            await self.send(message)
        else:
            await self.send(json.dump({'value':False}))
    
    