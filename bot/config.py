from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 29640594))
    API_HASH = env.get("TELEGRAM_API_HASH", "425945b03d2da856ab43e3f20e5570b7")
    OWNER_ID = int(env.get("OWNER_ID", 6706180358))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "saki_yoshida_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002063983487))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 14))

class Server:
    BASE_URL = env.get("BASE_URL", "http://blue-lion-34.telebit.io:7070")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 7070))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'hydrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
