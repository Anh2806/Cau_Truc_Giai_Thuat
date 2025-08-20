ĐỀ TÀI: TRIỂN KHAI THUẬT TOÁN HEAP SORT VỚI PRIORITY QUEUE CHO HỆ THỐNG ĐỀ XUẤT SẢN PHẨM

Bài báo nghiên cứu việc ứng dụng thuật toán Heap Sort và cấu trúc Priority Queue vào hệ thống đề xuất sản phẩm dựa trên các tiêu chí như đánh giá người dùng và mức độ phổ biến. Mục tiêu chính là đánh giá hiệu năng, độ phức tạp thời gian và không gian của cả hai phương pháp để lựa chọn cấu trúc tối ưu trong thực tế. Phương pháp nghiên cứu bao gồm xây dựng thuật toán, phân tích lý thuyết, và đánh giá thực nghiệm bằng cách sử dụng các ngôn ngữ lập trình phổ biến (Python). Kết quả thực nghiệm cho thấy Priority Queue có độ phức tạp thời gian tốt hơn Heap Sort, đặc biệt trong các tác vụ cần độ phản hồi nhanh. Nghiên cứu này góp phần cung cấp cơ sở lý thuyết và thực tiễn cho việc lựa chọn giải thuật phù hợp trong các ứng dụng thực tế như hệ thống đề xuất sản phẩm thương mại điện tử.

Đề tài làm về 1 ứng dụng sắp xếp theo đánh giá sản phẩm smart phone 

<img width="1034" height="787" alt="image" src="https://github.com/user-attachments/assets/e1608727-f203-45e4-b8b2-a8c00f7b3d87" />

[So Sanh 2 thuật toán]

<img width="573" height="528" alt="image" src="https://github.com/user-attachments/assets/75f546d9-ca9b-4df3-90e8-3b6c18fb4356" />

Chỉ tiêu	Heap Sort + PQ	Lọc theo nội dung	Lọc cộng tác	Nhận xét nhanh
T.gian phản hồi	1.0	≈ 0.5	≈ 0.05–0.1	Heap Sort + PQ phản hồi nhanh gấp ~2 lần so với “Lọc theo nội dung” và khoảng 10–20 lần so với “Lọc cộng tác”.
Độ chính xác	≈ 0.95–1.0	≈ 0.90	≈ 0.88	Chênh lệch nhỏ (dưới 10 %). Heap Sort + PQ gần như tối ưu độ chính xác hơn.
Độ bao phủ	≈ 0.78	≈ 0.75–0.77	≈ 0.74	Ba phương pháp gần tương đương; Heap Sort + PQ độ bao phủ cao hơn ~3–5 %. Nói lên Rẳng độ toàn diện của nó.

Phương pháp	Lý do nhanh/chậm
Heap Sort + PQ	Heap chỉ cỡ k → ít truy cập RAM, cache friendly.
Lọc theo nội dung	Tra cứu vector sẵn (TF IDF/embedding) → chỉ tốn k NN.
Lọc cộng tác	Xử lý ma trận người × mục lớn / cập nhật liên tục → nặng nhất.
________________________________________

Phương pháp	Hạn chế chính
Heap Sort + PQ	Cập nhật điểm số phải tái heap → kém với dữ liệu động.
Lọc theo nội dung	“Bong bóng lọc”, cần metadata tốt.
Lọc cộng tác	Cold start, chi phí tính toán cao.
