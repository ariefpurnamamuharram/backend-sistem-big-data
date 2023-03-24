import time
from random import randrange

DEFAULT_RANDRANGE = 100


def get_example_sentiment_results():
    t = time.time()

    return {
        'time': time.strftime('%Y-%m-%d %H:%M:%S %Z', time.gmtime(t)),
        'formattedTime': time.strftime('%b %-d, %Y %H:%M %p', time.gmtime(t)),
        'message': 'OK',
        'sentiments': {
            'prabowo': {
                'positive': randrange(DEFAULT_RANDRANGE),
                'negative': randrange(DEFAULT_RANDRANGE),
            },
            'anies': {
                'positive': randrange(DEFAULT_RANDRANGE),
                'negative': randrange(DEFAULT_RANDRANGE),
            },
            'ganjar': {
                'positive': randrange(DEFAULT_RANDRANGE),
                'negative': randrange(DEFAULT_RANDRANGE),
            },
            'puan': {
                'positive': randrange(DEFAULT_RANDRANGE),
                'negative': randrange(DEFAULT_RANDRANGE),
            }
        }
    }
