<p align="center">
  <h1 style="font-size: 36px;">AUTOTRADER - A vehicle marketplace</h1>
</p>


<br>

* Autotrader is a vehicle marketplace platform designed for used cars, similar to CARSS. It allows users to create their own listing to sell their used car, 
* as well as search for used cars if they are looking to buy a car. Users can register for the website and gain access to more features such as saving their 
* favorite cars and following car dealerships to be aware of their latest inventory.
* The backend API of Autotrader is based on the Django REST framework, which serves the front-end part of the project by retrieving and storing data in the database.
*  The API is responsible for handling user authentication and authorization, managing user profiles and listings, and processing search queries

<br>


#### Links to the Frontend Project

 - Backend - Reposito
 - Backend - Deployment

+ [User Experience (UX)](#user-experience-ux)
- [User Stories](#user-stories)
- [Database Schema](#database-schema)
- [Features](#features)
     - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
     - [Languages and Frameworks Used](#languages-and-frameworks-used)
     - [Python Modules Used](#python-modules-used)
     - [Packages Used](#packages-used)
     - [Programs and Tools Used](#programs-and-tools-used)
- [Testing](#testing)
     - [Bugs](#bugs)
      - [Fixed Bugs](#fixed-bugs)
      - [Remaining Bugs](#remaining-bugs)
- [Deployment](#deployment)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
    - [Deploying with Heroku](#deploying-with-heroku)
- [Credits](#credits)
     - [Code](#code)
     - [Acknowledgements](#acknowledgements)



<br>
<br>

# User Stories

- The primary objective of the API is to establish seamless communication between the backend and frontend components, enabling the fulfillment of user stories exclusively designed for the frontend aspect of the project. Below, you will find a comprehensive inventory of the user stories specifically tailored for the frontend:

1. Improve the user registration process by implementing a user-friendly interface with clear instructions and error handling.
2. Enhance the login functionality by incorporating additional security measures, such as two-factor authentication and password encryption.
3. Develop a visually appealing homepage that showcases the project's key features and provides easy access to relevant information.
4. Create an intuitive navigation menu that enables users to effortlessly browse through different sections and functionalities of the application.
5. Implement a search feature that allows users to quickly find specific content or items within the application.
6. Design an interactive dashboard that provides users with personalized insights, statistics, and notifications based on their preferences and activities.
7. Enable users to customize their profile by adding profile pictures, personal information, and preferences.
8. Build a robust messaging system that enables users to communicate with each other, facilitating seamless collaboration and information exchange.
9. Integrate social media sharing options to allow users to share their achievements, content, or experiences with their social networks.
10. Optimize the application's performance and loading times by implementing efficient caching mechanisms and minimizing unnecessary data transfers.
   -[here](https://github.com/users/SuzanDewitz/projects/1/views/3)

- Tasks were successfully implemented during the API development process. To track and manage these tasks, we utilized a Kanban board specific to the project. The Kanban board provides a visual representation of the workflow, allowing us to monitor the progress of tasks and their respective stages. This board serves as a centralized location where you can find a comprehensive list of all the tasks associated with the API development.

  - [Kanban board](https://github.com/users/SuzanDewitz/projects/1/views/3)


<br>


## Database Schema
+ The database models for the project were created based on the schema below.


<br>





































![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **March 3rd, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!
