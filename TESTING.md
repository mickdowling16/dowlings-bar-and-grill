# Testing
---

## HTML Testing

To test my HTML code I used [The W3C Markup Validation Service](https://validator.w3.org/). Because my code contained Jinja syntax I tested my using the test by URI feature. Below are the recorder results

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

![No errors on homepage](documentation/testing/no-errors-homepage-html.PNG)

</details>