# Lay-Z-Gym

*Ecommerce Web Application with User Authentication and Stripe payments and subscription options. 

The web app is designed with a small fitness company in mind. The objective is to have an online presence and also enable customers to purchase services directly online.  It can easily be adapted to the use for personal trainsers who would also like to advertise their services but dont have a physical service location.  

## Live Link 
The web app has been deployed on Heroku and may be accessed by clicking on this link https://ringhio79-lay-z-gym.herokuapp.com/
 
## UX

The website would be used by fitness clients.  The web app offers various levels of access depending on the type of authentication and registration level:

- Not authenticated: I can browse for information on the services provided but no account information or purchasing options are provided .  Must log in for further options and information
- Authenticated:  I can browse the website for information on the services provided and prices but cannot effect any purchases.  My account button will give me information about how to complete my registration and become a member.
- Basic Registration: I can browse the website, buy a subscription or purchase class packs/special event tickets for personal use as well as additional guests. I can view my account details on the 'account' page, including past bookings (if any)
- Subscripbed user: I can get information on all classes and events.  Scheduled classes are free but I have the option to purchase tickets to special events for personal use and for additional guests.  I can also view and manage my account from the 'account' page. 


This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

The application is built with two apps, Accounts and Events.  The accounts app handles the features related to authentication, membership and subscription while the Events app handles the events and services provided by the company.

### Accounts
- User login - allows users to create a log in account using just username, email and password.  Users are given the option whether they want to complete the regisgtration process immediately or return to it at a later stage.

- Registration/Profile - by completing the registration process the user also provides their payment details.  The payment details are sent to Stripe which in turn returns a Stripe ID.  The Stripe ID is stored in the user's profile but not credit card details are kept in the database. 

- Automated payments - The Stripe ID enables the user to make purchases automatically without having to fill in payment details for every transaction.

- Subscriptions - A registered user can sign up for a yearly subscription or monthly subscription.  This is done by using the Stripe ID to take payments on a yearly or monthly basis respectively.  Subscription details are also visible in the accounts page.

### Events
- 

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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