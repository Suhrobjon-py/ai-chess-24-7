# engine/stockfish.py
import os
import stat
from stockfish import Stockfish

# Stockfish binary fayl yo‘li
STOCKFISH_PATH = os.path.join(os.path.dirname(__file__), "stockfish-ubuntu-x86-64-avx2")

# Windows emas bo‘lsa (Linux/Render), faylni executable qilish
if os.name != "nt":  # Linux muhitida
    if os.path.exists(STOCKFISH_PATH):
        st = os.stat(STOCKFISH_PATH)
        os.chmod(STOCKFISH_PATH, st.st_mode | stat.S_IEXEC)

# Stockfish obyekti yaratish
stockfish = Stockfish(path=STOCKFISH_PATH, depth=15)
