#!/bin/bash
gunicorn --log-level DEBUG -c gunicorn.py t_and_d.wsgi & python telegram_bot.py