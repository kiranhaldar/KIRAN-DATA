import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="KIRAN.DATA - Student Portal", page_icon="🎓")

# Custom CSS for modern look
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #1877f2;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Application State for Login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- SCREEN 1: LOGIN ---
def login_page():
    st.markdown("<h1 style='text-align: center; color: #1877f2;'>Portal Login</h1>", unsafe_allow_html=True)
    
    with st.container():
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            name = st.text_input("Full Name")
            mob = st.text_input("Mobile Number")
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            
            if st.button("SUBMIT"):
                if name and password:
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Please fill Name and Password!")

# --- SCREEN 2: DASHBOARD / FORM ---
def dashboard_page():
    st.markdown("<h2 style='text-align: center; background-color: #1877f2; color: white; padding: 10px;'>WELCOME TO MY PAGE</h2>", unsafe_allow_html=True)
    
    st.subheader("Student Registration Form")
    
    with st.form("registration_form"):
        f_name = st.text_input("Full Name")
        
        edu = st.selectbox("Education Qualification", 
                           ["Select", "Madhyamik", "HS", "Graduation", "Masters", "PhD"])
        
        # Dynamic Stream Selection
        stream = ""
        if edu == "HS":
            stream = st.selectbox("Select Stream", ["Science", "Arts", "Commerce", "Vocational"])
        elif edu == "Graduation":
            stream = st.selectbox("Select Department", ["B.Sc", "B.A", "B.Tech", "MBBS", "B.Com"])
        elif edu in ["Masters", "PhD"]:
            stream = st.selectbox("Select Specialization", ["Computer Science", "Physics", "History", "Mathematics"])
            
        f_mob = st.text_input("Mobile Number")
        f_email = st.text_input("Email ID")
        f_pass = st.text_input("Secure Password", type="password")
        f_inst = st.text_input("Institute Name")
        f_city = st.text_input("City/District")
        
        submitted = st.form_submit_button("GENERATE REPORT & SUBMIT")
        
        if submitted:
            st.success("Registration Complete!")
            # Terminal output logic
            print("\n" + "="*40)
            print(f"NEW STUDENT: {f_name}")
            print(f"EDUCATION: {edu} - {stream}")
            print(f"CONTACT: {f_mob} | {f_email}")
            print("="*40)
            
            # Displaying on Screen
            st.info(f"Data Saved for {f_name} at {time.strftime('%H:%M:%S')}")

# Routing
if not st.session_state.logged_in:
    login_page()
else:
    dashboard_page()