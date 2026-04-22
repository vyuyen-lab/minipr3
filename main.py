# Các hàm chức năng (Sẽ viết code sau)
def add_member(members):
    pass

def display_members(members):
    pass

def search_member(members):
    pass

# Hàm điều phối chính
def main():
    gym_members = [] # Dữ liệu trung tâm (Biến cục bộ)
    
    while True:
        print("\n--- QUẢN LÝ PHÒNG GYM ---")
        print("1. Thêm hội viên")
        print("2. Xem danh sách")
        print("3. Thoát")
        
        choice = input("Chọn chức năng: ")
        
        if choice == '1':
            add_member(gym_members)
        elif choice == '2':
            display_members(gym_members)
        elif choice == '3':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

if __name__ == "__main__":
    main()