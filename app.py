import streamlit as st
import requests

st.header(body="User details", divider="rainbow")
st.markdown(
    f"""<span style="word-wrap:break-word;">You can add user details below.</span>""",
    unsafe_allow_html=True,
)
st.write("##")


first_name = st.text_input(label="First name", placeholder="Ajay, Shubham")

last_name = st.text_input(label="Last name", placeholder="kumar, Singh")

phone_no = st.text_input(label="Phone no", placeholder="9999999999, 7896999999")
st.write("##")

send_button = st.button(label="SEND", type="primary")


if send_button:
    user_infro = {
        "first_name": first_name,
        "last_name_part1": last_name,
        "phone_no": phone_no,
    }
    st.write(user_infro)
    server_url = "http://localhost:3001"
    endpoint = "/user_info"

    try:
        response = requests.post(server_url + endpoint, json=user_infro)
        if response.status_code == 200:
            st.success("Person info sent successfully!")
        else:
            st.error(f"Failed to send person info.")
    except requests.RequestException as e:
        st.error(f"Error sending request: {e}")
