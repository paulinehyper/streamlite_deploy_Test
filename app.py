import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

#페이지기본설정
st.set_page_config(
    page_icon="",
    page_title="디터개의 스토리",
    layout="wide",

)

#페이지 헤더, 서브헤더 제목 설정

st.header("아엠웤킹에 오신걸 환영해요")
st.subheader("음성인식 시작하기")