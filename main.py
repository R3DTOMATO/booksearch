import streamlit as st
from streamlit_option_menu import option_menu
import bookname,writername

class MultiApp:
    def _init_(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title":title,
            "function":function
        })
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='책 검색',
                options=['책이름','작가']
            )    
        if app=='책이름':
            bookname.app()
        if app=='작가':
            writername.app()       
    run()