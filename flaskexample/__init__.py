from flask import Flask

from .views import create_app

app = create_app()