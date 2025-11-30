import sys
import os
import streamlit as st
import chess
import chess.svg
from PIL import Image
import io

# engine va game papkalarni ulash
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.board import ChessBoard
from engine.commands import get_ai_best_move

st.set_page_config(layout="centered")
st.title("♟ AI Chess 24/7 - Render")

# Board session
if "board" not in st.session_state:
    st.session_state.board = ChessBoard()

board = st.session_state.board

# === BOARDNI SVG RASM QILISH ===
def render_board_svg(chess_board):
    svg = chess.svg.board(chess_board.board)
    png = Image.open(io.BytesIO(svg.encode("utf-8")))
    return png

# Vizual board chiqishi
st.image(render_board_svg(board), use_container_width=True)

# FEN ko‘rsatish
st.code(board.get_fen(), language="text")

# AI harakat tugmasi
if st.button("🤖 AI yuradi"):
    fen = board.get_fen()
    move = get_ai_best_move(fen)
    board.push_move(move)
    st.success(f"AI yurishi: {move}")
    st.rerun()

# RESET tugmasi
if st.button("♻️ Boardni qayta boshlash"):
    board.reset_board()
    st.rerun()
