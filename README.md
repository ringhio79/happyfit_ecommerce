# Lay-Z-Gym

*Ecommerce Web Application with User Authentication and Stripe payments and subscription options. 

The web app is designed with a fictious small fitness company in mind. The objective is to have an online presence and also enable customers to purchase services directly online.  It can easily be adapted to the use for personal trainsers who would also like to advertise their services but dont have a physical service location.  

## Live Link 
The web app has been deployed on Heroku and may be accessed by clicking on this link https://ringhio79-lay-z-gym.herokuapp.com/
 
## UX

The website would be used by fitness clients.  The web app offers various levels of access depending on the type of authentication and registration level:

- Not authenticated: I can browse for information on the services provided but no account information or purchasing options are provided.  Must log in for further options and information
-
- Authenticated:  I can browse the website for information on the services provided and prices but cannot effect any purchases.  My account button will give me information about how to complete my registration and become a member.
-
- Basic Registration: I can browse the website, buy a subscription or purchase class packs/special event tickets for personal use as well as additional guests. I can view my account details on the 'account' page, including past bookings (if any).

- Subscripbed user: I can get information on all classes and events.  Scheduled classes are free but I have the option to purchase tickets to special events for personal use and for additional guests.  I can also view and manage my account from the 'account' page. 


This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

The application is built with three apps, Home, Accounts and Events.  The accounts app handles the features related to authentication, membership and subscription while the Events app handles the events and services provided by the company.

### Home app

- The Home app is used to render pages that are generic to the application i.e. Home, About Us and the Custom-Error html pages.

### Accounts app
- User login: allows users to create a log in account using just username, email and password.  Users are given the option whether they want to complete the regisgtration process immediately or return to it at a later stage.

- Registration/Profile - by completing the registration process the user also provides their payment details.  The payment details are sent to Stripe which in turn returns a Stripe ID.  The Stripe ID is stored in the user's profile but not credit card details are kept in the database. 

- Automated payments:  The Stripe ID enables the user to make purchases automatically without having to fill in payment details for every transaction.

- Subscriptions: A registered user can sign up for a yearly subscription or monthly subscription.  This is done by using the Stripe ID to take payments on a yearly or monthly basis respectively.  Subscription details are also visible in the accounts page. Subscription information is accessed via the Stripe API.

### Events app
- Events: Events can be created via the django admin panel.  An event represents a service, group-class package or special event, which users can purchase tickets for.  Each event has a capacity which will determine the maximum no. of tickets that can be purchased for an event.

- Tickets:  Tickets can be purchased directly online by registered users.  The number of tickets available for an event is displayed in the events details page.  A user can also purchase tickets for guests in which case they must provide guests' details before confirming their purchase. Tickets are linked to a booking via a booking reference no. 

- Bookings:  Bookings are created at point of purchase together with the tickets.  These are linked to each other with the use of foreign keys.  A booking history can be viewed in the 'account' page.

### Filter by Category

- And additional featur available on the Events list page is the Filter by Category. The filter feature was implemented using the django filter library by creating a filter.py using the Event model and category field and then using the filter in the events_list function in views.py.  This allows users to filter the events by the predifined categories rather than using a text search thereby making it easier to find relevant events.

### Conditional Views

The web app is designed to display information depending on the type of user who  is logged in.  The pages which use conditional viewing are based on user type are:
- Subscription
- Event Details
- Account

Further details on the content displayed for each user type can be found in the supportingdocuments folder.

### Potential expansion
The web app is complete as per the required featurs however there is room for expansion if desired. As the company grows it may wish to allow intructors to have access to manage their events.

- Instructors app - Instructors would have privilidged access to be able to create their own events, review tickets sold, participants etc. 

## Technologies Used

### Frameworks
- [Django Web Framework](https://www.djangoproject.com/)
    - to creating the base web framework, templates
- [Bootstrap](https://getbootstrap.com/)
    - to create additional layout and styling features as well as responsive features using javascript components
- [Bootswatch Flatly Theme](https://bootswatch.com/3/flatly/)
    - used to provide a themed html components to be used and customised as necessary

### Languages
- [Python3](https://www.python.org/)
    - to create functionality, render templates write to database
- HTML & CSS
    - to create layout and styling of front end

### Databases
- [SQLite Database](https://www.sqlite.org/index.html)
    - used in dev environment
- [PostgreSQL Database](https://www.postgresql.org/)
    - used in prod environment

### Libraries
- [Bootstrap forms](https://django-bootstrap-form.readthedocs.io/en/latest/)
    - used to display forms
    - 
- [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - used to give flexibility in presenting forms

## Testing

### Automated testing

Some automated tests have been to the Accounts and Home App. These can be found in the tests.py file respectively.  To run the tests open the terminal and enter the command:

`$ python manage.py test <app name>`

This will return a PASS for 4 tests:

**Accounts** - ProfileForm validates correctly with all fields completed
**Accounts** - ProfileForm validates correctly with only required fields completed
**Accounts** - View edit_Profile only for authorised user
**Home** - Tests that the url for '/' resolves correctly

Extensive manual testing has also been conduted to make sure that conditional content is viewed correctly for each type of user:

**Logged out:**
    i. Able to browse through website for information
    ii. Able to view event prices and information & request log in for further info
    iii. Registration process works

**Logged in not a member:**
    i. Able to browse through website for information
    ii. Able to view event prices and information & request to complete member registration for futher options
    iii. Able to view memeber's account page and details
    iv. Able to view booking history (if applicable)

**Logged in registered member no subscription:**
    i. Able to browse through website for information
    ii. Able to view event prices and information
    iii. Able to purchase tickets for package classes & special events
    iv. Able to view memeber's account page and details
    v. Able to view booking history (if applicable)
    
**Logged in registered member with subscription:**
    i. Able to browse through website for information
    ii. Able to view event prices and information
    iii. Able to purchase tickets special events only (package classes FOC)
    iv. Able to view memeber's account page and details
    v. Able to view subscription details and if active able to cancel
    vi. Able to view booking history (if applicable)
    
**Forms & Inputs :**
    i. log in, log out, registration, forgotten password - all forms work correctly and display appropriate error messages where applicable
    ii. Forms have been tested for validation of fields
    iii. In case of incorrect input a message pops up with hint for correction
 
This web app has been designed to display on various screen sizes.  The variable view have been handled with a combination of bootstrap column settings in HTML and @media queries in CSS.

## Deployment



This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X