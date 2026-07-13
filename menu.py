import os
import sys

def menu():
    os.system('clear')  # hoặc 'cls' nếu dùng Windows
    print("\n" + "="*50)
    print("  ROBLOX_EGOR V2 - MENU CHÍNH")
    print("="*50)
    print("[1] 🚀 Chạy Google Phishing")
    print("[2] 📋 Xem log đã lấy")
    print("[3] 🗑️ Xóa log")
    print("[4] ❌ Thoát")
    print("="*50)
    
    choice = input("Chọn: ")
    
    if choice == '1':
        os.system('python app.py')
    elif choice == '2':
        if os.path.exists('log.txt'):
            os.system('cat log.txt')
        else:
            print("Chưa có dữ liệu.")
        input("\nNhấn Enter để tiếp tục...")
        menu()
    elif choice == '3':
        os.system('rm -f log.txt')
        print("Đã xóa log.")
        input("Nhấn Enter để tiếp tục...")
        menu()
    elif choice == '4':
        sys.exit()
    else:
        print("Lựa chọn không hợp lệ.")
        input("Nhấn Enter để tiếp tục...")
        menu()

if __name__ == '__main__':
    menu()
