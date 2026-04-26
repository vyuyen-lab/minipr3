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

    new_member = {
        'id': member_id,
        'name': name,
        'type': member_type,
        'months': months,
        'cost': cost
    }
    members.append(new_member)
    print(f"\n=> Thêm thành công hội viên: {name}!")
    return members

def display_members(members):
    """In danh sách hội viên dạng bảng căn lề."""
    print("\n" + "="*70)
    print(f"{'MÃ HV':<10} | {'TÊN HỘI VIÊN':<20} | {'GÓI TẬP':<10} | {'SỐ THÁNG':<10} | {'CHI PHÍ (VND)':<15}")
    print("-" * 70)
    
    if not members:
        print("Chưa có dữ liệu hội viên nào.")
    else:
        for m in members:
            print(f"{m['id']:<10} | {m['name']:<20} | {m['type']:<10} | {m['months']:<10} | {m['cost']:<15.0f}")
    print("="*70)

def sort_members(members):
    """Sắp xếp danh sách hội viên theo chi phí giảm dần."""
    if not members:
        print("\n=> Không có dữ liệu để sắp xếp.")
        return members
        
    def get_cost(member):
        return member['cost']
        
    members.sort(key=get_cost, reverse=True)
    print("\n=> Đã sắp xếp danh sách theo CHI PHÍ giảm dần!")
    display_members(members)
    return members

def advanced_search(members):
    """Tìm kiếm khớp một phần (chuỗi con) hoặc khớp ID."""
    keyword = input("\nNhập Mã ID hoặc một phần Tên hội viên: ").strip().lower()
    
    results = [m for m in members if (keyword == m['id'].lower()) or (keyword in m['name'].lower())]
    
    print("\n--- KẾT QUẢ TÌM KIẾM ---")
    if not results:
        print("=> Không tìm thấy kết quả nào phù hợp.")
    else:
        display_members(results)

def advanced_statistics(members):
    """Thống kê gom nhóm doanh thu theo Gói Tập."""
    if not members:
        print("\n=> Chưa có dữ liệu để thống kê.")
        return
        
    stats = {'VIP': {'count': 0, 'revenue': 0}, 'THUONG': {'count': 0, 'revenue': 0}}
    total_revenue = 0
    
    for m in members:
        g_type = 'VIP' if m['type'] == 'VIP' else 'THUONG'
        stats[g_type]['count'] += 1
        stats[g_type]['revenue'] += m['cost']
        total_revenue += m['cost']
            
    print("\n--- BÁO CÁO THỐNG KÊ NÂNG CAO ---")
    print(f"Tổng số hội viên : {len(members)} người")
    print(f"Tổng doanh thu   : {total_revenue:,.0f} VND\n")
    print("CHI TIẾT THEO NHÓM GÓI TẬP:")
    print(f"- Thẻ VIP    : {stats['VIP']['count']} hội viên | Doanh thu: {stats['VIP']['revenue']:,.0f} VND")
    print(f"- Thẻ THƯỜNG : {stats['THUONG']['count']} hội viên | Doanh thu: {stats['THUONG']['revenue']:,.0f} VND")


def main():
    filename = 'gym_data.json' 
    gym_members = load_data(filename) # Biến cục bộ, không dùng global
    
    while True:
        print("\n" + "*"*35)
        print(" HỆ THỐNG QUẢN LÝ PHÒNG GYM (PRO)")
        print("*"*35)
        print("1. Thêm hội viên mới")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm hội viên (Khớp một phần)")
        print("4. Sắp xếp theo chi phí")
        print("5. Thống kê theo nhóm (VIP/Thường)")
        print("6. Lưu dữ liệu (JSON) & Thoát")
        print("*"*35)
        
        choice = input("Mời bạn chọn chức năng (1-6): ")
        
        if choice == '1':
            gym_members = add_member(gym_members)
        elif choice == '2':
            display_members(gym_members)
        elif choice == '3':
            advanced_search(gym_members)
        elif choice == '4':
            gym_members = sort_members(gym_members)
        elif choice == '5':
            advanced_statistics(gym_members)
        elif choice == '6':
            save_data(gym_members, filename)
            print(f"\n=> Đã lưu cấu trúc JSON vào file '{filename}'. Tạm biệt!")
            break
        else:
            print("\n-> Lỗi: Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6.")

if __name__ == "__main__":
    main()