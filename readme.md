#  MINI PROJECT: HỆ THỐNG QUẢN LÝ HỘI VIÊN PHÒNG GYM

##  Lựa chọn đề tài (Topic Selection)
- **Chủ đề:** Topic 12 - Gym Membership Management (Quản lý thẻ thành viên phòng Gym).
- **Phạm vi quản lý:** Hệ thống theo dõi hồ sơ của từng hội viên bao gồm các trường thông tin: `Mã hội viên`, `Tên hội viên`, `Gói tập (VIP/THƯỜNG)`, `Số tháng đăng ký`, và `Tổng chi phí`.

---

##  Kiến trúc và Lưu trữ dữ liệu
Dự án không sử dụng cơ sở dữ liệu phức tạp mà tổ chức lưu trữ trực tiếp thông qua cấu trúc bộ nhớ của Python và xuất ra tệp tin:

- **Trong bộ nhớ:** Dữ liệu toàn hệ thống được lưu trong một danh sách (`List`), mỗi phần tử là một từ điển (`Dictionary`) đại diện cho một hội viên.
- **Lưu trữ vật lý:** Hỗ trợ lưu song song dưới hai định dạng:
  - `gym.json`: Lưu trữ có cấu trúc chuẩn, giúp dễ dàng tái sử dụng và mở rộng (Tiêu chí nâng cao).
  - `gym.txt`: Lưu trữ dạng văn bản thuần túy theo định dạng phân tách bằng dấu phẩy (CSV format), đáp ứng tốt yêu cầu xuất báo cáo cơ bản.

---

##  Các tính năng cốt lõi 

Hệ thống cung cấp một Menu tương tác với 6 chức năng chính:

1. **Thêm hội viên mới (Input & Validation):** - Khởi tạo hồ sơ khách hàng. 
   - *Điểm nhấn:* Tích hợp cơ chế kiểm tra tính hợp lệ của dữ liệu (chặn số âm, chặn ký tự chữ vào trường số học) bằng khối lệnh `try...except`, đảm bảo hệ thống không bị crash.
2. **Hiển thị danh sách (Display):** - Trích xuất toàn bộ dữ liệu hiện có và in ra màn hình dưới dạng bảng biểu được căn lề chuẩn xác, dễ nhìn.
3. **Tìm kiếm thông minh (Advanced Search):** - Hỗ trợ tìm kiếm chính xác theo ID hoặc tìm kiếm chuỗi con (khớp một phần) theo Tên hội viên (Không phân biệt chữ hoa/chữ thường).
4. **Sắp xếp dữ liệu (Sort):** - Sắp xếp và vinh danh danh sách hội viên dựa trên mức chi phí đầu tư (thứ tự giảm dần).
5. **Thống kê nâng cao (Advanced Statistics):** - Tính toán tổng số lượng khách hàng và tổng doanh thu toàn hệ thống.
   - *Điểm nhấn:* Gom nhóm và đối chiếu số liệu chi tiết giữa 2 phân khúc khách hàng (Gói VIP và Gói Thường).
6. **Sao lưu & Thoát (File I/O):** - Đồng bộ hóa dữ liệu từ RAM xuống ổ cứng (vào cả 2 tệp `.json` và `.txt`) trước khi đóng chương trình, đảm bảo tính toàn vẹn của dữ liệu cho những lần khởi động sau.

---

## Hướng dẫn cài đặt và sử dụng
**Yêu cầu môi trường:** Đã cài đặt Python 3.x trên máy tính.

**Các bước chạy chương trình:**
1. Clone repository này về máy hoặc tải toàn bộ mã nguồn.
2. Mở Terminal / Command Prompt tại thư mục chứa dự án.
3. Chạy lệnh: `python main.py`
4. Sử dụng các phím số từ `1` đến `6` để điều hướng menu và nhập dữ liệu theo các chỉ dẫn trên màn hình.

---

## Đánh giá mức độ hoàn thành
Dự án đã đáp ứng toàn bộ các yêu cầu của bài tập lớn (Mini Project), bao gồm cả phần cơ bản và phần thử thách nâng cao:

- [x] Menu CLI hoạt động ổn định (1.0 đ)
- [x] Nhập liệu & Bẫy lỗi thành công (1.0 đ)
- [x] Định dạng bảng hiển thị rõ ràng (1.0 đ)
- [x] Tìm kiếm khớp một phần chuỗi (1.0 đ + Nâng cao)
- [x] Sắp xếp dữ liệu theo số học (1.0 đ)
- [x] Thống kê gom nhóm phân loại (1.0 đ + Nâng cao)
- [x] Đọc/ghi file TXT an toàn (1.0 đ)
- [x] Tích hợp cấu trúc lưu trữ JSON (1.0 đ + Nâng cao)
- [x] Mã nguồn dạng Modular, sử dụng Git & GitHub (1.0 đ)

**Mục tiêu kỳ vọng: 10/10 Điểm**

---

##  Thông tin 
- **Sinh viên thực hiện:** Đinh Thị Vy Uyên 
- **Ngành học:** Sư phạm Tin học
- **Học phần:** Phương pháp lập trình