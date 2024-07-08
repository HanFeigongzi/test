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

    # 创建一个空列表来存储二维码图片的字节流
    qr_images = []

    # 遍历 A 列数据，为每一项生成二维码
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

        # 添加到列表
        qr_images.append(img_byte_arr)

    # 为每张图片创建下载按钮
    for i, img_bytes in enumerate(qr_images):
        st.download_button(
            label=f"下载二维码图片 {i + 1}",
            data=img_bytes,
            file_name=f"qr_code_{i + 1}.png",
            mime="image/png"
        )
