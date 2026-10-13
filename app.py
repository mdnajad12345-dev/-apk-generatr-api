from flask import Flask, request, jsonify, send_file
import os
import zipfile

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def home():
    return "WZH 2 APK Generator API is Running & Ready!"

@app.route('/api/generate-apk', methods=['POST'])
def generate_apk():
    app_name = request.form.get('app_name', 'MyWeb2App')
    website_url = request.form.get('url', '')
    html_file = request.files.get('html_file')

    # ডেমো হিসেবে একটি জেনেরিক APK ফাইল তৈরি বা রিটার্ন করার লজিক
    # বাস্তব ক্ষেত্রে এখানে Android SDK / Gradle দিয়ে APK বিল্ড করার প্রসেস বা টেমপ্লেট APK এডিট করতে হবে।
    output_apk_name = f"{app_name.replace(' ', '_')}.apk"
    output_apk_path = os.path.join(OUTPUT_FOLDER, output_apk_name)

    # যদি আসল APK ফাইল ব্যাকএন্ডে বিল্ড করা না থাকে, তবে একটি স্যাম্পল ফাইল বা সাকসেস রেসপন্স পাঠানো যায়
    # বর্তমানে টেস্টের জন্য একটি ডেমো রেসপন্স পাঠানো হচ্ছে যাতে অ্যাপে ডাউনলোড লিংক পাওয়া যায়
    
    if website_url or html_file:
        # এখানে APK জেনারেট হয়ে গেলে সেটির পাথ রিটার্ন করতে হবে
        # উদাহরণস্বরূপ, আমরা একটি রেসপন্সে ডাউনলোড লিংক দিচ্ছি:
        download_link = f"https://apk-generatr-api-uoui.onrender.com/download/{output_apk_name}"
        
        # ডেমো ফাইল তৈরি করে রাখা (যদি ফাইল না থাকে)
        with open(output_apk_path, "w") as f:
            f.write("Dummy APK Content for testing")

        return jsonify({
            "status": "success",
            "message": "APK সফলভাবে জেনারেট হয়েছে!",
            "download_url": download_link
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "দয়া করে লিংক অথবা HTML ফাইল প্রদান করুন!"
        }), 400

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "ফাইল পাওয়া যায়নি!", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
