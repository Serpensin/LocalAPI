import json
import tkinter as tk
import os
import sys
from flask import Flask
from tkinter import filedialog, simpledialog


app = Flask(__name__)

@app.route('/<file>')
def send_json(file):
    filename = f'{file}.json'
    try:
        with open(os.path.join(path_to_json_files, filename)) as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        return f"{filename} not found", 404
    return data

if __name__ == '__main__':
    if len(sys.argv) < 2:
        root = tk.Tk()
        root.withdraw()
        path_to_json_files = filedialog.askdirectory(title="Select folder containing JSON files")
        print(path_to_json_files)
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
