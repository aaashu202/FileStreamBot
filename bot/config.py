from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 23681812))
    API_HASH = env.get("TELEGRAM_API_HASH", "3152d0cda0a21787db0c924f522374b7")
    OWNER_ID = int(env.get("OWNER_ID", 6710996831))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "6710996831").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "ipapkorn_hindi_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6397250756:AAHEGEd9pGdnShtI1k6X_N80KmiauGGRGGE")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002242540576))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 14))

class Server:
    BASE_URL = env.get("BASE_URL", "http://106.196.43.183:8080")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

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
