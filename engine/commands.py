# engine/commands.py
from engine.stockfish import stockfish

def set_opening(opening_moves: list):
    """
    AIga ketma-ket ochilish harakatlarini yuboradi.
    Misol: Italian Game uchun ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4']
    """
    for move in opening_moves:
        stockfish.make_moves_from_current_position([move])

def sacrifice_piece(square: str, move: str):
    """
    AIga muayyan figurasini sacrifice qilish buyruqini beradi.
    square: qaysi figurani sacrifice qilmoqchisiz (masalan 'e4')
    move: shaxmat notation bo‘yicha harakat (masalan 'e4e5')
    """
    # AI harakatini kiritish
    stockfish.make_moves_from_current_position([move])

def get_ai_best_move(fen: str):
    """
    Berilgan FEN holatdan eng yaxshi AI harakatini oladi
    """
    stockfish.set_fen_position(fen)
    return stockfish.get_best_move()
