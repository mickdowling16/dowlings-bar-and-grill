# Testing
---

## HTML Testing

To test my HTML code I used [The W3C Markup Validation Service](https://validator.w3.org/). Because my code contained Jinja syntax I tested my HTML code using the test by URI feature. Below are the recorder results. For the pages that required an admin to be logged in this approach did not work and I had to test the using the below steps.

In order to properly validate my HTML pages with Jinja syntax for authenticated pages, I followed these steps:

- Navigate to the deployed pages which require authentication
- Right-click anywhere on the page, and select view page source
- This displays the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the validate by input method.
- Repeat this process for every page that requires an admin to be logged in

<details>
<summary>Index.html page</summary>
<br>
- Errors in first test. 
  
![Homepage Errors](documentation/testing/errors-homepage-html.PNG)

- After fixing these few errors by removing the button tag and just using an a tag, and adding code to my homepage view to populate page title. All tests passed

![No errors on homepage](documentation/testing/no-errors-homepage-html.PNG)

</details>

<details>
<summary>Reservations Form Page</summary>
<br>
- Errors in first test. These were similar to the errors on the homepage and an easy fix
  
![Booking page errors](documentation/testing/errors-bookings-html.PNG)

- After fixing these few errors by adding code to my bookings view to populate page title and removing the role of the form. All tests passed

![No errors on bookings page](documentation/testing/no-errors-bookings.PNG)

</details>

<details>
<summary>Admin Log In Page</summary>
<br>
- Errors in first test on log in page. These were similar to the errors on the homepage and an easy fix
  
![Log in page errors](documentation/testing/admin-log-in-error.PNG)

- After fixing this error by adding code to my log in view to populate page title. All tests passed

![No errors on log in page](documentation/testing/admin-log-in-no-errors.PNG)

</details>

<details>
<summary>Manage Bookings Page</summary>
<br>
- Errors in first test show there is multiple duplicate IDs. This was caused by having an ID value on the card and looping through for multiple cards causing the ID to duplicate.
  
![Manage booking errors](documentation/testing/manage-bookings-errors-html.PNG)

- To fix these errors by changing all the id names to classes

![No errors on manage bookings page](documentation/testing/no-errors-manage-bookings-html.PNG)

</details>

<details>
<summary>Confirmed Bookings Page</summary>
<br>
- No errors were found on my confirmed bookings page.
  
![Confirmed bookings no errors](documentation/testing/no-errors-confirmed-bookings.PNG)

</details>

<details>
<summary>Edit Bookings Page</summary>
<br>
- 3 errors were found on my edit bookings page. Page title as before and an error with the prepopulated code for date and time.
  
![Edit bookings page errors](documentation/testing/edit-bookings-error.PNG)

- After fixing the value of the time and date on my edit bookings form to properly pre populate with the correct format my code passed with no errors

![no errors in bookings page](documentation/testing/no-errors-edit-bookings.PNG)

</details>

<details>
<summary>Booking confirmation Email Template</summary>
<br>
- No errors were found in my booking confirmation email template
  
![No errors in email template](documentation/testing/email-html-no-errors.PNG)

</details>

<details>
<summary>Cancel Booking Email Template</summary>
<br>
- No errors were found in my cancel bookings email template
  
![No errors in cancel booking email template](documentation/testing/cancel-booking-email-no-errors.PNG)

</details>

<details>
<summary>Suggest a time Email Template</summary>
<br>
- No errors were found in my suggest a time email template
  
![No errors in suggested time email template](documentation/testing/suggested-time-email-no-errors.PNG)

</details>


## CSS Testing

To test my CSS file I used [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/). I copy and pasted my CSS file into the validator and it returned no errors

<details>
<summary>CSS Testing</summary>
<br>
- No errors were found
  
![No errors in CSS File](documentation/testing/css-no-errors.PNG)

</details>

## JavaScript Testing

To test my JavaScript code I used [JShint Validator](https://jshint.com/) to validate all of my JS files. The results are listed below.

<details>
<summary>Menu.js Test</summary>
<br>
- No errors were found in my menu.js file
  
![No errors in Menu JavaScript file](documentation/testing/menu-js-no-errors.PNG)

</details>

<details>
<summary>Map.js Test</summary>
<br>
- There were a couple of undifined google variables in my JavaScript code. and one unused variable in mymap. These variables are pulled for the Google maps API and my google maps shows on my page without any issue. When trying to fix these errors my map dissapears from my page. I decided to revert back to the code I have so my map shows and try to fix the bug at a later time.
  
![Errors in maps javascript file](documentation/testing/maps-js-errors.PNG)

</details>

## Python Testing

I have used [CI Python Linter](https://pep8ci.herokuapp.com/) to validate all of my Python files. Below are the results. When testing my python code the majority of the errors were related to line length. When i fixed this and went to deployment my heroku app was giving errors as it could not read values split accross two lines. I've had to change back some of the python code I fixed including links to databases and static files in my settings.py and env.py file.

<details>
<summary>Settings.py Test</summary>
<br>
- There were a couple of errors to do with line length in my settings.py file. When I fixed these errors my code passed 
  
![Errors in settings.py](documentation/testing/settings-py-error.PNG)

- All tests passed

![No errors in settings.py](documentation/testing/settings-py-no-errors.PNG)

</details>

<details>
<summary>urls.py main</summary>
<br>
- There were no errors found in my main urls.py file
  
![No errors in main urls.py](documentation/testing/urls-main-no-errors.PNG)

</details>

<details>
<summary>wsgi.py</summary>
<br>
- There were no errors found in my wsgi.py file
  
![No errors in wsgi.py file](documentation/testing/wysgi-no-errors.PNG)

</details>

<details>
<summary>asgi.py</summary>
<br>
- There were no errors found in my wsgi.py file
  
![No errors in wsgi.py file](documentation/testing/asgi-no-errors.PNG)

</details>

<details>
<summary>views.py</summary>
<br>
- There were errors found in my views.py file for too long line lengths.
  
![Errors in views.py file](documentation/testing/views-py-errors.PNG)

- After fixing the line lengths my tests passed with no errors
  
![No errors in views.py file](documentation/testing/views-py-no-errors.PNG)

</details>

<details>
<summary>models.py</summary>
<br>
- There were no errors found in my models.py file.
  
![No errors in models.py file](documentation/testing/models-py-no-errors.PNG)

</details>

<details>
<summary>urls.py booking app</summary>
<br>
- There were no errors found in my urls.py file in my booking app.
  
![No errors in urls.py booking app file](documentation/testing/urls-booking-no-errors.PNG)

</details>

</details>

<details>
<summary>admin.py</summary>
<br>
- There were no errors found in my admin.py file
  
![No errors in admin.py file](documentation/testing/admin-py-no-errors.PNG)

</details>

<details>
<summary>apps.py</summary>
<br>
- There were no errors found in my apps.py file
  
![No errors in apps.py file](documentation/testing/apps-py-no-errors.PNG)

</details>

## Browser Compatibility

I've tested my app on multiple browsers including Chrome, Microsoft Edge and Firefox.

<details>
<summary>Chrome Compatibility</summary>
<br>
- My app was built using Google chrome and all of my development took place on Google chrome. No issues were found when using this browser and everything is working as expected. My site features work as intended and emails send correctly to users. 
  
![Chrome screenshot](documentation/testing/chrome-compatibility.PNG)

</details>

<details>
<summary>Edge Compatibility</summary>
<br>
- when testing my app on Microsoft edge everything worked as expected. The styles remained consistant and emails sent without issues. There was not any difference in performance when testing on this browser
  
![Edge screenshot](documentation/testing/edge-compatibility.PNG)

</details>

<details>
<summary>Firefox Compatibility</summary>
<br>
- when testing my app on Firefox everything worked as expected. Styles were the same except for the form elements where drop down menus and calenders looked different as expected on a different browser. All my emails and reservations form worked as expected and my alerts popped up when forms were submitted
  
![Firefox screenshot](documentation/testing/firefox-compatibility.PNG)

</details>

## Responsiveness

When testing responsiveness I used my laptop, phone and tablet along with Google developer tools to test the app on different screen sizes. I styles my app with bootstrap to account for smaller screen sizes and for it to be responsive on mobile and tablet. It works as expected on these different screen sizes and below are screenshots from the manage bookings admin page on different devices.

- Mobile(dev tools)

![Mobile Responsiveness](documentation/testing/mobile-responsiveness.PNG)

- Tablet Responsiveness(dev tools)

![Tablet Responsiveness](documentation/testing/tablet-responsiveness.PNG)

- Laptop Responsiveness(dev tools)

![Laptop Responsiveness](documentation/testing/laptop-responsiveness-bookings.PNG)

- Desktop Responsiveness(dev tools)

![Desktop Responsiveness](documentation/testing/large-laptop-resonsiveness.PNG)

## Lighthouse Audit

I tested my deployed app speed on lighthouse to check for major issues. Below are screenshots from each page of my website

- Homepage test

![Homepage Lighthouse](documentation/testing/homepage-lh.PNG)

- My bookings page was giving a low score for accessability because I didn't have labels on my form. I fixed this and imporoved my score

![Bookings Lighthouse](documentation/testing/bookings-lh-1.PNG)

![Bookings Lighthouse](documentation/testing/bookings-lh-2.PNG)

- Manage bookings test
  
![manage bookings Lighthouse](documentation/testing/manage-lh.PNG)

- Confirmed bookings test

![confirmed bookings Lighthouse](documentation/testing/confirmed-lh.PNG)

- Edit bookings test

![edit bookings Lighthouse](documentation/testing/edit-lh.PNG)

- Admin log in test

![admin log in Lighthouse](documentation/testing/admin-lh.PNG)

## Manual Testing

I manually tested each page of my site performing tasks that both a user and admin would perform and recording the results. My tests are layed out below for each individual page and displayed in a table.

- Homepage tests

![Homepage Manual Tests](documentation/testing/homepage-mt.PNG)

- Reservations page

![Reservations Manual Tests](documentation/testing/reservations-mt.PNG)

- Manage Bookings page

![Manage Bookings Manual Tests](documentation/testing/manage-mt.PNG)

- Confirmed Bookings page

![Confirmed bookings Manual Tests](documentation/testing/confirmed-mt.PNG)

- Admin Log in

![Admin login Manual Tests](documentation/testing/admin-mt.PNG)

- Edit booking page

![Edit bookings Manual Tests](documentation/testing/edit-mt.PNG)

## User Story Testing

The user stories were tested as part of the manual testing above and can be matched to the manuals tests fulfilling them by their keys which have been added below.

US1:
 - As a Admin I can limit the amount of bookings per time slot so that we don't get overbooked

US2:
 - As a User I can easily access the bars social media channels so that I can follow them for updates and connect with their page

US3:
 - As a Admin I can edit upcoming bookings so that I can easily change booking info at the request of a customer

US4:
 - As a User I can receive updates on my booking so that I know if there is any changes

US5:
 - As a Admin I can cancel bookings so that I can manage the number of tables being served

US6:
 - As a User I can navigate the website so that I can find all the information I need easily

US7:
 - As a Customer I can receive a confirmation so that I know my booking has been confirmed

US8:
 - As a Admin I can login so that I can view all current bookings

US9:
 - As a Admin I can manage bookings so that I can confirm or deny any booking requests

US10:
 - As a Potential customer I can contact the restaurant so that I can make a special request or ask a question

US11:
 - As a Potential customer I can book a table online so that I can secure my table at a time and date that suits me

US12:
 - As a Potential customer I can view the menu options so that I can decide if I want to eat here


## Bugs

### Solved Bugs

- A major bug that I came across early in development was that my emails would not send using gmail. This was down to a couple of reasons. I needed to set up an app password for my gmail account for django to access it through a third party. I also needed to configure my settings.py file correctly for my email settings and I needed to add these settings to my config vars on heroku. I solved this by going ahead to the next walkthrough module for PP5 and looking at the email set up video. After following the walkthrough my emails were sending correctly
- Another bug that I faced was after deployment to heroku my static files were not being shown on my site. This was fixed by looking through previous problems people had on slack to identify the problem. My static file links in my settings.py file were incorrect and when I changed them this problem was fixed.
- Another bug on deployment to heroku was a internal server error where when debug was switched to False my site wasn't showing. This was an error between my database path. I was helped identify this by a fellow student on slack.
- A small bug I encountered with my css was making my page scroll horizontially which was giving a bad user experience. I fixed this by editing my max width and height attributes for my body and content container in my css file

### Unsolved bugs

- An unsolved bug I am experiences is to do with the PEP8 python code requirements. Some of my code goes over the reccommended character length. When I fixed this then my code wasn't reading correctly and my site was failing to deploy. I had to revent back some of the changes I made. I tried to use AutoPep8 to fix this issue but it would not work for me and my code still has problems. My app works as expected right now and I'm afraid to make changes this close to project submission and risk my app not working in deployment. For testing I fixed these issues and my code passed the validator so I'm happy that I have no mistakes, just the issue of line length.