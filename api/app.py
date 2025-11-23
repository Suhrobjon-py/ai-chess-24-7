from flask import Flask, request, jsonify
from game.board import ChessBoard
from engine.commands import get_ai_best_move

app = Flask(__name__)

# Global board obyektini yaratamiz
board = ChessBoard()

@app.route("/")
def home():
    return "Chess AI API is running!"

@app.route("/reset", methods=["POST"])
def reset():
    board.reset_board()
    return jsonify({"status": "reset_ok"})

@app.route("/move", methods=["POST"])
def make_move():
    data = request.json

    if "move" not in data:
        return jsonify({"error": "move key required"}), 400

    user_move = data["move"]

    try:
        board.push_move(user_move)  # foydalanuvchi yurishi
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    # AI yurishi
    fen = board.get_fen()
    ai_move = get_ai_best_move(fen)
    board.push_move(ai_move)

    return jsonify({
        "user_move": user_move,
        "ai_move": ai_move,
        "fen": board.get_fen()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
