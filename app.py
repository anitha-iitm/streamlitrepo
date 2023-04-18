import streamlit as st
import pandas as pd
st.set_page_config(page_title="Find Largest of 3 munbers")
st.write("""
# Application to find largest number
""")
#Get Input

st.header('User Input numbers')
def user_input_features():
    number1 = st.number_input("NUMBER1",min_value=-20000,max_value=400000 ,step=1)
    number2 = st.number_input("NUMBER2",min_value=-20000,max_value=400000 ,step=1)
    number3 = st.number_input("NUMBER3",min_value=-20000,max_value=400000 ,step=1)
    
    
    data = {'NUMBER1': number1,
            'NUMBER2': number2,
            'NUMBER3': number3
            }
    features = pd.DataFrame(data, index=[0])
    return features
df = user_input_features()
if (df['NUMBER1'][0] >= df['NUMBER2'][0]) and (df['NUMBER1'][0] >= df['NUMBER3'][0]):
   largest=df['NUMBER1'][0]
elif (df['NUMBER2'][0] >= df['NUMBER1'][0]) and (df['NUMBER2'][0] >= df['NUMBER3'][0]):
   largest=df['NUMBER2'][0]
else:
   largest=df['NUMBER3'][0]
st.subheader('LargestNumber')
st.write('Largest of 3 numbers is:')
st.write(largest)

