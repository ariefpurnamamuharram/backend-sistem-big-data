import datetime
import time
from random import randrange, choice

import pandas as pd

DEFAULT_RANDRANGE = 100


def get_example_sentiment_results():
    t = time.time()

    return {
        'time': time.strftime('%Y-%m-%d %H:%M:%S %Z', time.gmtime(t)),
        'formattedTime': time.strftime('%b %-d, %Y %I:%M %p', time.gmtime(t)),
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


def get_example_sentiment_dataframe(seed_per_item=10, inference_date=datetime.datetime.now()):
    data = []

    def random_date():
        return datetime.datetime.now() - datetime.timedelta(days=randrange(DEFAULT_RANDRANGE),
                                                            minutes=randrange(DEFAULT_RANDRANGE))

    for person in ['prabowo', 'anies', 'ganjar', 'puan']:
        for i in range(seed_per_item):
            data.append([person, randrange(10000), random_date(), inference_date, choice([0, 1])])

    df = pd.DataFrame(data, columns=['figure', 'video_id', 'published_at', 'inference_date', 'result'])
    df = df.sample(frac=1)

    return df
