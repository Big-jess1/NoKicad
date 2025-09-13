import streamlit as st

def app():
    # Page configuration
    st.set_page_config(page_title="USB-PCB Connector Design", layout="wide")

    # Custom CSS styles
    st.markdown("""
        <style>
            .stApp {
                background-image: url("https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg");
                background-size: cover;
                background-attachment: fixed;
            }
            .stApp::before {
                content: "";
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(255, 255, 255, 0.9); /* White overlay */
                z-index: 0;
            }
            .block-container {
                position: relative;
                z-index: 1;
                color: #000000;
            }
            .custom-header {
                font-size: 2.8rem;
                font-weight: bold;
                text-align: center;
                margin-top: 2rem;
                margin-bottom: 2rem;
                color: #000000;
            }
        </style>
    """, unsafe_allow_html=True)

    # Main content container
    with st.container():
        # Custom heading
        st.markdown('<div class="custom-header">👋 KiCad Concepts</div>', unsafe_allow_html=True)

        # Title
        st.title("How I Designed a USB-PCB Connector Using KiCad 9")

        # ========================
        # SECTION 1: Project Setup
        # ========================
        st.header("🔧 1. Project Setup")
        st.markdown("""
        - I began by installing **KiCad 9**, an open-source PCB design tool.
        - I created a new project and named it **`jesskicad`**.
        - This project was the foundation for my USB-PCB connector design.
        """)
       
        

        # =====================================
        # SECTION 2: Schematic Design (Editor)
        # =====================================
        st.header("🧩 2. Schematic Design (Schematic Editor)")
        st.markdown("""
        - I opened the **Schematic Editor** to start creating the electrical circuit.
        - I added basic components like:
            - Resistors
            - Diodes
            - Capacitors
            - D-Veneer (USB Connector)
        - Using the **Edit Symbol Properties** tool, I customized the components:
            - Changed their values
            - Assigned footprints
            - Added reference designators
        - I connected all components and added **power ports** to manage voltage and ground.
        """)
        st.text("📷 Schematic Snapshot")
        st.image("k.png", caption="USB-PCB Schematic Drawing", use_container_width=True)


        # ============================================
        # SECTION 3: Creating a Custom Symbol
        # ============================================
        st.header("🧠 3. Custom Symbol Creation (Symbol Editor)")
        st.markdown("""
        - I needed a **custom symbol** for my USB connector.
        - I opened the **Symbol Editor** and created a new symbol.
        - After saving it, I imported it into my schematic.
        - This step allowed me to tailor the symbol specifically to my design needs.
        """)
        st.text("📷 Symbol Editor Snapshot")
        st.image("k2.png", caption="USB-PCB Schematic Drawing", use_container_width=True)

        # ===================================
        # SECTION 4: PCB Layout (PCB Editor)
        # ===================================
        st.header("📐 4. PCB Layout (PCB Editor)")
        st.markdown("""
        - After completing the schematic, I moved to the **PCB Editor**.
        - I used the **"Update PCB from Schematic"** feature to transfer components.
        - Then, I:
            - Placed components neatly on the board
            - Routed traces between them
            - Optimized the layout for performance and manufacturing
        """)
        st.text("📷 PCB Editor Snapshot")
        st.image("k10.png", caption="USB-PCB Schematic Drawing", use_container_width=True)


        # =====================
        # Conclusion Section
        # =====================
        st.subheader("✅ Conclusion")
        st.markdown("""
        Using KiCad 9's powerful tools, I successfully designed a functional **USB-PCB connector**.

        Here's a quick recap of the tools I used:
        - **Schematic Editor**: For circuit diagram and connections
        - **Symbol Editor**: For creating custom parts
        - **PCB Editor**: For board layout and routing
        - **Footprint Editor** (indirectly via properties): For mapping symbols to real-world components

        The process helped me understand the full workflow of going from idea 💡 to layout 🧩 to final board 🖨️.
        """)
        st.video("3D v.mp4", start_time=0)

        # ========================
        # Media Section (Images/Video)
        # ========================
        
# Run the app
app()