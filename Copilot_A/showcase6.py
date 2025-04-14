import streamlit as st

# Initial data structure
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
    }
]

# App title
st.title("🌟 Dynamic Project Management")

# Sidebar for management options
st.sidebar.header("Manage Projects")

# Add Project
if st.sidebar.button("Add Project"):
    st.session_state.show_add_form = not st.session_state.get("show_add_form", False)

if st.session_state.get("show_add_form", False):
    with st.sidebar.form(key="add_form"):
        new_title = st.text_input("Title")
        new_status = st.text_input("Status")
        new_description = st.text_area("Description")
        new_url = st.text_input("URL")
        new_image = st.text_input("Image Filename")
        if st.form_submit_button("Add"):
            projects.append({
                "title": new_title,
                "status": new_status,
                "description": new_description,
                "url": new_url,
                "image": new_image
            })
            st.sidebar.success("Project added successfully!")

# Edit and Delete Projects
selected_project = st.sidebar.selectbox("Select a Project to Edit or Delete", [p["title"] for p in projects])

if st.sidebar.button("Edit Project"):
    st.session_state.show_edit_form = not st.session_state.get("show_edit_form", False)

if st.session_state.get("show_edit_form", False):
    selected = next((p for p in projects if p["title"] == selected_project), None)
    if selected:
        with st.sidebar.form(key="edit_form"):
            selected["title"] = st.text_input("Title", selected["title"])
            selected["status"] = st.text_input("Status", selected["status"])
            selected["description"] = st.text_area("Description", selected["description"])
            selected["url"] = st.text_input("URL", selected["url"])
            selected["image"] = st.text_input("Image Filename", selected["image"])
            if st.form_submit_button("Save"):
                st.sidebar.success("Project updated successfully!")

if st.sidebar.button("Delete Project"):
    projects = [p for p in projects if p["title"] != selected_project]
    st.sidebar.success(f"Deleted '{selected_project}'!")

# Display Projects
col1, col2 = st.columns(2)
for i, project in enumerate(projects):
    column = col1 if i % 2 == 0 else col2
    with column:
        st.subheader(project["title"])
        st.write(f"**Status:** {project['status']}")
        st.write(f"**Description:** {project['description']}")
        st.write(f"[Visit here]({project['url']})")

        if project["image"]:
            st.image("images/" + project["image"], caption=project["title"], use_column_width=True)
