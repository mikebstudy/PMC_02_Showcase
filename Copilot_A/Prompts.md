# Prompts for Copilot

## Experimental test prompts

### Initial setup

- I want to generate some code. Can you receive a folder structure of data?
  - Could not receive data structures
- Can you receive data files for my coding session?
  - Cannot receive files
  - Asks for description of data structure
- (Here is a sample of the data.)
  - 4 rows of data.csv pasted
- What coding languages do you work with?
  - Several listed. Python first
- Let's code in Python
  - simple_sample.py generated and tried

### First try
- Generate a web application for the prior data structure.
  - Generated code. Placed in showcase.py
  - Does not run, however
- MediaFileStorageError: Error opening '1.png'
  - Gave instructions to correct.
  - Followed adding path before file name. It worked.
- Make the display 2 columns
  - Provided a good nested solution that alternates between the two columns. Maybe use same logic in mikeb_M verwion. Resizes well.
- Add status filter using checkboxes
  - At this point, Copilot provided a response, but also asked to sign in. 
    - Sign up was done and the session was lost, with the code.

### Second try
- Here is the code from the previous chat
  - Code provided from version prior to adding filter status boxes
  - Response made several good suggestions:
    - Filtering Projects: Add a dropdown or search bar to filter projects by their status or title.
    - Interactive Features: Let users rate or vote for the projects they like most.
    - Styling Enhancements: Use custom CSS or Streamlit themes to make your app more visually appealing.
    - Dynamic Project Management: Allow users to add, edit, or delete projects directly within the app.
- Filter projects by status
  - Solution used a dropdown box
- Use checkboxes for filtering
  - Solution provided that filters through status
- Update the dictionary based on the following csv text
  - Updated the data to have 5 lines rather then 3
  - Code works
- Make styling enhancements
  - Solution used 'markdown' method and css
- Dynamic Project Management
  - Code a little buggy
  - Provided 'sidebar' coding logic for maintenance
  - Dropped 'status' checkbox logic