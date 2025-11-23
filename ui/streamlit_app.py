import streamlit as st
from game.board import ChessBoard
from engine.commands import get_ai_best_move, set_opening, sacrifice_piece

st.title("AI Chess 24/7 - Render")

# Yangi board yaratish yoki session_state orqali saqlash
if "board" not in st.session_state:
    st.session_state.board = ChessBoard()

board = st.session_state.board

st.write("Hozirgi FEN:", board.get_fen())

if st.button("AI eng yaxshi harakatni bajar"):
    fen = board.get_fen()
    move = get_ai_best_move(fen)
    board.push_move(move)
    st.write(f"AI harakati: {move}")
    st.write("Yangilangan FEN:", board.get_fen())

if st.button("Boardni reset qilish"):
    board.reset_board()
    st.write("Board bosh holatga qaytarildi")
    st.write("FEN:", board.get_fen())
