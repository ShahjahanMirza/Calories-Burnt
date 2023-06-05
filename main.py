import pandas as pd
import pickle
import streamlit as st
import numpy as np

st.title('Calculate Your Burnt Calories')

model = pickle.load(open('calories_burnt_model.pkl', 'rb'))

# background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/2803160/pexels-photo-2803160.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url() 
# till here

# look at the data
df = pd.read_csv('calories_burnt.csv')
df.Gender = df.Gender.apply(lambda x: 'male' if x == 1 else 'female')
st.dataframe(df.head(5))
# till here

# input columns
col1, col2, col3 = st.columns(3)

with col2:
    
    cola, colb,colc = st.columns(3)
    with colb:
        sex = st.radio('Gender',('male','female'))
        if sex == 'male': Gender = 1
        else: Gender = 0
        
with col1:
    Age = st.number_input('Age',0)
with col2:
    Height = st.number_input('Height',0.0)
with col3:
    Weight = st.number_input('Weight',0.0)

with col1:
    Duration = st.number_input('Duration',0)
with col2:
    Heart_Rate = st.number_input('Heart_Rate',0)
with col3:
    Body_Temp = st.number_input('Body_Temp',0.0)
# till here    

# input for prediction
values = np.array([Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]).reshape(1,-1)

if st.button('Predict'):    
    pred = round(model.predict(values)[0], 2)
    st.write("""
            ### Calories Burnt : {}🔥 """.format(str(pred)))
    st.balloons()
# till here