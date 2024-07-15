# <div id="up">Physio Appointment Management</div>

![](documentation/mockup.png)

### [Live site](https://pp4-physio-4e914098e1ff.herokuapp.com/)

## Contents:

- [UX](#ux)
  - [Overview](#overview)
  - [First Time User](#first-time-user)
  - [Returning User](#returning-user)
- [Strategy](#strategy)
  - [Agile](#agile)
  - [User Stories](#user-stories)
- [Database Structure](#database-structure)
- [Design](#design)
  - [Colours](#colours)
  - [Wireframes](#wireframes)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Testing User Stories](#testing-user-stories)
  - [Testing Features](#testing-features)
  - [Responsiveness Testing](#responsiveness-testing)
- [Bugs](#bugs)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Languages, Technologies & Libraries](#languages-technologies-libraries)
- [Credits](#credits)
- [Deployment](#deployment)
- [Acknowledgements](#acknowledgements)

## <div id="ux">UX</div>

### Overview
Physio Appointment Management is a web application for managing physiotherapy appointments, including booking, viewing, and managing treatments. The main goal is to create a simple and intuitive platform based on a deep understanding of the target users.

#### First Time User
- As a person seeking physiotherapy services.
- As a person looking for clear information about the physiotherapy treatments offered.
- As a person who prefers to make bookings digitally rather than over the phone.

#### Returning User
- As a returning user, I would like to review all my previous physiotherapy appointments.
- As a returning user, I would like to quickly and easily make an appointment with a specific physiotherapist.
- As a returning user, I would like to see updates and new information on the site.

### <div id="strategy">Strategy</div>

Determining the best approach involved studying the needs of potential users. This included enabling users to quickly and easily book appointments, as well as read, update, and delete their appointments (CRUD).

#### Agile
The Agile methodology was used to plan the project. GitHub was used as the tool to demonstrate this. Milestones were used to create Epics. Each user story was linked to an Epic and placed within one of three Iterations. Issues were used to create User Stories with custom templates ([Link to Kanban board](https://github.com/users/YourUsername/projects/1/views/1)). To prioritize tasks, the [MoSCoW method](https://github.com/users/YourUsername/projects/1/views/2) was used.

##### User Stories 
Issues were used to create User Stories with custom templates for admin and user. I added the acceptance criteria and the tasks to track my work effectively. Once I completed a User Story, I moved it from `in progress` to `completed`. 

- Completed User Stories:
  - Epic: Enable users to CRUD the bookings.
    - As a Registered User, I want to see a list of available treatments, including relevant details such as physiotherapist name, appointment date, and time, so that I can choose the options that suit me.
    - As a Registered User, I want to view my appointments so that I can keep track of my bookings.
    - As a Registered User, I want to edit my booking so that I can change the details.
    - As a Registered User, I want to delete my booking so that I can cancel my appointment.

  - Epic: Enable unregistered users to view all key information about the physiotherapy services.
    - As a User, I want to examine the information on the home page about the services provided to decide whether I want to use them.

  - Epic: Enable users to create an account and log in.
    - As a User, I want to create an account so that I can book an appointment.
    - As a User, I want to log in so that I can access my profile.

  - Epic: Set up admin page for admin (superuser) to manage appointments.
    - As an Admin, I want to have access to database data so that I can make necessary changes.
    - As an Admin, I want to view the bookings so that I can manage the physiotherapist's timetable.

- Uncompleted User Stories:
  - As a Registered User, I want to receive a confirmation email so that I know my appointment has been successfully booked.
  - As a Registered User, I want to be able to make an appointment with any available physiotherapist to have a wider range of dates and times.

### <div id="database-structure">Database Structure</div>

![](documentation/db_diagram.png)

The pre-planned database structure underwent several changes during the project, including the addition of `description` and `image` fields to the `Treatment` model.

### <div id="design">Design</div>

The site design is intuitive and functional, with an emphasis on usability. Google fonts Lato (body) and Raleway (headers) have been used to customize the default Bootstrap fonts. Sans Serif was chosen as the backup font.

#### Colours

The following colour palette was used from [Coolors](https://coolors.co/):

![](documentation/colour_palette.png)

The colours were chosen to convey professionalism and tranquility. The colour `Tomato` for the buttons was chosen to attract attention and contrast with the rest of the colours in the design.

#### Wireframes

> index.html

![](documentation/wireframe.png)

> booking.html

![](documentation/wireframe_booking.png)

<a href="#up">Back to Top of page</a>

---

## <div id="testing">Testing</div>

### Manual Testing

Thorough testing was conducted by the developer and multiple users among friends and family. Usability suggestions were considered and acted on. All design features were manually tested, and everything functions as expected.

- Testing for responsiveness was conducted using Chrome Dev Tools. The website was tested extensively on a range of emulated mobile, tablet, and large-format screen sizes in both portrait and landscape orientations.
- All HTML files were passed through the W3C validator with no errors.
- The CSS file (`style.css`) was passed through the W3C validator with no errors.
- The website was tested on browsers Chrome, Firefox, Edge, and Opera.
- All user flows were tested, including landing page navigation, link clicks, and form submissions.
- All forms were tested to ensure they are validated and can be submitted without errors.

#### <div id="testing-user-stories">Testing User Stories</div>

| User Story | User Story Testing |
|------------|--------------------|
| As a User, I want to examine the information on the home page about the services provided so that I can decide whether I want to use them. | The home page provides complete information about the physiotherapy services, treatments, and physiotherapists. |
| As a User, I want to create an account so that I can book an appointment. | The registration form includes fields for username, email, and password. Errors are shown for incorrect inputs. |
| As a User, I want to log in so that I can access my profile. | After logging in, the user can view their profile with current bookings. |
| As a Registered User, I want to see a list of available treatments, including relevant details, so that I can choose the options that suit me. | The booking form includes dropdown lists for selecting treatments, physiotherapists, and available dates and times. |
| As a Registered User, I want to view my appointments so that I can keep track of my bookings. | The profile page shows a list of current bookings with options to edit or delete them. |
| As a Registered User, I want to edit my booking so that I can change the details. | The update page prepopulates the booking form with the current details, allowing changes. |
| As a Registered User, I want to delete my booking so that I can cancel my appointment. | The delete page asks for confirmation before canceling an appointment. |
| As an Admin, I want to have access to database content so that I can make necessary changes. | The admin panel allows managing all database tables, including adding, editing, and deleting entries. |
| As an Admin, I want to view the bookings so that I can manage the physiotherapist's timetable. | The admin panel shows all bookings, allowing the admin to manage the schedule. |

#### <div id="testing-features">Testing Features</div>

##### Navigation Links

| Test | Result |
|------|--------|
| Non-logged-in user can access landing page links. | All navigation links work correctly and bring the user to the appropriate section. |
| Non-logged-in user can go to the home page by clicking the title or logo in the header. | Clicking the title or logo returns the user to the home page. |
| Non-logged-in user can access sign-in and login pages. | `Login` button and `Book now!` buttons redirect to the login or registration page. |
| Logged-in user can access profile page and log out. | Logged-in users see `Profile` and `Logout` buttons. `Book now!` buttons are hidden for logged-in users. |
| Logged-in user can view bookings. | The profile page shows a list of current bookings. |
| Logged-in user can log out of their profile. | Clicking `Logout` logs the user out. |

##### User Forms

| Test | Result |
|------|--------|
| User can create an account. | The registration form works correctly, showing errors for incorrect inputs. |
| User can log in. | The login form works correctly, showing errors for incorrect inputs. |
| Logged-in user can make a booking. | The booking form works correctly, requiring all fields to be filled out. |
| Autoreset booking form fields. | Changing the selected service resets the barber and date/time fields. |
| Logged-in user can update bookings. | The update form prepopulates correctly and saves changes. |

##### Security Tests

| Test | Result |
|------|--------|
| Non-logged-in user cannot make a booking. | Non-logged-in users are redirected to the login page. |
| Non-logged-in user cannot access the profile page. | Only logged-in users can access the profile page. |
| User cannot delete a booking without confirmation. | The delete page requires confirmation before deleting. |
| Non-superuser cannot access the admin panel. | Only superusers can access the admin panel. |

##### Admin Tests

| Test | Result |
|------|--------|
| Admin can view data in database tables. | The admin panel shows all data correctly. |
| Admin can add items to database tables. | The admin panel allows adding new entries. |
| Admin can edit items in the database. | The admin panel allows editing entries. |
| Admin can search and filter data. | The admin panel provides search and filter functionality. |
| Admin can delete items in the database. | The admin panel allows deleting entries. |

##### Booking Tests

| Test | Result |
|------|--------|
| List of physiotherapists is loaded correctly based on the selected treatment. | The dropdown list updates correctly. |
| Dates and times are loaded correctly based on the selected physiotherapist. | The dropdown list updates correctly. |
| Admin can manage physiotherapist availability. | Unavailable physiotherapists are not shown in the dropdown list. |

#### <div id="responsiveness">Responsiveness Testing</div>

Testing for responsiveness was conducted using Chrome Dev Tools. The website was tested extensively on a range of emulated mobile, tablet, and large-format screen sizes in both portrait and landscape orientations.

| Device | Resolution | Result |
|--------|------------|--------|
| Samsung Galaxy S8+ | 360 x 740 | Pass |
| iPhone 6/7/8 | 375 x 667 | Pass |
| iPhone X | 375 x 812 | Pass |
| iPhone 12 PRO | 390 x 844 | Pass |
| Samsung Galaxy A51/71 | 412 x 914 | Pass |
| iPhone XR | 414 x 896 | Pass |
| iPad Mini | 768 x 1024 | Pass |
| iPad Air | 820 x 1180 | Pass |
| iPad Pro | 1024 x 1366 | Pass |
| HP Laptop 14s | 1920 x 1080 | Pass |

<a href="#up">Back to Top of page</a>

---

### <div id="bugs">Bugs</div>

##### LoginForm Bug

- Error when processing data from the user login form:

![](documentation/error_login_form.png)

- Fixed LoginForm error:

![](documentation/fixed_login_form_bug.png)

##### DateTime Bug

- Errors due to format mismatches when iterating through DateTime and Time objects. Fixed using the `datetime.combine()` function:

![](documentation/fixed_bug_datetime.png)

##### Background Images Bug

- Background images not loading from Cloudinary after deployment. Fixed by adding direct URLs to the images in the `style.css` file.

### Google Lighthouse Testing

#### Desktop

Site pages tested using Lighthouse to identify performance and accessibility issues:

> Homepage (index.html)

![](documentation/lighthouse_homepage.png)

> profile.html

![](documentation/lighthouse_profile.png)

> booking.html

![](documentation/lighthouse_booking.png)

### HTML W3 Validation

![](documentation/html_valid.png)

Result: No errors or warnings.

### CSS Validation

![](documentation/css_valid.png)

Result: No errors.

### Python Validation

The only issues found in Python files were due to extra whitespaces and long lines, which have been fixed.

> views.py

![](documentation/views_valid.png)

Result: No errors.

### JavaScript Validation

JavaScript code passes through [Jslint](https://jslint.com) with no significant issues.

<a href="#up">Back to Top of page</a>

## <div id="features">Features</div>

### Existing Features

#### Navigation 

The main navigation is located in the header and is present on all pages. The hamburger menu is present on medium and small devices and expands to show the main navigation links.

![](documentation/header.png)

Logged-in users see a welcome message and have access to profile and logout options.

![](documentation/header1.png)

#### Landing Page

The landing page provides all key information about the physiotherapy services, treatments, and physiotherapists.

![](documentation/landing_page.png)

#### Footer

The footer provides contact information and a `Book now` button.

![](documentation/footer.png)

#### Registration Page

The registration form allows users to create an account.

![](documentation/registration.png)

Successful account creation is confirmed with a message.

![](documentation/account_success.png)

#### Login Page

The login form allows users to log in to their accounts.

![](documentation/login.png)

Successful login is confirmed with a message.

![](documentation/login_success.png)

#### Booking Page

Logged-in users can book appointments through a form with dependent dropdown lists.

![](documentation/new_booking.png)

The `Book` button is enabled only after all fields are filled.

![](documentation/booking_button.png)

#### Profile Page

The profile page shows current bookings and allows users to update or delete them.

![](documentation/profile1.png)

#### Update Page

The update form prepopulates with current booking details.

![](documentation/update_booking.png)

Successful updates are confirmed with a message.

![](documentation/updated.png)

#### Delete Page

The delete page asks for confirmation before canceling an appointment.

![](documentation/delete_booking.png)

Successful cancellations are confirmed with a message.

![](documentation/cancelled.png)

### <div id="features-left-to-implement">Features Left to Implement</div>

- Create an archive of appointments in the user profile.
- Improve the booking form by allowing users to select a date and time separately.
- Allow users to select the `any physiotherapist` option.
- Add a phone number field to the booking form.
- Send confirmation emails for appointments.
- Allow users to delete their accounts.
- Improve the registration form by using email addresses instead of usernames.
- Add animations to the treatment gallery.

<a href="#up">Back to Top of page</a>

## <div id="languages-technologies-libraries">Languages, Technologies & Libraries</div>

### Languages

- **Python** for backend logic.
- **HTML/CSS** and **Django Template Language** for structuring webpages.
- **JavaScript** for dynamic functionalities.

### Libraries and Frameworks

- **Django** for backend development.
- **Bootstrap 5** for frontend framework.
- **htmx** for AJAX requests.

### Technologies

- **PostgreSQL from Code Institute** for PostgreSQL database hosting.
- **Cloudinary** for static file hosting.
- **Heroku** for deployment.
- **GitHub** for version control and project management.

## <div id="credits">Credits</div>

- [Pexels](https://www.pexels.com/) and [Freepik](https://www.freepik.com/) for images.
- [Favicon.io](https://favicon.io/) for favicon creation.
- [favpng](https://favpng.com/) for icon templates.
- [Lucidchart](https://www.lucidchart.com/) for wireframes and database diagram.
- [Luis Cortes](https://www.youtube.com/watch?v=zYs42XcpHYI) for dependent dropdown lists tutorial.
- Various online resources for troubleshooting and debugging.

<a href="#up">Back to Top of page</a>

## <div id="deployment">Deployment</div>

To deploy the project on Heroku:

1. Sign up or log in to Heroku.
2. Create a new app on the Heroku dashboard.
3. Add a PostgreSQL database in the Resources tab.
4. Add the following Config Vars in the Settings tab:
   - `DATABASE_URL`: Your database URL
   - `SECRET_KEY`: Your Django secret key
   - `CLOUDINARY_URL`: Your Cloudinary URL
   - `DISABLE_COLLECTSTATIC`: 1 (remove this before final deployment)
5. Push the code to Heroku:
   ```bash
   git push heroku main
