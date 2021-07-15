import os

TARGET = os.getenv('TARGET', "localhost:8080,6582,8084,8085,8083")
authUrl = os.getenv('AUTH_TARGET', "bexs.auth0.com")


class Config:
    address = TARGET.split(":")
    ports = address[1].split(",")

    @classmethod
    def authentication_url(cls):
        return f'http://{authUrl}'