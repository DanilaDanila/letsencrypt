FROM python:3.13-bookworm

ENV PYTHONPATH="/:/app"
ENV PATH=$PATH":/usr/games"

RUN \
    apt-get update && \
    apt-get install -y fortune

RUN pip install fastapi uvicorn

WORKDIR /app
COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4466"]
