from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "8bd53e36eceada3329fbe46d9b961d1f")
      API_ID = int(getenv("API_ID", "29478734"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7090377529:AAESRjpsLObyoILsjvf-HODcAE6OifYpBi8")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002028796700:-1002028796700").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
