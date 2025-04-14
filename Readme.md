# 02.Showcase Project
- From Python Mega Course (by Ardit Sulce)
- Portfolio like showcase project
- Day 21-23 Project 2 Portfolio Showcase 

- Three separate implementations 
  - course_C is from working the lessons
  - mikeb_M is enhanced implementation based on my own ideas and those of others on the internet
  - ChatGTP_A is experiments in generating code similiar to course.C and mikeb.M
  - (C,M,A - are the letters that proceed git commit comments and correspond to the respective implementations)

- Github repo: https://github.com/mikebstudy/PMC_02_Showcase
  - each implementation is in its own folder 

## course_C

### (Day22) Features added to Website bonus project
- Added extra space vertically between team boxes (write(&nbsp;))
- Calculated the number of rows for each column,so that extra team boxes would fill columns from left to right

### (Day23) Features added to Website bonus project
- Added ability to access .env file for setting environment variables
  - Works with both Local User Variables and .env file
  - test_T\testenv.py added for experimentation

## mikeb_M
- Started with final version of course_C
- [X] Add status to projects and display
- [X] Filter by status with checkboxes
- [X] Add numbers to project titles and reduce their size for readability
- [ ] Change columns to alternate rather than two long columns
- [ ] Use markdown to right justify status next to source code 

## Copilot_A
- Started with creating prompts in Prompt.md
- Second try worked well enough 
  - Several good enhancement ideas
    - Sidebar coding example
    - Sidebar maintenance of projects
    - markdown coding example for styling
    - sort and filter all the statuses and create checkbox for each
    - Two column alternating logic rather than two independent columns
  - Did not change the code to reflect the organization of the 'card' structure
  - Code could not read from a file. It used dictionary data instead.  

