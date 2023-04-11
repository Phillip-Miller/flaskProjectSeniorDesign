export FLASK_CONFIG=config.ProdConfig
export FLASK_APP="geocache.__init__:create_app"
flask --app geocache db upgrade
gunicorn --workers 2 --threads 4 --timeout 60 --access-logfile \
    '-' --error-logfile '-' --bind=0.0.0.0:8000 \
     --chdir=/home/site/wwwroot app:app