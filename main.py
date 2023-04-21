import json
import tkinter as tk
import os
import sys
from flask import Flask, render_template_string
from tkinter import filedialog, simpledialog


app = Flask(__name__)


@app.route('/')
def show_files():
    path = app.config['PATH_TO_JSON_FILES']
    files = [f for f in os.listdir(path) if f.endswith('.json')]
    with open(os.path.join(app.static_folder, 'index.html')) as f:
        html = f.read()
    return render_template_string(html, files=files, current_path=path)

@app.route('/<path:path>')
def get_json_file(path):
    path = os.path.join(app.config['PATH_TO_JSON_FILES'], f'{path}.json')
    if os.path.isfile(path) and path.endswith('.json'):
        with open(path) as f:
            data = json.load(f)
            return data
    else:
        return f"{path} not found or not a valid JSON file", 404


if __name__ == '__main__':
    if len(sys.argv) < 2:
        root = tk.Tk()
        root.withdraw()
        path_to_json_files = filedialog.askdirectory(title="Select folder containing JSON files")
        if not path_to_json_files:
            print("No folder selected. Exiting.")
            sys.exit(1)
        port = simpledialog.askinteger("Port", "Enter port number:", initialvalue=5000)
        if not port:
            print("No port specified. Exiting.")
            sys.exit(1)
    else:
        path_to_json_files = sys.argv[1]
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 5000

    app.config['PATH_TO_JSON_FILES'] = path_to_json_files
    app.run(debug=False, port=port)
