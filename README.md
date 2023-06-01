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

[View the live project here.](https://autotraderss-drf-backend.herokuapp.com/)

#### Links to the Frontend Project

 - Backend - Repository
 - Backend - Deployment

<br>

 ## Table of Contents

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

   - [User Stories 1 view here](https://github.com/users/SuzanDewitz/projects/1/views/3)
   - [User Stories 2 view here](https://github.com/SuzanDewitz/autotraderss-drf-backend/blob/main/docs/userstories.md)

- Tasks were successfully implemented during the API development process. To track and manage these tasks, we utilized a Kanban board specific to the project. The Kanban board provides a visual representation of the workflow, allowing us to monitor the progress of tasks and their respective stages. This board serves as a centralized location where you can find a comprehensive list of all the tasks associated with the API development.

  - [Kanban board](https://github.com/users/SuzanDewitz/projects/1/views/3)


<br>


## Database Schema
+ The database schema depicted below served as the foundation for creating the project's database models.
![dbschema](docs/dbschema.png)

<br>


## Future Features:

- Enhanced Search Options and Filters: Expand the search capabilities by incorporating additional options and filters based on various criteria.

- Buyer Rating System: Introduce a rating system to enable buyers to rate sellers, enhancing trust and credibility within the service.

- Location Algorithm: Implement an algorithm to facilitate location-based searches, enabling users to find cars and sellers within a specific distance.

- Image Gallery Functionality: Integrate an image gallery feature that empowers sellers to upload multiple pictures of the autotraders, providing a more comprehensive visual representation.

<br>

## Technologies Used
Languages and Frameworks Used
 - Python: [Python](https://www.python.org/)
 - Django 3.2.14: [Django 3.2.14](https://pypi.org/project/Django/3.2.14/)
 - Django Rest Framework 3.14.0: [Django Rest Framework 3.14.0](https://pypi.org/project/djangorestframework/3.14.0/)

<br>

## Python Modules Used
- Built-in Packages/Modules
  + [pathlib](https://docs.python.org/3/library/pathlib.html)- Used to work with filepaths.
  + [os](https://docs.python.org/3/library/os.html) - Provides a portable way of using operating system-dependent functionality.

<br>

## Packages Used
- External Python Packages
   + [cloudinary](https://pypi.org/project/cloudinary/) - Integration with Cloudinary for handling cloud-based media storage.
   + [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - Integration with Cloudinary for storage backend in Django.
   + [dj-database-url](https://pypi.org/project/dj-database-url/) - Allows the use of 'DATABASE_URL' environmental variable in the Django project settings file to connect to a PostgreSQL database.
   + [django-allauth](https://pypi.org/project/django-allauth/) - Set of Django application used for account registration, management and authentication.
   + [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) - API endpoints for handling authentication in Django Rest Framework.
   + [django-filter](https://pypi.org/project/django-filter/) - Application that enables dynamic QuerySet filtering based on URL parameters.
   + [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - JSON Web Token authentication backend for the Django REST Framework.
   + [django-cors-headers](https://pypi.org/project/django-cors-headers/) - Django app that adds Cross-Origin Resource Sharing (CORS) headers to responses.
   + [gunicorn](https://pypi.org/project/gunicorn/) - Python WSGI HTTP Server for hosting Django applications.
   + [Pillow](https://pypi.org/project/Pillow/) - Fork of PIL, the Python Imaging Library, providing image processing capabilities.
   + [psycopg2](https://pypi.org/project/psycopg2/) - Python PostgreSQL database adapter.
   + [python-dotenv](https://pypi.org/project/python-dotenv/) - Utility for setting key-value pairs from a .env file as environmental variables.

<br>

## Programs and Tools Used
[drawSQL](https://drawsql.app/)-  Used to create the Database Schema/ERD (Entity-Relationship Diagram) for the project.
[Gitpod](https://gitpod.io/workspaces)
Gitpod was utilized as the primary code editor for this project, providing a cloud-based development environment.
[Git](https://git-scm.com/)
Git was used for version control throughout the project. The terminal was utilized to commit changes to Git and push them to the project's repository.
[GitHub](https://github.com/)
 GitHub served as the remote repository for storing the project's code after it was pushed from Git. It provided collaboration features, issue tracking, and a centralized location for code hosting.

<br>

## Testing
- A separate document for testing can be found [here](https://github.com/SuzanDewitz/autotraderss-drf-backend/blob/main/TESTING.md).

## Bugs
### Fixed Bugs
Click here to view a list of fixed bugs that has been completed.
### Remaining Bugs
No known remaining bugs

<br>

## Deployment
### Forking the GitHub Repository
1.Go to [the project repository](https://github.com/SuzanDewitz/TableFinder)
2. In the right most top menu, click the "Fork" button.
3. There will now be a copy of the repository in your own GitHub account.

<br>

## Making a local clone
1. Go to [the project repository](https://github.com/SuzanDewitz/TableFinder)
2. Click on the "Code" button.
3. Choose one of the three options (HTTPS, SSH or GitHub CLI) and then click copy.
4. Open the terminal in you IDE program.
5. Type git clone and paste the URL that was copied in step 3.
6. Press Enter and the local clone will be created.

<br>

## Alternatively by using Gitpod:
1. Go to the project repository
2. Click the green button that says "Gitpod" and the project will now open up in Gitpod.

<br>

## Deploying with Heroku
I followed the below steps using the Code Institute tutorial:

The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies pip3 freeze --local > requirements.txt. Please note this file should be added to a .gitignore file to prevent the file from being committed.

1. Go to [Heroku.com](https://id.heroku.com/login) and log in; if you do not already have an account then you will need to create one.
2. Click the New dropdown and select Create New App.
3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4. Select the region you are working in.

<br>

### Heroku Settings
- You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.

1. In the Settings tab, click on Reveal Config Vars and set the following variables:
 + Key as ALLOWED_HOSTS and the value as the name of you project with '.herokuapp.com' appended to the end e.g. example-app.herokuapp.com. Click the Add button.
 + Key as CLOUDINARY_URL and the value as your cloudinary API Environment variable e.g. cloudinary://**************:**************@*********. Click the Add button.
  + Key as SECRET_KEY and the value as a complex string which will be used to provide cryptographic signing. The use of a secret key generator is recommended such as
  +  [django-secret-key-generator](https://miniwebtool.com/django-secret-key-generator/). Click the Add button.
  + Ensure the key DATABASE_URL is already populated. This should have been created automatically by Heroku.
  + The DATABASE_URL should be copied into your local .env, created during the cloning process.
  + To make authenticated requests to this API (e.g. from a fontend application) you are required to add the key CLIENT_ORIGIN with the value set as the URL you will be sending the authentication request from.
   + Additionally, a CLIENT_ORIGIN_DEV key can be set with the value of a development server (IP or URL) for use during local development.

<br>

## Heroku Deployment
In the Deploy tab:

1. Connect your Heroku account to your Github Repository following these steps:
    + Click on the Deploy tab and choose Github-Connect to Github.
    + Enter the GitHub repository name and click on Search.
    + Choose the correct repository for your application and click on Connect.
2. You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the Deploy Branch button whenever you want a change made.
3. Once you have chosen your deployment method and have clicked Deploy Branch your application will be built and you should now see the View button, click this to open your application.

<br>
<br>

## Credits

## Online resources
 - [Django Documentation](https://docs.djangoproject.com/en/3.2/)
 - [Django REST Documentation](https://www.django-rest-framework.org/)
 - [Python Documentation](https://docs.python.org/3/)

<br>

## Code
 - Code Institute DRF Tutorial Project, used through as a basis for the creation of this API
   + CREDIT: Code Institute DRF-API Tutuorial Project
   + URL: https://github.com/Code-Institute-Solutions/drf-api

<br>

## Acknowledgements
The tutor support team at Code Institute for their support.
My Code Institute Mentor for feedback and suggestions.
The Code Institute Slack community.



























