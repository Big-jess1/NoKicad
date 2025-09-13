
import streamlit as st

from streamlit_option_menu import option_menu

import about
import account
import home

st.set_page_config(page_title="Brief intro")

class MultiApp:
    def __init__(self):
       self.apps = []

    def add_app(self, title, function):
        self.apps.append({
        "title": title,
        "function": function
        })

    def run(self):
        # only the menu goes inside the sidebar
        with st.sidebar:
            app = option_menu(
                menu_title='Brief intro',
                options=['Home','Account','About'],
                icons=['house-fill','person-circle', 'trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'}, 
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "opx"},
                    "nav-link-selected":{"background-color": "#02ab21"},
                }
            )
            


            # This part controls what appears in the main body
        if app == 'Home':
                home.app()
        if app == 'Account':
                account.app()
        if app == 'About':
                about.app()


app = MultiApp()
app.run()                
        