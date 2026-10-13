from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def home():
    return "WZH 2 APK Generator API is Running!"

@app.route('/api/generate-apk', methods=['POST'])
def generate_apk():
    app_name = request.form.get('app_name', 'MyWeb2App')
    website_url = request.form.get('url', '')
    html_file = request.files.get('html_file')

    if website_url:
        return jsonify({
            "status": "success",
            "type": "url",
            "message": f"'{website_url}' লিংক থেকে '{app_name}' এর APK তৈরির কাজ শুরু হয়েছে!"
        }), 200

    elif html_file:
        file_path = os.path.join(UPLOAD_FOLDER, html_file.filename)
        html_file.save(file_path)
        return jsonify({
            "status": "success",
            "type": "file",
            "message": f"'{html_file.filename}' ফাইল থেকে '{app_name}' এর APK তৈরির কাজ শুরু হয়েছে!"
        }), 200

    else:
        return jsonify({
            "status": "error",
            "message": "দয়া করে কোনো ওয়েবসাইট লিংক অথবা HTML ফাইল প্রদান করুন!"
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
