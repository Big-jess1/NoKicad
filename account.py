import streamlit as st

def app():
    st.markdown("""
        <style>
            .stApp {
                background-image: url("https://picsum.photos/1600/900");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                position: relative;
            }

            .stApp::before {
                content: "";
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(255, 255, 255, 0.7);
                z-index: 0;
            }

            .appview-container, 
            .block-container {
                position: relative;
                z-index: 1;
                background: transparent !important;
            }
                    
                /* 🔥 Make all text bold and black */
            html, body, .stApp, .block-container, .appview-container {
                color: #000000 !important;
                font-weight: 600;
            }

            /* Optional: style input labels */
            label {
                color: #000000 !important;
                font-weight: bold;
        </style>
    """, unsafe_allow_html=True)

    st.title('Welcome, Please fill in your Login Details.')
    st.write("Welcome to the Account section of  app.")

    choice = st.selectbox('Login/signup', ['Login','Sign up'])
    if choice =='Login':

        st.text_input('Email Address')
        st.text_input('Password', type='password')

        st.button('Login')


    
    else:

        email=st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        username = st.text_input('Enter your unique username')
        st.button('create my account')
    
  

