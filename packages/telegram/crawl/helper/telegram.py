import os
import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import time
 
class Bot:
  def __init__(self):
   TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
   TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
   PHONE_NUMBER = os.getenv("PHONE_NUMBER")
   TOKEN = os.getenv("TOKEN")
   
   if TOKEN:
    login = StringSession(TOKEN)
   else:
    login = StringSession()
   
   client = TelegramClient(login,TELEGRAM_API_ID,TELEGRAM_API_HASH)
   client.start()
   if not client.is_user_authorized():
          client.send_code_request(PHONE_NUMBER)
          me = client.sign_in(PHONE_NUMBER, input('Enter code: '))

   self.client = client

  async def _last_posts(self, channel_name,limit):
      # Get the channel entity
      channel_entity = await self.client.get_entity(channel_name)
      # Get the last 10 messages
      messages = await self.client.get_messages(channel_entity, limit= limit) 
      return messages
    
  def get_last_posts(self, channel_name,limit=10):
      loop = asyncio.get_event_loop()
      return loop.run_until_complete(self._last_posts(channel_name,limit))
    
  def get_last_posts_telegram(self,telegram_channels):
    response_data = {}
    for channel in telegram_channels:
      response_data[channel] = []
      for message in self.get_last_posts(channel):
        print(type(message.date))
        response_data[channel].append({
          "id":message.id,
          "text":message.message,
          "date": int(time.mktime(message.date.timetuple()))
        })
      
    return response_data