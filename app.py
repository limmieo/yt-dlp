from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"status": "error", "message": "URL is required"}), 400

    try:
        result = subprocess.run(
            ["yt-dlp", "--cookies", "ig_cookies.txt", "--dump-json", url],
            capture_output=True, text=True, check=True
        )
        info = json.loads(result.stdout)
        return jsonify({
            "status": "ok",
            "url": info.get("url"),
            "title": info.get("title"),
            "caption": info.get("description")
        })
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "details": e.stderr}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
