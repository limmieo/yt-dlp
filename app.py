from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes

@app.route('/api', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"status": "error", "message": "URL is required"}), 400

    try:
        result = subprocess.run(
            ["yt-dlp", "-g", url],
            capture_output=True, text=True, check=True
        )
        download_url = result.stdout.strip()
        return jsonify({"status": "ok", "url": download_url})
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "details": e.stderr}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
