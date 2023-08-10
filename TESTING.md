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