# Dowling's Bar & Grill

Welcome to Dowling's Bar & Grill, a combination of an American sports bar and an Irish pub. The objective of this website is to provide potential customers with a website to view our menu, read about our restuarant and book a table. The goal of the website for an admin is to be able to manage all bookings. This includes the features to accept bookings, suggest a new booking time for customers, edit bookings and delete bookings. The customer will also be updated each time a change is made to their booking via email.

To achieve the goals of this project I have used full stack software development tools including HTML, CSS, JavaScript, Django and Python.

---

## Features 

### Navbar

The navbar is a feature used on all pages on the website and is vital for customers and admins to navigate the website effectively. The navbar changes if the admin is logged in to show admin controls to manage bookings and view confirmed bookings. On the navbar a user can navigate to the homepage, the menu, the contact us section and the reservations page. When an admin is logged in they can navigate to the manage bookings page and the confirmed bookings page, they also have the option to log out.

This navbar was created on my base.html template so I could import it on all pages.

### Hero Image

The hero image appears on the homepage welcoming the user to the website and showing them buttons for booking a table and viewing the menu so they can quickly navigate to the desired page. 

### Footer

The footer is also found on every page on the website. The footer contains 3 columns including social media links, the address of the business and a navigation menu for added user experience when navigating the website

This was also created on my base.html template to make it easier to implement on all pages.

### About section

The about section appears on the homepage and it is a breif introduction to the history of Dowling's Bar and Grill. The about section outlines the history of the bar with images and also gives the user a breif description of what to expect.

This section was styled with bootstrap to create 2 side by side columns that display and image and text. This view changes for mobile to contribute to a better user experience and displays the content in one column on smaller devices.

### Menu

The menu section shows the user our Starters, Mains and Desserts on offer at Dowling's Bar and Grill. The menu consists of a title, description, price and image. The menu is styled with bootsrap and my own custom css. The menu is imported from a javascript array and displayed through a function in my menu.js file. I decided to display the menu like this to keep my index.html page cleaner and to make the menuitems easily editable. The function loops through the menu items and displays them on the index.html page. The array can be added to, to include as many menu items as you need.

### Contact Us

The contact us section includes 2 columns. One for a Google map displaying the location of the restuarant. This was created using a Google maps api key and it is imported from my maps function in a seperate maps.js file located in the static directory. 

The second column on the contact us section is a contact form that sends an email to the restuarant with the customers query. The contact us form sends the email using SMTP and sends it to an email address i've created for the project. The restuarant will them recieve this email with the information and can reply to the customer directly from gmail.

### Reservations

The reservations page is a form that allows a user to book a table at Dowling's Bar and Grill. The form has 7 fields. Name, email, phone number, date, time, number of people and a message box.

The user can book a table with the calender for a date in the future only for a time between 12pm and 9pm. This is the times in which the bar serves food 7 days a week. The user can then select the number of people between 2 and 8. They can then add a message for a special request or query.

When this form is submitted, The page will update with a message to let the user know that the booking has been submitted and they will be contacted as soon as possible for confirmation. The admin will then get an email to dowlingsbarandgrill@gmail.com to let them know there has been a new booking.

### Admin Log In

The admin log in page allows a super user to log in to the site to access admin privlidges. The admin logs in with their username and password and is redirected to the manage bookings page

### Manage Bookings

The manage bookings page is where all bookings from the reservations form go. This view is only accessable when an admin is logged in and from here they can see all the booking information.

This page displays 9 booking cards per page. The cards are displayed in an easy to read format outlining all the booking information submitted by the customer. The admin has the option to accept the date propossed by the customer or suggest a new date. If the accept the original date the booking updates and moves to the confirmed bookings view. A success message will appear to confirm that the booking has been accepted and the customer will recieve an email confirming this also. This email is send using my email.html template.

If the booking time or date does not suit the restuarant or the customer wants to change it before it is excepted, a suggest a new date button can be used. This allows the admin to select a date and time and submit this change to update the booking. The customer will then recieve an email with the new time and date asking them to confirm if this suits. When the customer accepts this date and time, the admin can then accept the new booking and this will move to the confirmed bookings view

### Confirmed bookings

The confirmed bookings view is also only accessable to logged in admins. This page displays all the current bookings that have been accepted. This view will automatically delete past bookings over 1 day old. This view allows an admin to cancel a booking. This will send a confirmation email to the customer letting them know thier booking was cancelled. This view also has an edit booking option so a booking can be edited by an admin if a customer requests. To manage large amounts of bookings the view can be filtered by specific date to allow the admin to view only bookings on that date. 

This view also displays 9 bookings per page on easy to read cards that are styled with bootstrap. 

## CRUD Functionality

I have implemented CRUD functionality into this project by allowing an admin the ability to fully manage booking to the restuarant. They can accept bookings, edit bookings, suggest new time and date for bookings and cancel bookings. The customer can add bookings using the reservations form.

This functionality represents the features needed for a real world application to manage online bookings for a busy restauarant. This gives the restuarant more visability on all their upcoming bookings and the ability to edit them and filter them for specific dates. The customer is also updated in real time with emails regarding any change in their booking. This allows the resturant to save time when dealing with large amounts of bookings as all functionality can be done straight from the admin panel.

## Design

The design of my website was inspired by holidays to New York and Canada where the Irish sports bar is very popular and seen nationwide. I used a mixture of green, white and gold for my colours to represent Ireland and I used images of american sports bars to tie in with the theme.

### Colour pallette

![Colour Pallette](documentation/colours.PNG)

I decided to use these colours as they represent the Irish flag colours and I think it ties in well with the overall theme of my website.

### Typography

I used the fonts Roboto Serif and Alice for the main fontson this site. I liked the Alice font for the headings and logo as I thought it looked old and classy and this was the vibe i was going for mith my sports bar, being inspired by New York. I used the Roboto Serif font for the main text as it looked clean and matched the design. I used Google fonts for these and imported them into my custom CSS file.

## Agile Methodology

I used GitHub to implement agile methodology into this project by creating epics and user stories in my repository and using these to plan out my project and features to implement based on importance to achive a MVP. One week was spent on project planning where I outlined my original idea, features I'd like to include and a plan of attack. The initial sprint took 2 weeks where I implemented the main base of the project including the beginning templates and all html and css. I then reevaluated the features needed and the last sprint took 2 weeks to implement the main django features.
