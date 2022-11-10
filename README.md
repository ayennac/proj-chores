# ChoreBuddy

ChoreBuddy is a web app that uses the principles of body doubling and community to help users finish their chores.  A way that I kept sane and on top of my chores during the pandemic was to do it with my friends over Zoom. If they weren’t around, I would put on a random youtube video of someone doing chores and I’d just do it with them. 


## Features
To watch a demo of the app, [![watch this youtube video](https://img.youtube.com/vi/3MLRlw7La2M/default.jpg)](https://youtu.be/3MLRlw7La2M). 

A user has two main functions on ChoreBuddy which are to either watch videos or to submit a video doing chores to the public video repository. An admin user has the ability to delete and moderate videos sent into the public video repository. 

## Tech Stack

- Python
- Flask
- Jinja
- PostgreSQL
- SQL Alchemy

- JavaScript
- HTML
- CSS
- Bootstrap

## APIs Used
Cloudinary API

## Installation 
To run ChoreBudy on your own machine: 

Fork this repo:  

`git clone https://github.com/ayennac/proj-chores.git`

Create and activate a virtual environment inside your ChoreBuddy directory:  

`$ virtualenv`
`$ source env/bin/activate`

Install the dependencies:  

`pip3 install -r requirements.txt`

Sign up for [Cloudinary API](https://cloudinary.com/) and save your Cloudinary Key and Cloudinary Secret in a `secrets.sh` file 

Source your keys form secrets.sh into your virtual environment:  

`source secret.sh`

Set up the database:  

`createdb images`
`python3 seed_database.py`

Run the app:  

`python3 server.py`

You can now navigate to 'localhost:5000/' to access ChoreBuddy

## Known Bugs
- [ ] It takes a LONG time for videos to upload to the Cloudinary API
- [ ] The app is deployed on AWS, but the service comes down intermittently.


## ChoreBuddy 2.0 Next Steps
- [ ] Work through bugs listed above 
- [ ] Build out the admin functions   
- [ ] Create a tagging system so that users can filter and view certain types of chore videos


