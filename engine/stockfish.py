import os
from stockfish import Stockfish

# Stockfish exe faylga path
STOCKFISH_PATH = os.path.join(os.path.dirname(__file__), "stockfish-windows-x86-64-avx2.exe")

# Stockfish obyekti, depth = qanchalik chuqur o‘ylash
stockfish = Stockfish(path=STOCKFISH_PATH, depth=15)

def get_ai_move(fen):
    """
    berilgan FEN holatidan AI ning eng yaxshi harakatini qaytaradi
    """
    stockfish.set_fen_position(fen)
    return stockfish.get_best_move()

