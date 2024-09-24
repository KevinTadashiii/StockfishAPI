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

### Example Request

```json
{
  "fen": "rnbqkbnr/ppp2ppp/8/8/8/8/PPPP2PPP/RNBQKBNR"
}

### Example Response

```json
{
  "best_move": "e4"
}

### requirements
_________________
yes