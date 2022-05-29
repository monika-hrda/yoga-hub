# Yoga Hub
_“You are only one yoga class away from a good mood.”_

The web application was built as my third milestone project for Code Institute's Full Stack Software Development course. It is a full-stack site that allows its users to store and manipulate data records about a yoga domain. The topic for the project was chosen because of my own yoga journey and those of my fellow yoga teachers in training. The app was designed with me/us using it in the future in mind. 

You can view the live website [here]( "Yoga Hub"). 
***
## User Experience (UX)

### Site Goals

* To provide a place for the yoga community (predominantly in Ireland) to come to to find classes being organised (online or in person) by various yoga teachers.
* To provide a place for yoga teachers to promote their own classes.

### User Stories

As a guest / not logged in user, I want to be able to:

* easily understand what the purpose of the website is.
* navigate the website easily, so that I can find any relevant content.
* view all classes posted on the website.
* find details of any class, as well as find out how to book the class I am interested in.
* search classes based on search terms of my choosing, so that I can find classes suited to me.
* contact the site administrator, so that I can ask any specific questions and get more information.
* view the website clearly on multiple devices, including my mobile device, so that I can achieve my other goals on the go.
* register on the website so that I can create and manage my own classes.

As a registered / logged in user, in addition to the above, I want to be able to:

* log into my account.
* view all classes created by me.
* add a new class.
* edit an existing class of mine.
* delete an existing class of mine.
* get visual feedback when an action on the site is completed.
* log out. 

### Planned Features

* Navigation menu on all pages - changes contents depending on user status
* Home page with information on the site purpose
* Classes displayed and searchable to all users
* User authentication (register, login, logout)
* Profile page listing the logged in user's classes
* CRUD functionality - class creation and management, limited to the class author
* 404 Error page navigating lost users back home
* Responsive design
* MongoDB to store information about users and classes

### User Journey

![user journey](docs/readme-img/user-journey.jpg)

### Wireframes

* Home page
![home page wireframe](docs/wireframes/home.png)

* Classes page
![classes page wireframe](docs/wireframes/classes.png)

* Classes page for logged in user
![classes page for logged in user wireframe](docs/wireframes/classes-logged-in-user.png)

* Register page
![register page wireframe](docs/wireframes/register.png)

* Login page
![login page wireframe](docs/wireframes/login.png)

* Profile page
![profile page wireframe](docs/wireframes/profile.png)

* Add Class page
![add class page wireframe](docs/wireframes/add-class.png)

* Edit Class page
![edit class page wireframe](docs/wireframes/edit-class.png)

* 404 page
![404 page wireframe](docs/wireframes/404.png)

### Design

* #### Colour Scheme

* #### Typography

* #### Imagery

***
## Development Process

* Trello Board has been used since the beginning of development to track progress, capture ideas, and make notes
![trello board](docs/readme-img/trello-board.jpg)

***
## Database Design

***
## Features

### Existing Features

### Features Left to Implement in the Future

***
## Technologies Used

### Languages Used

* HTML5
* CSS3
* JavaScript
* Python3

### Frameworks, Libraries & Programs Used

* [Heroku](https://heroku.com/) - to deploy the live site
* [MongoDB](https://www.mongodb.com/) - to host the database
* [Flask](https://flask.palletsprojects.com/en/2.1.x/) - micro web framework written in Python
* [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/) - to connect the app to MongoDB
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - extensible templating engine 
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.1.x/) - WSGI web application library
* [pip](https://pip.pypa.io/en/stable/) - to install dependencies for the site
* [dnspython](https://www.dnspython.org/) - DNS toolkit for Python
* [Git](https://git-scm.com/) - version control
* [GitHub](https://github.com/) - to store the code for this project
* [GitPod](https://www.gitpod.io/) - virtual IDE used to build this site
* [Materialize](https://materializecss.com/) - a responsive front-end framework based on Material Design
* [Font Awesome](https://fontawesome.com/) - to add icons to the site
* [jQuery](https://jquery.com/) - JavaScript library
* [Google DevTools](https://developer.chrome.com/docs/devtools/)
* [Balsamiq](https://balsamiq.com/wireframes/) - to create wireframes
* [Lucidchart](https://www.lucidchart.com/) - to create user journey (flowchart)
* [Trello](https://www.trello.com/) - to project manage, Kanban-style
* [https://imagecompressor.com/](https://imagecompressor.com/) - to compress image files
* [https://favicon.io/](https://favicon.io/favicon-converter/) - to generate favicon

***
## Testing

### Validator Testing

### User Stories Testing

### Continuous Testing - Issues and Resolutions to issues found during testing

During the development process, the application was continuously tested and bugs and issues that were found were resolved. A few examples:

* When a logged in user typed in url address looking to get to another user's profile, or the username in the typed url did not exist / user was deleted, they were still sent to their profile page (see the screenshot below). If the user was not logged in and typed a url aiming to get to a profile page, an internal server error was triggered. This was corrected by checking whether the username from the url exists, and whether it matches the username of the logged in user. The user was then redirected appropriately. See example of bug showing username in url not matching logged in user's username below:
![bug showing username in url not matching logged in user's username](docs/readme-img/profile-page-bug.jpg)

### Known Bugs and Issues

***
## Deployment

### Requirements for Deployment

* GitHub account
* Python
* MongoDB account
* Heroku account

### Heroku Deployment

This project was deployed on Heroku following these steps:

#### Requirements.txt and Procfile

Create these files using these steps in (GitPod) terminal:

1. Type `pip3 freeze -–local > requirements.txt` to create a requirements file (it keeps track of the Python dependencies that we've installed for our project)
2. Type `echo web: python3 run.py > Procfile` to create Procfile (a Heroku-specific type of file that tells Heroku how to run our project)
3. Delete any additional empty lines after the line `web: python app.py`
4. Push these two files into your depository

#### Environment Variables

Create an env.py file with the following information: 

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", " unique secret key")
os.environ.setdefault("MONGO_URI", " unique uri from mongodb ")
os.environ.setdefault("MONGO_DBNAME", " database name ")
```

As this file contains sensitive information, it needs to be added to the .gitignore file to not be pushed to GitHub

#### Create Heroku App

1. Log in to Heroku
2. Select 'Create New App' from the dashboard
3. Choose an app name (each name has to be unique, if app with that name exists already, a different name will have to be chosen)
4. Select the region based on your location
5. Click 'Create App'
6. Add config vars to Heroku - go to Heroku Settings tab, click on Reveal Config Vars, enter your above described environment variables
7. In your CLI install Heroku by typing `npm install -g heroku`

#### Deploying our App to Heroku

1. Login to Heroku by typing `heroku login -i`
2. Get your app name from Heroku by typing command `heroku apps`
3. Set the Heroku remote (replace the <app_name> with your actual app name): `heroku git:remote -a <app_name>`
4. Add, commit, and push to GitHub (commands `git add .` & `git commit -m "Deploy to Heroku via CLI"`)
5. Push to GitHub `git push origin main`
6. Push to Heroku `git push heroku main`
7. Your Heroku app will be built and you will see your deployed app's URL

### Forking the Repository

This project can be forked following these steps: 

1. Log in to GitHub and locate this project (you are most likely here). 
2. Locate the Fork button at the top right corner of the page and click on it. 
3. A copy of the original repository is in your GitHub account

### Local Clone

1. Navigate to this GitHub repository (you are most likely here)
2. Click on the Code dropdown
3. Copy the URL of the repository in the HTTPS tab
4. Use your IDE of choice to open its terminal
5. Change the current working directory to the location where you want the cloned directory
6. Type `git clone` and then paste the previously copied URL
7. Press enter to locate your local clone  

***
## Credits

### Code

* project is based on and developed from [Code Institute](https://codeinstitute.net/)'s walkthrough Flask Task Manager
* [Materialize documentation](https://materializecss.com/) with code snippets
* [Materialize on GitHub](https://github.com/Dogfalo/materialize)
* [MongoDB documentation](https://www.mongodb.com/docs/)
* [demo for how to use flask-paginate](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9)

### Content

Content written by Monika Hrda.

### Media

* all yoga related images sourced from [Pexels](https://www.pexels.com/)
* image used as favicon found on [PxHere](https://pxhere.com/)

### Acknowledgements

A big thank you to fellow Slackers from Code Institute's Slack channel for their support, advice, encouragement, and friendship.
