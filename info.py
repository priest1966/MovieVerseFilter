@@ -1,156 +0,0 @@
import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'MovieVerse')
API_ID = int(environ.get('API_ID', '900652'))
API_HASH = environ.get('API_HASH', 'a4183efcd370bf03011df1ba8772b1c9')
BOT_TOKEN = environ.get('BOT_TOKEN', "658:AAF6XLWv5T8LUhkr61lKVDfNZ5SJtU_lEd0")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
PICS = (environ.get('PICS', 'https://graph.org/file/bdf74912ff48bcedbe9cc.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/bdf74912ff48bcedbe9cc.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://t.me/howtoverify_97/3")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/bdf74912ff48bcedbe9cc.jpg")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001953637842'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '330029937').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001986007776 -1001548900361 -1002145274472 -1002069136954 -1002091789879').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# auth_channel means force subscribe channel.
# if REQUEST_TO_JOIN_MODE is true then force subscribe work like request to join fsub, else if false then work like normal fsub.
REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False)) # Set True Or False
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False)) # Set True Or False
auth_channel = environ.get('AUTH_CHANNEL', '-1002050647275') # give your force subscribe channel id here else leave it blank
auth_grp = environ.get('AUTH_GROUP', '-1002055042397') # give your force subscribe group id here else leave it blank
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002082710490')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002125544878')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001986007776 -1001548900361 -1002145274472 -1002069136954 -1002091789879')).split()]
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://icecube:lovely8249@cluster0.mn7t6la.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_DB')

# Premium And Referal Settings
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', True)) # Set Ture Or False

# If PREMIUM_AND_REFERAL_MODE is True Then Fill Below Variable, If Flase Then No Need To Fill.
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '10')) # number of referal count
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '30day')
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/e2d9b5e15e15daafb64e8.jpg')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - \n\n- 10ʀs - 1 ᴡᴇᴇᴋ\n- 30ʀs - 1 ᴍᴏɴᴛʜs\n- 50ʀs - 2 ᴍᴏɴᴛʜs\n\nᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ\n○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ\n\nᴜᴘɪ ɪᴅ - <code>movieverse@axl</code>\n\nᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n\nᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ\n\nᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ</b>')
OWNER_USERNAME = environ.get('OWNER_USERNAME', 'icecube9680_bot') # owner username without @

# Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/movieverse_discussion_2')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/movieverse_2')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/howtoverify_97/3')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'movieverse_discussion_2') # Support Chat Link Without https:// or @

# True Or False
AI_SPELL_CHECK = bool(environ.get('AI_SPELL_CHECK', True))
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# Token Verification Info :
VERIFY = bool(environ.get('VERIFY', True))
VERIFY_SECOND_SHORTNER = bool(environ.get('VERIFY_SECOND_SHORTNER', True))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', 'mdiskshortner.link')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', 'ca7ccd8b6e197a03f98baec5078920bf26987dc2')
# if verify second shortner is True then fill below url and api
VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', 'omegalinks.in')
VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '9b3b87cc699f7874fa7193531decf02364770e73')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', 'https://t.me/howtoverify_97/3')

# Shortlink Info
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'mdiskshortner.link')
SHORTLINK_API = environ.get('SHORTLINK_API', 'ca7ccd8b6e197a03f98baec5078920bf26987dc2')

# Others
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = environ.get("PORT", "8081")
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>File Name</b>: {file_name}\n\n<b>File Size:</b> {file_size}\n\n\n\n<b>Join Us: [MovieVerse Backup](https://t.me/movieversepremium)</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "<b>File Name</b>: {file_name}\n\n\n\n<b>Join Us: [MovieVerse Backup](https://t.me/movieversepremium)</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>{title}</b>\n\n<b>Genres:</b> {genres}\n<b>Rating:</b> {rating}/10 Based on {votes} user ratings.\n<b>Languages: Hindi Or {languages}</b>\n<b>RunTime:</b> {runtime} Minutes\n<b>Release Info:</b> {release_date}\n\n<b>Story Line:</b> {plot}\n\n<b>Download {query} From Here\n\n[MovieVerse Backup](https://t.me/movieversepremium)</b>")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# Choose Option Settings 
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]
EPISODES = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25", "E26", "E27", "E28", "E29", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E38", "E39", "E40"]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]
YEARS = ["1900", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]

# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://998c9929dc7a.herokuapp.com/")


# Rename Info : If True Then Bot Rename File Else Not
RENAME_MODE = bool(environ.get('RENAME_MODE', True)) # Set True or False

# Auto Approve Info : If True Then Bot Approve New Upcoming Join Request Else Not
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', True)) # Set True or False

# Save Restricted Info : If True Then Bot Save Content From Restricted Channel Else Not
SAVE_RESTRICTED_MODE = bool(environ.get('SAVE_RESTRICTED_MODE', False)) # Set True or False

# if SAVE_RESTRICTED_MODE is True Then Fill String Session Variable In Your Server Environment Variable, If Flase Then No Need To Fill.
# Warning: Never Fill String Session Variable In Your Repo, If You Fill Then Your Account Can Be Access By Anyone.
SESSION_STRING = environ.get('SESSION_STRING', 'BQANviwAOSuax91KJ49ZpY7_wYgFl2szvbSG8QAA5yZHYS4LFh_aMO9HegPpNzyDPWfFwC4osfZr_L4sMcVgbN6CeTRWaqPjNlXeHzzRDlRg0RfJs9_6KxebSKiE1-uFi1IzhGv2agso77huvPBrqxb0_ZQAm1XiapOO_mExrnURujp3l_gI_7F7jkhgWvim4GAS0MnEWOqr4g6yi0NQ6pW5tUSJMK7zABlcCeADZajjVO0UeWny65h7N7qxqBB7S49gme0lS0Tpvd9GP4KQDXGEtftXOeomuNf6jNBYktL0yLmdra5c-4k4B86kzIF3OaEcrG6m2idfoLx8SA6L1TOZty1_kwAAAAATq9txAA') # PYROGRAM V2 Session 

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
