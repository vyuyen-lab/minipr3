import os
import json

# FILE JSON (TIÊU CHÍ 9)

def load_data(filename):
    """Đọc dữ liệu từ file JSON. Trả về mảng rỗng nếu file chưa tồn tại."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(members, filename):
    """Lưu toàn bộ dữ liệu vào file JSON với định dạng thụt lề chuẩn."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(members, file, ensure_ascii=False, indent=4)

def add_member(members):
    """Thêm hội viên với cơ chế bẫy lỗi nhập liệu (try-except)."""
    print("\n--- THÊM HỘI VIÊN MỚI ---")
    member_id = input("Nhập Mã HV (VD: G01): ").strip().upper()
    name = input("Nhập Tên HV: ").strip()
    member_type = input("Nhập Gói Tập (Thuong/VIP): ").strip().upper()
    
    while True:
        try:
            months = int(input("Nhập số tháng đăng ký: "))
            if months <= 0:
                print("-> Lỗi: Số tháng phải lớn hơn 0.")
                continue
            break
        except ValueError:
            print("-> Lỗi: Vui lòng nhập một số nguyên (VD: 3, 6, 12)!")

    while True:
        try:
            cost = float(input("Nhập tổng chi phí (VND): "))
            if cost < 0:
                print("-> Lỗi: Chi phí không được là số âm.")
                continue
            break
        except ValueError:
            print("-> Lỗi: Vui lòng nhập số hợp lệ!")