# Extream Vocal School Django P4
## This a my first business based framework.
### The idea with this business page is to make it possible for everyone in every and all ages to learn the basic requierments and essential skills to bring there vocal range to a new level.
### This idea can be used for all sorts of businesses of any kind!
Please take the time to check this read me file and get an understanding of the website.
![You can find the live version here](add link)


![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661416981/ifgwx4t8dgswluvzfrmr.png)


# Features

 - ## The Nav Bar
    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661417758/ok5wp65kpfbaxvhhskbn.png)
- This Navigation bar is clean and simple and more or less says it'self!

  -  Upon pressing "The 4 steps", you are redirected down the this area shown in the below image, with what steps are being taken for your journey.
  
    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661419293/owv6ayffqn94h9lh3dp7.png) 

 -  Upon pressing "Services", you are redirected down the this area shown in the below image, were information about my service and what you can expect from me as a tutor.
    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661419486/hgehwxt0ppu84zus3rev.png)

-  Upon pressing "Testimonials", you are redirected down the this area shown in the below image, were student's have left there reveiw's and such.

    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661419807/ufhswbkgono5eyevomfj.png)

-  And last on the bottom of the page, i have a contact area with my nr,email,location and a link to my social facebook page.

    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661420099/zhj5zmoy7tilmbasa2vw.png)

- ## Let's go back to the top!
 - Also at the top, if you are not logged in, the nav bar will display 2 options, "Register" & "Login"!

   ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661422059/c6r0kymfjlas6zvadblx.png)

 ### When you have registered or logged in it, the navbar will change:
  - After login or register, the navbar will appear like this:
   ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661422250/tia2rpa2lvydrv7aos9j.png)

   - You now have the alernative to "manage" and "logout".

- ## Let's try to Book an appointment!
![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661422507/wx0rjwvmo066114ugnxp.png)

###  After pressing this btn, You will enter a booking process!
    The booking is in a type of a from, you enter your name email and phone and also your request!
![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661422803/y9dlfcrh5pvrtevr8vq6.png)

   After you fill out the form as seen below!
   ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661423031/qrj9pgchm1ebu6vsabvc.png)

   Your request will be sent to the admin page or confirmation in the admin panel:
   ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661423168/l5cacuwwmlvyokpkcspp.png)

- ## Manegment
  - If you are a registered user on this website you will have access to the "Manage" option on the nav bar, pressing this will bring you to a appoinrment management page. (This page is not fully functional at this point)
  ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661423534/soikvktxnvnnnss8xuvz.png)

 - ## Storage
    - Cloudinary
    - Static files
    - also an img file for bigger images

- ## Future Improvments
  As a developer it's important to see your errors and understand and see what can be better and can be improved! This is my take on future improvments!

    - Invest more time in reading documentation for django to optimze the user experience and user interface to get the best out of django!
    - Make a code that give's you a comformation on bookings.
    - Connect a email api to make it easier to reach out and contact the company (except for just facebook and phone calls)
    - The sign in / sign out / register pages have no styling but are fully funtional, in the future i would be wise to invest more time into learing template styling.
    - Improving the management opitons.
    - Adding a notification code that let's admin's know when there has been a new appointment request.


- ## Future Features
    - And a media sektion that supply the student with basic techniques for vocals.
    - Make a better more satisfing GUI that is more personal and modifyed
    - Improve the management and manipulation for users.

# Testing
 ###  Testing with TestCase:
   - Here are my detailed view test's:

   - Index test:

   ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661434246/pxmnce1lu7qux0vsgnpz.png)

   - Appointment test:

   ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661434839/jrd9d8vmafa6epndylct.png)

   - Manage Appointment test:

   ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661435023/jrrmy62qdxzmosaztzni.png)


  - All view test's:

    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661436638/a1lypvnvrole1mbev5fw.png)

    The code for view testing can be found in here: vocal_school/test_views.py!

    ###  Testing Html with (https://validator.w3.org/):

    - HTML show's 3 errors, but no negative impact on the frontend, the reason is that the tester isnt not aware that the "{{% %}}" is being used.
    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661437423/cxvaihem0r14elkotz7l.png)

    ###  Testing CSS with (https://validator.w3.org/):

    - HTML show's 3 errors, but no negative impact on the frontend, the reason is that the tester isnt not aware that the "{{% %}}" is being used.
    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1661437423/cxvaihem0r14elkotz7l.png)

  - ## Manuall testing:
   - During the coding process i have manually check the github problem terminal and resolves all issues as i have gone along.
   - I have also run the code in pep8 muliple times and corrected issues on the way.
   - Some error's under the process such as missing docstring's stil remain's on some pages.

  - Used language:
      - HTML
      - CSS
      - Javascript
      - Python
  -  Extentions:
      - Bootstrap
      - Django
      - Jquery

- ## ADMIN CREDENTIALS
  - username: CIadmin
  - password: qwed1234
 
 # Bugs
  - There is a remaing CSS bug and styling bug for the log out/ sign up and register pages but the pages are fully functional.



 # Deployment

 - This project was deployed via github's terminal to heroku using the git add command, after pushing to github, it was deployed to heroku

  - The code can be found on github [Here](https://github.com/Kollecollier/Pyhton_portfolio3)!

 # Credits & Content
 - [Template's and Idea for the project](https://www.youtube.com/watch?v=3_3q_dE4_qs&ab_channel=SelmiTech)

 - [Code Institue](https://codeinstitute.net/se/) for deployment