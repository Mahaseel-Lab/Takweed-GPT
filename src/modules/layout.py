import streamlit as st

class Layout:
    
    def show_header(self, types_files):
        """
        Displays the header of the app
        """
        st.markdown(
            f"""
            <h1 style='text-align: center;'> مساعد تكويد يعمل بالذكاء الاصطناعي لمساعدتك في التعرف اكثر من خلال  ملفاتك    ! 😁</h1>
            """,
            unsafe_allow_html=True,
        )

 