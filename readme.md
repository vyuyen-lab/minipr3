# DỰ ÁN QUẢN LÝ HỘI VIÊN PHÒNG GYM (CLI APPLICATION)

# Các tính năng cốt lõi 

Dự án đã hoàn thiện 100% các yêu cầu cơ bản và nâng cao:

1. Hệ thống Menu Điều hướng (Tiêu chí 1): Vòng lặp vô hạn `while True`, xử lý an toàn mọi thao tác nhập sai của người dùng.
2. Thêm & Xác thực dữ liệu (Tiêu chí 2):Sử dụng `try-except` bẫy lỗi nghiêm ngặt, ngăn chặn nhập chữ vào trường số (Chi phí, Số tháng) hoặc nhập số âm.
3. Hiển thị định dạng bảng (Tiêu chí 3):Sử dụng f-string căn lề chuẩn xác giúp báo cáo trực quan.
4. Sắp xếp (Tiêu chí 5):Sắp xếp danh sách giảm dần theo tổng chi phí.
5. Tìm kiếm & Thống kê Nâng cao (Tiêu chí 4 & 8):
   - Tìm kiếm linh hoạt: Khớp mã ID chính xác hoặc khớp một phần Tên hội viên (Substring match).
   - Thống kê gom nhóm: Tự động phân loại và tính tổng doanh thu riêng cho thẻ VIP và thẻ THƯỜNG.
6. Lưu trữ Cấu trúc JSON (Tiêu chí 7 & 9):Tự động xuất/nhập dữ liệu dưới định dạng `gym_data.json` đảm bảo tính toàn vẹn của cấu trúc (List of Dictionaries) thay vì txt thuần túy.

-Không sử dụng Biến Toàn Cục (No Global Variables): Dữ liệu `gym_members` được khởi tạo cục bộ trong hàm `main()` và truyền qua các tham số (parameters) vào các hàm con.
- Mã nguồn được module hóa, mỗi hàm chỉ đảm nhận đúng một vai trò duy nhất (nhập, xuất, tìm kiếm...).

# Chạy chương trình

1. Yêu cầu hệ thống:
- Máy tính đã cài đặt Python 3.6 trở lên.
- Không yêu cầu cài thêm thư viện bên ngoài (dùng thư viện `os` và `json` có sẵn của Python).

2. Cách chạy ứng dụng:
- Bước 1: Mở Terminal / Command Prompt tại thư mục chứa dự án.
- Bước 2: Chạy tệp lệnh chính bằng cú pháp:
  ```bash
  python main.py