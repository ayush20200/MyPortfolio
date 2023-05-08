import streamlit as st
from PIL import Image

# Set page title
st.set_page_config(page_title="My Portfolio")

# Set page layout
col1, col2 = st.columns([1, 3])

# Image
from PIL import Image
img = Image.open("ayush.png")
st.image(img)

# Add description
st.write("""
    # About Me
    ### Name : Ayush Dadwe
    #### Seeking a challenging role as a Programmer where i can utilize my skills in programming language such as python, as well as my experience in developing Web applications, to contribute the growth of the company while continuing to enhance my programming skills.
    """)



# Add skills
st.write("""
    # Education
    ## College 
    #### S.B. Jain Institute of Technology, Management & Research (7.5 cgpa)

    ## School 
    #### Mahatma Gandhi High School (X, 83.40 %)
    ####  Nityanand Junior College (XII, 70.77 %)
    """)


# Add skills
st.write("""
    # Skills
    #### * C Programming
    #### * C++ Programming
    #### * Core Java
    #### * Python Programming
    #### * Web Development 
    #### * MySQL Database
    """)

# Add projects
st.write("""
    # Projects
    ## Project 1
    #### Title        : Hotel Management System
    #### Role         : Project Leader 
    #### Languages    : Python, MySQL Database 
    #### Softwares     : Visual Studio Code, SQLite 3
    """)

st.write("""
    # Contact Details 
    #### * eMail       : ayushdadwe7@gmail.com
    #### * LinkedIn    : @ayushdadwe23
    #### * Contact No. : 7219791929
    #### * Address     : Nagpur
    """)