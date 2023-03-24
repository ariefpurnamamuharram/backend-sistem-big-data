import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.example import get_example_sentiment_results

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
    return get_example_sentiment_results()
