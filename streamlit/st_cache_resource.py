# 직렬화가 가능하고 데이터의 불변성이 필요한 경우에는 데이터 캐싱 메커니즘을 사용하는 것이 적합한 반면, 
# 직렬화할 수 없으며 결과를 전역적으로 공유해야 하는 경우에는 리소스 캐싱 메커니즘을 사용하는 것이 효율적입니다. 
# 따라서 복잡한 연산 결과를 재사용하려고 할 때에는 데이터 캐싱 메커니즘을 사용해야 하지만, 
# 프로그램 내에서 자원을 효율적으로 관리하고 싶을 때에는 리소스 캐싱 메커니즘을 사용해야 합니다

import streamlit as st
import time

#@st.cache_data
@st.cache_resource
def get_vocab_logits(param=None):
    print(f"get_vocab_logits({param}) starting")
    vocab_logits = param
    vocab_logits = {"나는": 0.01,"내일": 0.03,"오늘": 0.25,"어제": 0.3,
                    "산에": 0.4,"학교에": 0.5,"집에": 0.65,
                    "오른다": 1.2,"간다": 1.05,"왔다": 0.95}
    print(f"get_vocab_logits({param}) ending")    
    return vocab_logits

user_input = st.number_input(label="'나는'에 대한 로짓값을 입력하세요.", value=0.01)

st.write("# Bar Chart")
vocab_logits = get_vocab_logits()  #(1)함수의 결괏값을 복사하여 반환받음.
vocab_logits['나는'] = user_input  #(2)복사한 값을 변경함
vocab_logits = get_vocab_logits()  #(3)함수의 결괏값을 다시 복사하여 반환받음.
st.bar_chart(vocab_logits)
