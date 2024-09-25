FROM python:3.11
WORKDIR /code
RUN mkdir -p /.cache && chmod 777 /.cache
RUN mkdir -p ./Checkpoint/ && chmod 777 ./Checkpoint/
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./audio_files /code/audio_files/
COPY ./images /code/images/
COPY ./templates /code/templates/
COPY ./static /code/static/
COPY ./Model /code/Model/
COPY ./main.py /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

