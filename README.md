# Stockfish API

A simple API interface for the Stockfish chess engine.

## Table of Contents
---------------------

1. [Overview](#overview)
2. [Features](#features)
3. [Usage](#usage)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Running the API](#running-the-api)
7. [API Endpoints](#api-endpoints)
8. [Contributing](#contributing)
9. [License](#license)

## Overview
------------
This project provides a RESTful API for interacting with the Stockfish chess engine. It allows users to send a FEN position to the API and receive the best move suggested by Stockfish.

## Features
------------
* Validate FEN positions
* Get the best move for a given FEN position

## Usage
---------
To use the API, send a POST request to the `/get_best_move` endpoint with a JSON payload containing a `fen` key with the FEN position.

## Example Request

```json
{
  "fen": "rnbqkbnr/ppp2ppp/8/8/8/8/PPPP2PPP/RNBQKBNR"
}
```

## Example Response

```json
{
  "best_move": "e4"
}
```

## requirements
_________________
• Python 3.7+
• Flask
• pyhton-chess
• Stockfish chess engine

## Installation
_________________
1. Install the required dependencies using pip: pip install -r requirements.txt
2. Download the Stockfish chess engine for your platform and place it in the Engine/ directory.

## Running the API
___________________
1. Start the API using Flask by executing the command: `flask run app.py`. For deployment purposes, consider using Gunicorn.

## API Endpoints
------------------
• /get_best_move: Get the best move for a given FEN position.

## GET Parameters
• fen: The FEN position to analyze.

## Responses
• best_move: The best move suggested by Stockfish.

## Contributing
----------------
Pull requests and contributions are welcome. Please submit a pull request with your changes.

## License
-----------
This project is licensed under the MIT License. See [LICENSE](#license) for details.