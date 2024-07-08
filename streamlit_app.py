import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
import tempfile
import os

# 创建一个文件上传器
uploaded_file = st.file_uploader("选择一个Excel文件", type=["xlsx", "xls"])

if uploaded_file is not None:
    # 将上传的文件内容写入到一个临时文件中
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        tmp.write(uploaded_file.read())
        temp_file_path = tmp.name
    
    # 使用 pandas 读取 Excel 文件
    df = pd.read_excel(temp_file_path)

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
        
        # 在 Streamlit 中显示二维码图片
        st.image(img)
    
    # 清理临时文件
    os.remove(temp_file_path)
