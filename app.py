import streamlit as st
import requests
import json

with open("countryCode.json") as f:
    data = json.load(f)

country_code_list = []

for obj in data:
    country_code_str = f"""{obj["dial_code"]} - {obj["name"]}"""
    country_code_list.append(country_code_str)

st.header(body="User details", divider="rainbow")
st.markdown(
    f"""<span style="word-wrap:break-word;">You can add user details below.</span>""",
    unsafe_allow_html=True,
)
st.write("##")


first_name = st.text_input(label="First name", placeholder="Ajay, Shubham")

last_name = st.text_input(label="Last name", placeholder="kumar, Singh")


country_code_value = st.selectbox("Select country code", country_code_list)

phone_no = st.text_input(label="Phone no", placeholder="9999999999, 7896999999")
st.write("##")

send_button = st.button(label="SEND", type="primary")


if send_button:

    parts = country_code_value.split(" - ")
    country_code = parts[0]

    user_infro = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_no": phone_no,
        "country_code": country_code,
    }
    st.write(user_infro)
    server_url = "https://afe9-2405-201-682c-6012-60c8-914c-e9a6-ac33.ngrok-free.app/twilio/makeCall"
    endpoint = "/user_info"

    try:
        response = requests.post(server_url, json=user_infro)
        st.success("Person info sent successfully!")
    except requests.RequestException as e:
        st.error(f"Error sending request: {e}")
