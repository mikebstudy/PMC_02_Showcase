# Course Notes 02.Showcase Project
- From Python Mega Course (by Ardit Sulce)
- Day 21-23 Project 2 Portfolio Showcase 

### Day 21

#### L206 
- Case is made for using CSV file for data for this project
  - JSON is overkill and hard to edit
  - SQL is overkill and not needed because there are no dependencies between the projects as it concerns this project
- Also CSV file is semi-colon separated

### Day 22

#### L215
- Explains how to setup a virtual environment outside of PC
  - Open Terminal at desired directory location
  - python --version (to get current version)
  - py -3.12.6 -m venv .venv (can use any version you have installed)
- Also explains how to run code using that virtual environment
  - create text file
  - rename extension from .txt to .py
  - use code editor of choice to edit
  - to run
    - py -3.12.6 myfile.py
    - .venv\Scripts\python myfile.py
  - to run in pc
    - may need to delete .venv and create a new one in pc

### Day 23

#### L217
- To add sidebar for navigation menu
  - Add pages folder
    - Add py files for pages and name them the way they are to appear in the sidebar menu
      - Use Capitals as needed and underscores as spaces
  - Rename main.py as Home.py in the main folder

#### L219
- Create app password
  - Go to google settings  
    - In Search Box: step verification
      - Select 2-Step Verification (2nd or 3rd one)
        - Turn on, if not turned on
        - Add my phone number if needed
    - In Search Box: app passwords
      - Select App passwords
        - Enter app name: PMC_02_SHOWCASE_PW
        - Copy password for installation in program or environment variable

#### L220
- Connecting send_email.py to Contact_Me.py does not reference send_email.py correctly
  - [X] Fix needed. Tried to figure it out, but ran out of time
    - Fix was to rename course.C directory to course_C

#### L223
- Setup environment variable and password, doesn't work
  - password = os.getenv("PMC_02_SHOWCASE_PW") returns None
  - [X] Fix needed. Had to research and try .env file. 
    - Finally, got it to work with both local env variables and .env file
      - When using .env file use override=True to get load_env() to override Local Variable values
      - When using Local Variables, restart of PC is needed when a value is changed to see effect
  - Note .env file has password, but not saved in git repo
