FROM python:3.8-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install pipenv
RUN pipenv install
EXPOSE 5000
CMD ["pipenv", "run", "python", "wsgi.py"]