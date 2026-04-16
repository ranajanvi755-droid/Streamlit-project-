import streamlit as st
import datetime

#Title
st.title("🍽️ FOOD DELIVERY APP")
st.divider()

#Name input
fname = st.text_input("👤Enter your name", placeholder="First Name")
lname = st.text_input("", placeholder="Last Name")
if st.button("✅Submit"):
    st.write("🙋Your name is", fname, lname)
st.divider()

#Radio button
st.radio("Choose your gender",("Male","Female","Other"))
st.divider()

#selectbox
st.selectbox("📍Choose your city",("Vadodara","Surat","Ahemdabad","Bharuch"))
st.divider()

#Date of birth
DOB = st.date_input("select your DOB", datetime.date(2003, 4, 25))
st.divider()

#Multiselect
st.multiselect("🍜Choose your favorite cuisine",("Indian","Chinese","Italian","Mexican"))
st.divider()

#slider
st.slider("Choose how many times you order food in a week",min_value=0,max_value=10,value=1)
st.divider()

#Audio Massage
Audio_massage = st.audio_input("Record your message")
if Audio_massage:
    st.write("Message recorded succesfully")
    st.audio(Audio_massage)
st.divider()

# Create columns
# Food Section
st.subheader("🍕 Food Preference")

c1, c2 = st.columns(2)

with c1:
    st.markdown("### 🍔 Food Items")
    food_choice = st.multiselect("Choose food", ["Pizza", "Burger", "Pasta"])

with c2:
    st.markdown("### 🥤 Beverages")
    beverage_choice = st.multiselect("Choose beverage", ["Coke", "Juice", "Coffee", "Milkshake"])

#Text_area
st.text_area("Write your comment")

#Checkbox
agree = st.checkbox("I agree")

#Button

if st.button("🚀 Place Order"):
    if not fname or not lname:
        st.warning("⚠️ Please enter your name")
    elif not agree:
        st.error("❌ Please accept terms & conditions")
    elif not food_choice:
        st.warning("🍽️ Please select at least one food item")
    else:
        st.success(f"🎉 Order placed successfully, {fname}!")
        st.toast("🛍️ Your food is on the way 🚴‍♂️")
st.divider()
st.snow()




