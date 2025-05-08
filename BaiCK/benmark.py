import matplotlib.pyplot as plt
import numpy as np

# Tên các phương pháp
methods = ['Heap Sort + PQ', 'Lọc cộng tác', 'Lọc theo nội dung']

# Dữ liệu gốc
response_time = [45, 120, 85]
precision = [0.82, 0.75, 0.79]
recall = [0.76, 0.68, 0.72]

# Chuẩn hóa thời gian phản hồi (vì nhỏ hơn là tốt hơn)
max_time = max(response_time)
min_time = min(response_time)
norm_time = [(max_time - t) / (max_time - min_time) for t in response_time]

# Chuẩn bị dữ liệu tổng hợp đã chuẩn hóa (0–1)
data = [
    [norm_time[0], precision[0], recall[0]],
    [norm_time[1], precision[1], recall[1]],
    [norm_time[2], precision[2], recall[2]]
]

# Tên các tiêu chí
labels = ['T.gian phản hồi', 'Độ chính xác', 'Độ bao phủ']
num_vars = len(labels)

# Góc chia đều cho radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # để khép kín hình

# Vẽ biểu đồ
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

for i, d in enumerate(data):
    values = d + d[:1]  # khép kín đa giác
    ax.plot(angles, values, label=methods[i])
    ax.fill(angles, values, alpha=0.25)

# Cài đặt trục
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
ax.set_title('So sánh các phương pháp theo Radar Chart')
ax.set_ylim(0, 1)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.show()
