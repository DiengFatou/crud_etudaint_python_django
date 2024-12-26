FROM python:3.12

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gestion_etudiant.wsgi:application"]
