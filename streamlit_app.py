import streamlit as st
import tempfile
import os

# 创建一个文件上传器
uploaded_file = st.file_uploader("选择一个文件", type=["csv", "txt"])

if uploaded_file is not None:
    # 将上传的文件内容写入到一个临时文件中
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        temp_file_path = tmp.name
    
    # 显示临时文件的路径
    st.text(f"文件已保存到临时位置: {temp_file_path}")

    # 现在你可以使用 'temp_file_path' 像处理普通文件一样处理这个临时文件
    # 例如，你可以使用 open() 函数打开它
    # with open(temp_file_path, 'r') as f:
    #     data = f.read()
    
    # 不要忘记清理临时文件
    os.remove(temp_file_path)
