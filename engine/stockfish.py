import os
import platform
from stockfish import Stockfish

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if platform.system() == "Windows":
    STOCKFISH_PATH = os.path.join(BASE_DIR, "stockfish-windows-x86-64-avx2.exe")
else:
    STOCKFISH_PATH = os.path.join(BASE_DIR, "stockfish-ubuntu-x86-64-avx2")

stockfish = Stockfish(path=STOCKFISH_PATH, depth=15)

def get_ai_move(fen):
    stockfish.set_fen_position(fen)
    return stockfish.get_best_move()
