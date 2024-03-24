# Django
FROM python:3.9

ENV PYTHONUNBUFFERED 1

ARG APP=/code

WORKDIR ${APP}

RUN apt-get update && apt-get install -y --no-install-recommends \
    vim

COPY requirements.txt .

# It will install the framework and the dependencies
# in the `requirements.txt` file.
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . ${APP}

#ENTRYPOINT ["python", "./run.py"]

CMD ["python3"]