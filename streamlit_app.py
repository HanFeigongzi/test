import io
import streamlit as st
import pandas as pd
import qrcode
from PIL import Image

# 创建一个文件上传器
uploaded_file = st.file_uploader("选择一个Excel文件", type=["xlsx", "xls"])

if uploaded_file is not None:
    # 使用 pandas 读取 Excel 文件
    df = pd.read_excel(uploaded_file)

    # 遍历 A 列数据，为每一项生成二维码并显示
    for index, row in df.iterrows():
        cell_value = str(row['A'])  # 假设 A 列的数据在列索引 'A'

        # 生成二维码
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(cell_value)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # 将图片保存为字节流
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # 显示二维码图片
        st.image(img_byte_arr, caption=f"QR Code for {cell_value}", use_column_width=True)
