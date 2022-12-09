import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv

from helper.validation import validation
from helper.response import error as response_error, success as response_success

from helper.telegram import Bot

load_dotenv()

def make_crawl(args):
   print("Crawling...")
   app = Bot()
   return app.get_last_posts_telegram(args["channels"])
   

def main(args):
      # VALIDATION ---------------------------------
      valid=validation(args)
      if not valid["status"]:
        return response_error(valid["message"])
      # --------------------------------------------
      response = make_crawl(args)
      return response_success(response)

if __name__ == "__main__":
  print(main({"channels":["channel_user_name"]}))