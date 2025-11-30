import chess
import chess.svg
from cairosvg import svg2png

def render_board(fen: str, output_path: str = "board.png"):
    board = chess.Board(fen)
    svg_image = chess.svg.board(board=board)

    # SVG → PNG
    svg2png(bytestring=svg_image.encode("utf-8"), write_to=output_path)

    return output_path
