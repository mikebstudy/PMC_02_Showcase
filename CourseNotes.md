# Course Notes 02.Showcase Project
- From Python Mega Course (by Ardit Sulce)
- Day 21-23 Project 2 Portfolio Showcase 

### Day 21
#### - L206 
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
