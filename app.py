import os
import socket
import random
from flask import Flask, render_template

app = Flask(__name__)

# Define color codes
COLOR_CODES = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "pink": "#be2edd",
    "yellow": "#ffff00",
    "white": "#ffffff",
    "purple": "#7d3c98"
}

# Set default color from environment or randomly select one
color = os.getenv("APP_COLOR", random.choice(list(COLOR_CODES.keys())))

@app.route("/")
def main():
    return render_template('hello.html', name=socket.gethostname(), color=COLOR_CODES.get(color, "#ffffff"))

@app.route('/color/<new_color>')
def change_color(new_color):
    if new_color in COLOR_CODES:
        return render_template('hello.html', name=socket.gethostname(), color=COLOR_CODES[new_color])
    return "Invalid color", 400

@app.route('/read_file')
def read_file():
    file_path = "/data/testfile.txt"
    try:
        with open(file_path, "r") as f:
            contents = f.read()
        return render_template('hello.html', name=socket.gethostname(), contents=contents, color=COLOR_CODES.get(color, "#ffffff"))
    except FileNotFoundError:
        return "File not found", 404
    except Exception as e:
        return f"Error reading file: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
