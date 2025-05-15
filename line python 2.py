import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("dataset.csv")

# Đổi tên cột cho nhất quán nếu cần
df.rename(columns={
    "Current_Job_Level": "Level",
    "Years_to_Promotion": "Years_to_Promotion",
    "Work_Life_Balance": "Work_Life_Balance"
}, inplace=True)

# Giao diện Streamlit
st.title("Average Work-Life Balance vs. Years to Promotion")
st.markdown("#### Select Job Level(s):")

# Dropdown để chọn nhóm hiển thị
levels = df["Level"].unique().tolist()
selected_levels = st.multiselect("Choose Level(s)", ["All"] + levels, default="All")

# Lọc dữ liệu
if "All" in selected_levels or not selected_levels:
    filtered_df = df.copy()
else:
    filtered_df = df[df["Level"].isin(selected_levels)]

# Tính giá trị trung bình cho từng tổ hợp
avg_df = filtered_df.groupby(["Years_to_Promotion", "Level"], as_index=False)["Work_Life_Balance"].mean()

# Vẽ biểu đồ
fig = px.line(
    avg_df,
    x="Years_to_Promotion",
    y="Work_Life_Balance",
    color="Level",
    markers=True,
    title="Average Work-Life Balance by Years to Promotion",
)

fig.update_layout(
    xaxis_title="Years to Promotion",
    yaxis_title="Average Work-Life Balance",
    legend_title="Job Level",
    template="plotly_white",
    height=500,
    width=900,
)

st.plotly_chart(fig, use_container_width=True)
