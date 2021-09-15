FROM python:3.9.6

WORKDIR /app

# Prevent writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent Python from buffering stderr and stdout
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY ./docker/api/requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./docker/api/entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY api/ .

ENTRYPOINT ["bash", "entrypoint.sh"]