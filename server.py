from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/list", defaults={"filename": ""})
@app.route("/<path:filename>/list")
def list_files_from_Folder(filename):
    
    entries = os.listdir(os.path.join(".", filename))
    print(filename)
    print(entries)
    result = []

    for entry in entries:
        full_path = os.path.join(".", filename, entry)
        if os.path.isfile(full_path):
            result.append({"name": entry, "type": "file"})
        elif os.path.isdir(full_path):
            result.append({"name": entry, "type": "folder"})

    return jsonify(result)

@app.route("/", methods=["POST"], defaults={"filename":""})
@app.route("/<path:filename>", methods=["GET","POST"])
def serve_file(filename):
    if request.method == "GET":
        if (os.path.isfile(filename)):
            return send_from_directory(".", filename)
        else:
            return index()
    elif request.method == "POST":
        if 'file' not in request.files:
            return "Keine Datei gesendet", 400

        file = request.files['file']
        uploadFilename = file.filename or "upload.bin"
        path = os.path.join(filename, uploadFilename)
        file.save(path)
        return f"Datei gespeichert unter: {path}", 200      
         

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000, debug=True)
