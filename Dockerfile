FROM python:3
COPY . /ws_server_app
COPY requirements.txt /ws_server_app
WORKDIR /ws_server_app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "python", "-u", "main.py" ]