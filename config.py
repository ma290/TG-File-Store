import os

API_ID = int(os.environ.get("API_ID", '29529966'))
API_HASH = os.environ.get("API_HASH", '90807ece0df07a5943c29fbf51520459')
BOT_TOKEN = os.environ.get("BOT_TOKEN", '7247732685:AAHtSUv7iM1U-19qTvfaCr5NAk5HCefD1iY')
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", '-1002431381593')
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", '6630039904'))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '@leafposting')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
