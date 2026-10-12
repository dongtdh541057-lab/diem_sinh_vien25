import pandas as pd
import matplotlib.pyplot as plt

# 1. Tạo dữ liệu 10 sinh viên
data = {
    "Họ và Tên": [
        "Đỗ Thị Ngọc Cầm",
        "Nguyễn Thị Mỹ Duyên",
        "Nguyễn Xuân Dự",
        "Trương Đình Hải Đông",
        "Nguyễn Tuấn Hào",
        "Nguyễn Dũ Hào",
        "Đặng Anh Hạo",
        "Võ Văn Quy",
        "Nguyễn Thanh Việt",
        "Nguyễn Thị Trúc Mai"
    ],
    "Chuyên cần": [9, 8, 7, 6, 9, 8, 5, 7, 6, 10],
    "Giữa kỳ": [8, 7, 6, 7, 9, 8, 8, 7, 6, 9],
    "Cuối kỳ": [9, 8, 7, 8, 9, 7, 5, 8, 6, 10]
}

df = pd.DataFrame(data)

# 2. Tính điểm tổng kết
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
).round(2)

# 3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 4. Hiển thị bảng điểm đầy đủ
print("BẢNG ĐIỂM 10 SINH VIÊN")

cot_hien_thi = [
    "Họ và Tên",
    "Chuyên cần",
    "Giữa kỳ",
    "Cuối kỳ",
    "Tổng kết",
    "Xếp loại"
]

print(df[cot_hien_thi].to_string(index=False))

# 5. Thống kê điểm

# Tính Điểm trung bình của lớp
diem_trung_binh = df["Tổng kết"].mean()
print("\nĐiểm tổng kết trung bình của lớp:", round(diem_trung_binh, 2))

# Tìm sinh viên có điểm tổng kết cao nhất
sv_cao_nhat = df.loc[df["Tổng kết"].idxmax()]
print("\nSinh viên có điểm tổng kết cao nhất:")
print("Họ và tên:", sv_cao_nhat["Họ và Tên"])
print("Điểm tổng kết:", sv_cao_nhat["Tổng kết"])

# Tìm sinh viên có điểm tổng kết thấp nhất
sv_thap_nhat = df.loc[df["Tổng kết"].idxmin()]
print("\nSinh viên có điểm tổng kết thấp nhất:")
print("Họ và tên:", sv_thap_nhat["Họ và Tên"])
print("Điểm tổng kết:", sv_thap_nhat["Tổng kết"])

# Dếm số sinh viên đạt
so_sinh_vien_dat = (df["Tổng kết"] >= 5).sum()
print("\nSố sinh viên đạt:", so_sinh_vien_dat)

# 6. Vẽ biểu đồ điểm tổng kết
plt.figure(figsize=(12, 6))

plt.barh(df["Họ và Tên"], df["Tổng kết"])

plt.title("BIỂU ĐỒ ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
plt.xlabel("Điểm tổng kết")
plt.ylabel("Họ và tên sinh viên")
plt.xlim(0, 10)
plt.gca().invert_yaxis()

for i, diem in enumerate(df["Tổng kết"]):
    plt.text(diem + 0.1, i, f"{diem:.2f}",
             va="center")

plt.tight_layout()
plt.show()




import streamlit as st

st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 12px; margin-top: 30px; padding: 10px; border-top: 1px solid #dddddd;">
        Người tạo ứng dụng: Trương Đình Hải Đông<br>
        MSSV: 054208001057
    </div>
    """,
    unsafe_allow_html=True
)