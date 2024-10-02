# st_cache_data.py
import streamlit as st
import time

# 스트림릿에서는 캐싱 매커니즘을 제공합니다. 스트림릿의 @st.cache_data 데코레이터를 사용하면 함수를 실행한 결과가 캐시에 보관됩니다. 
# 이후부터는, 파라미터가 달라졌거나 구현 내용이 달라진 경우에 한해서만 함수를 다시 실행합니다. 
# 만일 함수의 코드가 변경되지 않았고, 이전에 호출된 파라미터와 동일하다면, 캐시에 보관되어 있는 결과를 반환함으로써 불필요한 재실행을 막습니다.
@st.cache_data
def get_vocab_logits(param=0):
    print(f"get_vocab_logits({param}) starting")
    time.sleep(10)
    vocab_logits = {"나는": 0.01,"내일": 0.03,"오늘": 0.25,"어제": 0.3,
                    "산에": 0.4,"학교에": 0.5,"집에": 0.65,
                    "오른다": 1.2,"간다": 1.05,"왔다": 0.95}
    vocab_logits = {word: logit + param for word, logit in vocab_logits.items()}
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
