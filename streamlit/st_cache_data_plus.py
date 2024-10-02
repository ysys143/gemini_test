# @st.cache_data 데코레이터를 사용할 때 한 가지 유의할 점이 있습니다. 
# @st.cache_data는 함수에 전달되는 파라미터와 구현 내용이 동일하다면 함수의 호출 결과 역시 항상 동일할거라는 가정 하에 캐싱 메커니즘을 적용한다고 설명했습니다. 
# 따라서 함수 내에서 데이터베이스에 접근하거나 네트워크 통신 등을 통해 그 결과가 변경되도록 코드가 구현되어 있다면 원하는대로 동작하지 않을 수 있다는 점을 알고 있어야 합니다.


# st_cache_data_plus.py
import streamlit as st
import time

total=0

@st.cache_data
def get_vocab_logits(param=0):
    print(f"get_vocab_logits({param}) starting")
    global total
    time.sleep(10)
    vocab_logits = {"나는": 0.01,"내일": 0.03,"오늘": 0.25,"어제": 0.3,
                    "산에": 0.4,"학교에": 0.5,"집에": 0.65,
                    "오른다": 1.2,"간다": 1.05,"왔다": 0.95}
    vocab_logits = {word: logit + param + total for word, logit in vocab_logits.items()}
    total +=1
    print(f"get_vocab_logits({param}) ending")    
    return vocab_logits

text = "마지막 레이어의 로짓값을 가정"
st.header(text, divider='rainbow')
st.subheader(text)
st.title(text)
st.write(text)

user_input = st.number_input(label="로짓값에 더해지는 숫자를 입력하세요.", value=0)

st.write("# Bar Chart")
st.bar_chart(get_vocab_logits(user_input))
st.caption(text)