FROM python:3.9-slim
WORKDIR /app
COPY . /app
EXPOSE 8000
# By default, run the server
CMD ["python", "server.py"]