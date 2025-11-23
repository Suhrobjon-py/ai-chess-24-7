# engine/ai.py

from engine.stockfish import stockfish
from game.board import ChessBoard

class ChessAI:
    def __init__(self, board: ChessBoard):
        self.board = board

    def get_best_move(self):
        """Hozirgi board holatidan eng yaxshi AI harakatini qaytaradi."""
        fen = self.board.get_fen()
        stockfish.set_fen_position(fen)
        return stockfish.get_best_move()

    def apply_ai_move(self):
        """
        AIning eng yaxshi harakatini boardga qo‘shadi
        va move string qaytaradi.
        """
        best = self.get_best_move()
        if best:
            self.board.push_move(best)
        return best
