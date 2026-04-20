'''/app'''

import string
import random
from dotenv import load_dotenv
import os 
from urllib.parse import quote_plus
from sqlalchemy import create_engine

# carregando variavel de ambiente do .env
load_dotenv()


#criando uma chave aleatoria parar a scret key do flas
random_str = string.ascii_letters + string.digits + string.ascii_uppercase
#secret_key = ''.join(random.choice(random_str) for _ in range(32))
#print(f'Secret key: {secret_key}')

DEBUG = True
Secret_key = os.getenv('SECRET_KEY')

params = quote_plus("charset=utf8mb4")
SQLALCHEMY_DATABASE_URI = (
    '{SGDB}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?{params}'.format(
        SGDB='postgresql+psycopg2',
        USER=os.getenv('DB_USER'),
        PASSWORD=os.getenv('DB_PASSWORD'),
        HOST=os.getenv('DB_HOST'),
        PORT=os.getenv('DB_PORT'),
        DATABASE=os.getenv('DB_NAME'),
        params=params
    )
)
engine = create_engine(SQLALCHEMEY_DATABASE_URI) #cria uma conexao com o banco de dados usando o URI
SQL_TRACK_MODIFICATIONS = False #desativa um sistema que fica monitorando alterações nos objetos do banco
