import os
import platform
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_stockfish_path():
    system = platform.system().lower()

    # Windows
    if system == "windows":
        path = os.path.join(BASE_DIR, "stockfish-windows-x86-64-avx2.exe")
        if os.path.exists(path):
            return path
        else:
            raise FileNotFoundError("Windows uchun stockfish .exe topilmadi!")

    # Linux (Render)
    path_linux = os.path.join(BASE_DIR, "stockfish-ubuntu-x86-64-avx2")
    if os.path.exists(path_linux):
        return path_linux

    raise FileNotFoundError("Hech qanday stockfish binary topilmadi!")


def run_stockfish(commands):
    engine_path = get_stockfish_path()

    process = subprocess.Popen(
        engine_path,
        universal_newlines=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1
    )

    for cmd in commands:
        process.stdin.write(cmd + "\n")
        process.stdin.flush()

    process.stdin.write("quit\n")
    process.stdin.flush()

    output = process.stdout.read()
    process.kill()
    return output


def get_best_move(fen):
    commands = [
        f"position fen {fen}",
        "go depth 20"
    ]
    output = run_stockfish(commands)

    for line in output.split("\n"):
        if "bestmove" in line:
            return line.split(" ")[1]

    return None
