import streamlit as st

def app():
    st.set_page_config(page_title="Welcome", layout="centered")

    st.markdown("""
        <style>
            .stApp {
                background-color: #f5f6f7; /* light ash / off-white color */
            }
            .main {
                background-color: white;
                padding: 2rem;
                border-radius: 10px;
                max-width: 800px;
                margin: auto;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            h1 {
                text-align: center;
                color: #333;
                font-family: 'Arial', sans-serif;
            }
            small {
                display: block;
                font-size: 0.7em;
                color: #666;
                margin-top: -10px;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="main">', unsafe_allow_html=True)

        st.markdown("<h1>Welcome to KiCad<br><small>(Video Demonstration on what I've learnt so far about KiCad)</small></h1>", unsafe_allow_html=True)
        st.subheader("🎥 Video Demonstration Part 1")
        st.video("video1.mp4", start_time=0)
        st.markdown("---")
        st.subheader("🎥 Video Demonstration Part 2")
        st.video("video2.mp4", start_time=0)

        st.markdown('</div>', unsafe_allow_html=True)