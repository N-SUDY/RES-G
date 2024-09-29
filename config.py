# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23303247"))
API_HASH = getenv("API_HASH", "23623f737dc15708708c65a7297e1510")
BOT_TOKEN = getenv("BOT_TOKEN", "6398304554:AAF0shKN88TuXORWtoG7-qR_nFNXeH4lN_I")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7763435852").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://RADHAXRANI:RADHAXRANI@cluster0.ftpb4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002416068649")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002361150456"))
