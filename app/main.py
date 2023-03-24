import datetime
import os
import time

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.example import get_example_sentiment_dataframe

# Load .env
load_dotenv()
app_name = os.getenv('APP_NAME', None)
app_env = os.getenv('APP_ENV', 'local')
if app_env not in ['production', 'local']:
    app_env = 'local'

# Configure FastAPI
if app_env == 'production':
    openapi_url = None
    allowed_origins = ['http://something/', 'https://something/']
else:
    openapi_url = '/docs/openapi.json'
    allowed_origins = ['*']

# Start FastAPI
app = FastAPI(openapi_url=openapi_url)
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=['*']
)

# Urls
BASE_URL = {
    'v1': '/api/v1'
}


@app.get('/')
async def welcome():
    return {'message': f'{app_name}'}


@app.get(f'{os.path.join(BASE_URL["v1"], "sentiments")}')
async def get_sentiments():
    # Please replace this line with the production code
    data = get_example_sentiment_dataframe(seed_per_item=300)

    data = data.drop_duplicates(subset=['video_id'])

    def get_result(dataframe, figure, result):
        if result not in [0, 1]:
            raise ValueError('Value is not allowed!')

        return len(dataframe.loc[(dataframe['figure'] == figure) &
                                 (dataframe['result'] == result) &
                                 (dataframe['published_at'] <= datetime.datetime.now())])

    t = time.time()

    return {
        'time': time.strftime('%Y-%m-%d %H:%M:%S %Z', time.gmtime(t)),
        'formattedTime': time.strftime('%b %-d, %Y %H:%M %p', time.gmtime(t)),
        'message': 'OK',
        'sentiments': {
            'prabowo': {
                'positive': get_result(data, 'prabowo', 1),
                'negative': get_result(data, 'prabowo', 0),
            },
            'anies': {
                'positive': get_result(data, 'anies', 1),
                'negative': get_result(data, 'anies', 0),
            },
            'ganjar': {
                'positive': get_result(data, 'ganjar', 1),
                'negative': get_result(data, 'ganjar', 0),
            },
            'puan': {
                'positive': get_result(data, 'puan', 1),
                'negative': get_result(data, 'puan', 0),
            }
        }
    }
