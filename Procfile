web: gunicorn -w 4 -b 0.0.0.0:$PORT Event_Manage.app:app
release: python -c "from Event_Manage.app import init_db; init_db()"
