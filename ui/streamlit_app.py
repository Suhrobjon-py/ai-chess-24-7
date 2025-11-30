import sys
import os
import streamlit as st
import chess
import chess.svg
from PIL import Image
import io
import cairosvg

# Projectning asosiy papkasini sys.path ga qo‘shish
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.board import ChessBoard
from engine.commands import get_ai_best_move, set_opening, sacrifice_piece

st.title("AI Chess 24/7 - Render")

# Yangi board yaratish yoki session_state orqali saqlash
if "board" not in st.session_state:
    st.session_state.board = ChessBoard()

board = st.session_state.board

# =======================
# Board vizualizatsiyasi
# =======================
def show_board(board):
    """ chess.Board() ob’ektini oladi va Streamlit’da PNG rasm sifatida chiqaradi """
    svg_board = chess.svg.board(board=board, size=400)
    png_board = cairosvg.svg2png(bytestring=svg_board.encode('utf-8'))
    image = Image.open(io.BytesIO(png_board))
    st.image(image)

# Boardni ekranga chiqarish
st.write("Hozirgi board:")
show_board(board)

# AI eng yaxshi harakat tugmasi
if st.button("AI eng yaxshi harakatni bajar"):
    fen = board.get_fen()
    move = get_ai_best_move(fen)
    board.push_move(move)
    st.write(f"AI harakati: {move}")
    st.write("Yangilangan board:")
    show_board(board)

# Boardni reset qilish tugmasi
if st.button("Boardni reset qilish"):
    board.reset_board()
    st.write("Board bosh holatga qaytarildi")
    show_board(board)
