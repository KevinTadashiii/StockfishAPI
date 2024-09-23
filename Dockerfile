FROM ubuntu:latest

WORKDIR /app

COPY . /app

# Give execution rights to the Engine
RUN chmod +x Engine/stockfish\ linux