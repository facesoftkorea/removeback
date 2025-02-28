import streamlit as st
from PIL import Image
from rembg import remove
import io


hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


footer="<style> your css code put here</style><div class='footer'><p>the word you want to tell<a style='display:block;text-align:center;' href='https://www.streamlit.io' target='_blank'>your email address put here</a></p></div>"

st.markdown(footer, unsafe_allow_html=True)


# Streamlit 앱 제목 설정
st.title("증명사진 배경 제거 및 보정")

# 파일 업로드 위젯
uploaded_file = st.file_uploader("얼굴 사진을 업로드하세요.", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 이미지 열기
    image = Image.open(uploaded_file)
    
    # 이미지 표시
    st.image(image, caption='업로드된 이미지', use_column_width=True)
    
    # 배경 제거
    st.write("배경 제거 중...")
    result = remove(image)
    
    # 배경 제거된 이미지 표시
    st.image(result, caption='배경 제거된 이미지', use_column_width=True)
    
    # 이미지를 BytesIO로 변환
    buf = io.BytesIO()
    result.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    # 다운로드 버튼
    st.download_button(
        label="배경 제거된 이미지 다운로드",
        data=byte_im,
        file_name="background_removed.png",
        mime="image/png"
    )
