web: gunicorn portfolio.wsgi --log-file - 

web: python manage.py migrate && gunicorn portfolio.wsgi