import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
import tempfile
import os
from pathlib import Path
import time

# 创建一个文件上传器
uploaded_file = st.file_uploader("选择一个Excel文件", type=["xlsx", "xls"])

if uploaded_file is not None:
    # 获取上传文件的文件名
    file_name = uploaded_file.name
    # 创建一个临时文件来处理上传的文件内容
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        tmp.write(uploaded_file.read())
        temp_file_path = tmp.name
    
    # 使用 pandas 读取 Excel 文件
    df = pd.read_excel(temp_file_path)

    # 指定D盘作为保存二维码图片的目标目录
    target_dir = Path('D:/') / Path(file_name).stem
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 遍历 A 列数据，为每一项生成二维码并保存到目标目录
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
        
        # 保存二维码图片到D盘的目标目录
        img_path = os.path.join(target_dir, f'qr_{index}.png')
        img.save(img_path)
        time.sleep(1)
        
    
    # 清理临时文件
    os.remove(temp_file_path)

    # 提示用户二维码已保存的位置
    st.success(f'二维码图片已保存至：{target_dir}')
