# game/board.py
import chess

class ChessBoard:
    def __init__(self):
        """Yangi shaxmat taxtasi yaratadi"""
        self.board = chess.Board()

    def get_fen(self):
        """Hozirgi board holatini FEN string sifatida qaytaradi"""
        return self.board.fen()

    def push_move(self, move_uci: str):
        """
        Harakatni boardga qo‘shadi.
        move_uci: string, masalan 'e2e4'
        """
        move = chess.Move.from_uci(move_uci)
        if move in self.board.legal_moves:
            self.board.push(move)
        else:
            raise ValueError(f"Illegal move: {move_uci}")

    def reset_board(self):
        """Boardni boshlang‘ich holatga qaytaradi"""
        self.board.reset()
