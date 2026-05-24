import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv(override=True)


def _required_env(name):
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Variavel de ambiente obrigatoria nao definida: {name}"
        )

    return value


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=_required_env("MYSQL_USER"),
        password=_required_env("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE", "ecommerce"),
        autocommit=False
    )