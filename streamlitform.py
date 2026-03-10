import streamlit as st
import time
import smtplib
from email.mime.text import MIMEText

# --- EMAIL SENDING FUNCTION ---
def send_email_to_kiran(user_data):
    # Eikhane apnar details bosaun
    sender_email = "your-email@gmail.com"  # Apnar Gmail id
    receiver_email = "your-email@gmail.com" # Jekhane mail jete chan (same hote pare)
    app_password = "xxxx xxxx xxxx xxxx"    # 16 digit Google App Password

    subject = f"New Student Registration: {user_data['Name']}"
    
    body = f"""
    Hello Kiran, 
    Ekjon notun student form fill-up koreche. Details niche dewa holo:
    
    Full Name    : {user_data['Name']}
    Education    : {user_data['Education']}
    Stream       : {user_data['Stream']}
    Mobile       : {user_data['Mobile']}
    Email ID     : {user_data['Email']}
    Institute    : {user_data['Institute']}
    City/District: {user_data['City']}
    Time         : {user_data['Time']}
    """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# --- UI & LOGIC ---
st.set_page_config(page_title="KIRAN.DATA Portal", page_icon="🎓")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Screen 1: Login
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #1877f2;'>Portal Login</h1>", unsafe_allow_html=True)
    with st.container():
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            name = st.text_input("Full Name")
            password = st.text_input("Password", type="password")
            if st.button("SUBMIT"):
                if name and password:
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Please enter Name and Password")

# Screen 2: Registration Form
else:
    st.markdown("<h2 style='text-align: center; background-color: #1877f2; color: white; padding: 10px;'>WELCOME TO MY PAGE</h2>", unsafe_allow_html=True)
    st.subheader("Student Registration Form")
    
    with st.form("reg_form"):
        f_name = st.text_input("Full Name")
        edu = st.selectbox("Education Qualification", ["Madhyamik", "HS", "Graduation", "Masters", "PhD"])
        
        # Dynamic Stream Selection
        stream = ""
        if edu == "HS":
            stream = st.selectbox("Select Stream", ["Science", "Arts", "Commerce"])
        elif edu == "Graduation":
            stream = st.selectbox("Select Department", ["B.Sc", "B.A", "B.Tech", "B.Com"])
        else:
            stream = st.text_input("Specialization/Subject")

        f_mob = st.text_input("Mobile Number")
        f_email = st.text_input("Email ID")
        f_inst = st.text_input("Institute Name")
        f_city = st.text_input("City/District")
        
        submitted = st.form_submit_button("GENERATE REPORT & SEND EMAIL")
        
        if submitted:
            # Data dictionary to send
            data_to_send = {
                "Name": f_name,
                "Education": edu,
                "Stream": stream,
                "Mobile": f_mob,
                "Email": f_email,
                "Institute": f_inst,
                "City": f_city,
                "Time": time.strftime("%H:%M:%S")
            }
            
            # Show a loading spinner while sending email
            with st.spinner("Sending data to Kiran's Email..."):
                if send_email_to_kiran(data_to_send):
                    st.success("Registration Complete! Details sent to Email.")
                    st.balloons()
                else:
                    st.error("Email send failed! Please check App Password.")
