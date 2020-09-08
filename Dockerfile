FROM python
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install  flask
RUN pip install  flask-login
RUN pip install  flask-openid
RUN pip install  flask-mail
RUN pip install  flask-sqlalchemy
RUN pip install  sqlalchemy-migrate
RUN pip install  flask-whooshalchemy
RUN pip install  flask-wtf
RUN pip install  flask-babel
RUN pip install  guess_language
RUN pip install  flipflop
RUN pip install  coverage
RUN pip install  redis
EXPOSE 5000

ADD . /code
CMD python run.py
