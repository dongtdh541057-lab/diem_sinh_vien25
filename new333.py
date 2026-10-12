import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Hiển thị tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu 10 sinh viên
data = {
    "Họ và Tên": [
        "Đỗ Thị Ngọc Cầm",
        "Nguyễn Thị Mỹ Duyên",
        "Nguyễn Xuân Dự",
        "Trương Đình Hải Đông",
        "Nguyễn Tuấn Hào",
        "Nguyễn Dũ Hào",
        "Đặng Anh Hạo",
        "Trần Thùy Trang",
        "Nguyễn Thanh Việt",
        "Nguyễn Thị Trúc Mai"
    ],
    "Chuyên cần": [9, 8, 7, 6, 6, 8, 6, 9, 6, 10],
    "Giữa kỳ": [8, 7, 6, 7, 9, 8, 8, 9, 6, 9],
    "Cuối kỳ": [9, 8, 7, 8, 9, 7, 7, 10, 6, 10]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
).round(2)

# Xếp loại sinh viên
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

cot_hien_thi = [
    "Họ và Tên",
    "Chuyên cần",
    "Giữa kỳ",
    "Cuối kỳ",
    "Tổng kết",
    "Xếp loại"
]

# 2. Hiển thị bảng điểm của 10 sinh viên
st.subheader("📋 Bảng Điểm Chi Tiết 10 Sinh Viên")
st.dataframe(df[cot_hien_thi], use_container_width=True)

# 3, 4, 5. Hiển thị thống kê (Điểm trung bình lớp, Cao/Thấp nhất, Số sinh viên đạt)
st.subheader("📊 Thống Kê Tổng Quan")
col1, col2, col3, col4 = st.columns(4)

diem_trung_binh = df["Tổng kết"].mean()
so_sinh_vien_dat = (df["Tổng kết"] >= 5).sum()
sv_cao_nhat = df.loc[df["Tổng kết"].idxmax()]
sv_thap_nhat = df.loc[df["Tổng kết"].idxmin()]

with col1:
    st.metric("Điểm TB Lớp", f"{diem_trung_binh:.2f}")
with col2:
    st.metric("Số Sinh Viên Đạt", f"{so_sinh_vien_dat}/10")
with col3:
    st.metric("Cao Điểm Nhất", f"{sv_cao_nhat['Tổng kết']}đ", sv_cao_nhat["Họ và Tên"])
with col4:
    st.metric("Thấp Điểm Nhất", f"{sv_thap_nhat['Tổng kết']}đ", sv_thap_nhat["Họ và Tên"])

st.markdown("---")

# 6 & 7. Tạo danh sách xổ xuống (Selectbox) và hiển thị thông tin chi tiết khi chọn sinh viên
st.subheader("🔍 Tra Cứu Điểm Chi Tiết Theo Sinh Viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df["Họ và Tên"])

# Lọc dữ liệu của sinh viên được chọn
student_info = df[df["Họ and Tên" if "Họ and Tên" in df.columns else "Họ và Tên"] == selected_student].iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.metric("Chuyên cần", student_info["Chuyên cần"])
with c2:
    st.metric("Giữa kỳ", student_info["Giữa kỳ"])
with c3:
    st.metric("Cuối kỳ", student_info["Cuối kỳ"])
with c4:
    st.metric("Tổng kết", student_info["Tổng kết"])
with c5:
    st.metric("Xếp loại", student_info["Xếp loại"])

st.markdown("---")

# 8. Hiển thị biểu đồ cột điểm tổng kết của 10 sinh viên
st.subheader("📈 Biểu Đồ Cột Điểm Tổng Kết")
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.barh(df["Họ và Tên"], df["Tổng kết"], color="skyblue")
ax.set_title("BIỂU ĐỒ ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Họ và tên sinh viên")
ax.set_xlim(0, 10)
ax.invert_yaxis()

for i, diem in enumerate(df["Tổng kết"]):
    ax.text(diem + 0.1, i, f"{diem:.2f}", va="center")

plt.tight_layout()
st.pyplot(fig)

# --- PHẦN FOOTER CÁ NHÂN CỦA BẠN ---
st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 12px; margin-top: 30px; padding: 10px; border-top: 1px solid #dddddd;">
        Người tạo ứng dụng: Trương Đình Hải Đông<br>
        MSSV: 054208001057
    </div>
    """,
    unsafe_allow_html=True
)