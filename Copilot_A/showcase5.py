import streamlit as st

# Data structure
projects = [
    {
        "title": "Todo App",
        "status": "Done",
        "description": "A distraction-free web app to help you focus on creating and completing tasks.",
        "url": "https://github.com/mikebstudy/PMC_01_ToDoList.git",
        "image": "1.png"
    },
    {
        "title": "Portfolio Website",
        "status": "Doing Extra",
        "description": "A website built entirely in Python to showcase coding projects and apps.",
        "url": "https://pythonhow.com",
        "image": "2.png"
    },
    {
        "title": "PDF Templates",
        "status": "Started",
        "description": "A script that generates PDF templates of multiple pages given some predefined guidelines.",
        "url": "https://pythonhow.com",
        "image": "3.png"
    },
    {
        "title": "PDF Invoices",
        "status": "Not Started",
        "description": "A script that reads invoice records from Excel files and automatically generates PDF invoices.",
        "url": "https://pythonhow.com",
        "image": "4.png"
    },
    {
        "title": "Positive News Site",
        "status": "Not Started",
        "description": "A website that gets data from a news API and uses sentiment analysis to publish only positive news.",
        "url": "https://pythonhow.com",
        "image": "5.png"
    }
]

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f0f5;
        font-family: 'Arial', sans-serif;
    }
    .card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-bottom: 20px;
    }
    .card-title {
        font-size: 1.5em;
        font-weight: bold;
        color: #333333;
    }
    .card-status {
        font-size: 1.1em;
        font-weight: 600;
        margin-bottom: 10px;
        color: #4CAF50;
    }
    .card-description {
        font-size: 1em;
        color: #555555;
    }
    .card-button {
        background-color: #4CAF50;
        color: white;
        padding: 5px 10px;
        border: none;
        border-radius: 5px;
        text-decoration: none;
        font-size: 1em;
    }
    .card-button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("🌟 Project Showcase")

# Two-column layout for displaying projects
col1, col2 = st.columns(2)

# Display each project in a card-like design
for i, project in enumerate(projects):
    column = col1 if i % 2 == 0 else col2
    with column:
        st.markdown(f"""
            <div class="card">
                <div class="card-title">{project["title"]}</div>
                <div class="card-status">Status: {project["status"]}</div>
                <div class="card-description">{project["description"]}</div>
                <a class="card-button" href="{project["url"]}" target="_blank">Visit Project</a>
            </div>
        """, unsafe_allow_html=True)

        # Display image
        if project["image"]:
            st.image("images/" + project["image"], caption=project["title"], use_column_width=True)
