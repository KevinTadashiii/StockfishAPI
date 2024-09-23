"""
This script provides a RESTful API using Flask to interact with the Stockfish chess engine.
It can receive a FEN (Forsyth-Edwards Notation) position as input, and return the best move
suggested by Stockfish.
"""

import chess
import os
import sys
from flask import Flask, request, jsonify
from stockfish import Stockfish

# Create a new instance of the Flask web application
app = Flask(__name__)

class StockfishEngine:
    """
    This class provides a simple interface to interact with the Stockfish engine.

    Attributes:
        path (str): Path to the Stockfish engine executable
        engine (Stockfish): Instance of the Stockfish engine
    """

    def __init__(self):
        """
        Initialize a new StockfishEngine instance.
        
        This method sets the path to the Stockfish engine executable and creates a new instance
        of the engine.
        """
        self.path = self._get_stockfish_path()
        self.engine = Stockfish(path=self.path)
        
    def _get_stockfish_path(self):
        """
        Get the path to the Stockfish engine executable based on the operating system.

        Returns:
            str: Path to the Stockfish engine executable
        """
        if sys.platform == 'win32':
            return 'Engine/stockfish windows.exe'
        else:
            return 'Engine/stockfish linux'

    def get_best_move(self, fen):
        """
        Get the best move for a given FEN position.

        Args:
            fen (str): FEN position

        Returns:
            str: Best move in UCI (Universal Chess Interface) notation
        """
        self.engine.set_fen_position(fen)
        return self.engine.get_best_move()

def validate_fen(fen):
    """
    Validate a FEN position.

    Args:
        fen (str): FEN position

    Returns:
        bool: True if the FEN is valid, False otherwise
    """
    board = chess.Board(fen)
    return board.is_valid()

def validate_move(fen, move):
    """
    Validate a move for a given FEN position.

    Args:
        fen (str): FEN position
        move (str): Move in UCI notation

    Returns:
        bool: True if the move is valid, False otherwise
    """
    board = chess.Board(fen)
    return chess.Move.from_uci(move) in board.legal_moves

@app.route('/get_best_move', methods=['GET', 'POST'])
def get_best_move():
    """
    Handle a request to the /get_best_move endpoint.

    This endpoint expects a JSON payload with a 'fen' key containing a FEN position.
    It returns the best move suggested by Stockfish for that position.

    Returns:
        jsonify: JSON response with the best move, or an error message
    """
    data = request.json
    fen = data.get('fen')

    if not fen:
        # FEN is required, return an error if it's missing
        return jsonify({"error": "FEN is required"}), 400

    if not validate_fen(fen):
        # FEN is invalid, return an error
        return jsonify({"error": "Invalid FEN position"}), 400

    # Create a new StockfishEngine instance and get the best move
    stockfish = StockfishEngine()
    best_move = stockfish.get_best_move(fen)

    if not validate_move(fen, best_move):
        # Move is invalid, return an error
        return jsonify({"error": "Invalid move generated"}), 500

    # Move is valid, return it
    return jsonify({"best_move": best_move})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
