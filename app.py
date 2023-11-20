import streamlit as st
from streamlit.components.v1 import html
import os
from genai_recommendations import *


# Initialize a session state to store the list from external resource file 
if 'text_list' not in st.session_state:
    st.session_state.text_list = temp_log_items
    
def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)



def main():
    st.title("Dimension Collaboration Log")

    # Text input for the user
    user_input = st.text_input("Enter your log input below:", key="user_input")

    # Adding this for convenience to copy same user issue for testing purposes
    st.write('''Temporary Placeholder: 'found a bug with the import issue icon - it doesn't look like the same size & also color looks a bit off. let's fix this pls' ''')
    
    if st.button("Submit"):
        # Check if the input is not empty and append it to the list
        if user_input:
            st.session_state.text_list.append(user_input)
            
            
            # LLM detect and display smart action
            rec = get_rec_category(user_input)
            tool = get_rec_tool(rec)
            if rec:
                col1, col2, col3 = st.columns([3,2,2])

                col1.header('Current User Log',)
                col2.header('Action')
                col3.header('Tool')

                with col1:
                    st.write(user_input)  # Displaying each text entry
                with col2:          
                    if rec:
                        st.success(f"{rec}")
                with col3:          
                    if tool:
                        st.success(f"{tool}")

         # Generic CSS formatting work around - can ignor this code!
        st.markdown("""
        <style>
            span[data-baseweb="tag"][aria-label="Create Issue, close by backspace"]{
                background-color: blue;
            }
            span[data-baseweb="tag"][aria-label="Schedule Meeting, close by backspace"]{
                background-color: green;
            }
            span[data-baseweb="tag"][aria-label="Project Management, close by backspace"]{
                background-color: wheat;
            }
        </style>
        """, unsafe_allow_html=True)
    
    
        # Generic multiselect widget - can ignor this code!
        options = st.multiselect("Which actions do you want to select:", ["Create Issue", "Schedule Meeting", "Project Management"], ["Create Issue", "Schedule Meeting", "Project Management"])
        st.write('You selected:', options[0])
    
    
    
    
    # Display all submitted previous user logs
    st.write("Previous Submitted User Logs:")
    col1, col2, col3 = st.columns([3,2,2])
    col1.header('Previous User Logs',)
    col2.header('Action')
    col3.header('Tool')

    for text in st.session_state.text_list:
        item = get_rec_category(text)
        tool = get_rec_tool(item)

        with col1:
            st.write(text)  # Displaying each text entry
        with col2:          
            if item != "No recommendation at this time!":
                st.success(f"{item}")
            else:
                st.success('No Category Found')
        with col3:          
            if tool:
                st.success(f"{tool}")
            else:
                st.success('No action Found')   
            
if __name__ == "__main__":
    main()