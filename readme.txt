Welcome to "mysite" this is a web space for me to learn various skills required
    for full stack development with django.

Skills I have learned through this project include.
    Web design: css, html
    Databases: sqlite, postgres
    Hosting: digital ocean, nameservers
    Coding: python, javascript
    Version control: Github, git

Things I want to do with the website
    -:HOMEPAGE:-
    This will be wholy unimportant app but simply set up so that a visitor to the site is greeted with a simple "This site is currently
        under contstruction."
    Will be where the index links to. Does not need any HTML rather a simple view with some text. At a later date the home page may
        become something of a navigation hub or it may simply be removed and the home index set to my CV. 
    -:CV:-
    Change the font so that it is much cleaner and thinner. User more 
        capitalization.
    Create a logo. Initially probablly just TA.
    Brainstorm in text or on paper what I actually want to include in my CV.
        Remember to keep it focused on my skills at the top. I can defend myself
        and prove knowledge of these skills at an interview. 

    -:BLOG:-
    Proof all of the articles that I have already written. 
    Create a blog site that inherits off the main site for the design. 
    Create a way to add blog articles through the admin page. The coding with
        mitch tutorials are probably a great way to go about this. 

    -:HRMS:-
    Look at the different features that you would actually use in an HRMS and 
        make one that you would actually really like to use.
    Create different users with different permissions. Keep this simple.
        Admin: All abilities
        Managers: All abilities for those in their teams
        Staff: Mostly view only
    
    -:FLASH-READER:-
    This will be my way of reading an article in spanish or similar and easily 
        creating ANKI flashcards as I read through the article and encounter
        difficulties. 
    Visitors would create an account which would be linked to the database. 
    As I want it to be based within my own website then I would have it so that
        a visitor would paste the article into a reader on the webpage. 
    
    -:WORKOUT-TRACKER:-
    This will be a way of recording my workouts as well as visualising the 1RM based point system that I have been using through excel.
    
How to deploy this website
    The deployed version of the website will be the master branch. 
    New developments will be part of a working branch for each individual app in the mysite django project. 
    When I am happy with a working branch and that it is ready to deploy I will merge it with the master branch. 
        1. log into the server and git pull the master branch. 
        2. Change settings.py to dissallow 127.0.0.1 and set debug to false
        3. Run "python manage.py collectstatic"
        4. reload gunicorn

Little Details I want to improve
    Add a little image to the tab section in the browser.
    Add CAA so that I get an A rating for security for the website instead of a B
        
