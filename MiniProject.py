# import the streamlit library
import streamlit as st
# give a title to our app
st.title('Welcome to our BMI calculator')
#Take the weight input in kg
weight = st.number_input('Enter your weight (in kg)')
# Take the height input
# radio button to choose height format status = st.radio('Select your height format :, ('cms', 'metres', 'feet'))
status = st.radio('Select your height format :', ('cms', 'metres', 'feet'))
# Take height input in centimetres:
if (status == 'cms'):
    height = st.number_input('Centimetres')

    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text('Enter some value of height')

#Take height input in metres
elif (status == 'metres'):
    #take height input in metres
    height = st.number_input('Metres')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text('Enter some value of height')

# take height input in Feet :
else:
    height = st.number_input('Feet')
    # 1 meter = 3.28
    try:
        bmi = weight / (((height / 3.28)) ** 2)
    except:
        st.text('Enter some value of height')

# check if the button is pressed or not
if(st.button('Calculate BMI')):

    # Print the BMI index
    st.text('Your BMI Index is {}.'.format(bmi))

#Give the interpretation of the BMI Index
    if (bmi< 16):
        st.error("You're extremely underweight")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You're underweight")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("You're healthy")
    elif (bmi >= 25 and bmi < 30):
        st.warning("You're overweight")
    elif (bmi >= 30):
        st.error("You're extremely overweight")
