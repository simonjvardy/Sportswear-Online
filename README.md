![SO logo](media/sportswear_online_logo.png)


![Sportswear Online screenshot](wireframes/Sportswear_online.png)
---

### **Contents** ###

- [UX (User Experience)](#ux-user-experience)
  - [Project Goals](#project-goals)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
  - [Site Owner Goals](#site-owner-goals)
- [Technologies](#technologies)
  - [Languages](#languages)
  - [Database](#database)
  - [Libraries](#libraries)
  - [Tools](#tools)
- [Credits](#credits)
  - [Images](#images)
  - [Colour](#colour)
  - [Inspiration](#inspiration)
  - [Acknowledgements](#acknowledgements)


---

## UX (User Experience) ##

### **Project Goals** ###

The **goal** of this project is to build a 

### **User Stories** ###

| User Story ID | AS A / AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
| --- | --- | --- | --- |
| | | ***Viewing and Navigation*** | | 
| 1 | Shopper | View a list of products | Select some to purchase |
| 2 | Shopper | View a specific category of products | Quickly find product's I'm interested in without having to search through all products |
| 3 | Shopper | View individual product details | Identify the price, description, product rating, product image and available sizes |
| 4 | Shopper | Quickly identify deals, clearance items and special offers | Take advantage of special savings on products I'd like to purchase |
| 5 | Shopper | Easily view the total of my purchases at any time | Avoid spending too much |
| | | ***Registration & User Accounts*** | | 
| 6 | Site User | Easily register for an account | Have a personal account and be able to view my profile |
| 7 | Site User | Easily login or logout | Access my personal account information |
| 8 | Site User | Easily recover my password in case I forget it | Recover access to my account |
| 9 | Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| 10 | Site User | Have a personalised user profile | View my personal order history and order confirmations and save my payment information |
| | | ***Sorting & Searching*** | | 
| 11 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sorted products |
| 12 | Shopper | Sort a specific category of product | Find the best-priced or best-rated product in a specific category or sort the products in that category by name |
| 13 | Shopper | Sort multiple categories of products simultaneously | Find the best-priced or best-rated products across broad categories, such as "clothing" or "homeware" |
| 14 | Shopper | Search for a product by name or description | Find a specific product I'd like to purchase |
| 15 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |
| | | ***Purchasing & Checkout*** | | 
| 16 | Shopper | Easily select the size and quamtity of a poduct when purchasing it | Ensure I don't accidentally select the wrong product, quantity or size |
| 17 | Shopper | View items in my shopping bag to be purchased | Identify the total cost of my purchase and all items I will receive |
| 18 | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout |
| 19 | Shopper | Easily enter my payment information | Checkout easily with no hassles |
| 20 | Shopper | Feel my personal and payment information is secure | Confidently provide the needed information to make a purchase |
| 21 | Shopper | View an order confirmation after checkout | Verify I have I haven't made any mistakes |
| 22 | Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records |
| | | ***Admin & Store Management*** | | 
| 23 | Store Owner | Add a product | Add new items to my store |
| 24 | Store Owner | Edit / update a product | Change product prices, descriptions, images,and other product criteria |
| 25 | Store Owner | Delete a product | Remove items that are no longer for sale |



[Back to contents](#contents)

--- 

## Technologies ##

### **Languages** ###

- [Python3](https://www.python.org/)
  - Used to create the main application functionality
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used to style the individual webpages.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - Used to create the interactive functionality of the website


### **Database** ###

- [PostgreSQL](https://www.postgresql.org/)
  - A powerful, open source object-relational database.
- [sqlite3](https://www.sqlitetutorial.net/sqlite-python/)
  - Default database created with Django used for app development on localhost.

### **Libraries / Frameworks** ###

- [Bootstrap5](https://getbootstrap.com/)
  - Used to design a mobile-first responsive website layout.
- [Django](https://www.djangoproject.com/)
  - A high-level Python Web framework.
- [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)
  - Python user authentication and login plugin for Django.
- [Stripe](https://stripe.com/en-gb)
  - Online payments platform used for the shopping basket functionality.
- [Green Unicorn (gunicorn)](https://gunicorn.org/)
  - Python WSGI HTTP Server for Unix used on the Heroku deployment.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
  - PostgreSQL database adapter for Python.
- [Pillow](https://pillow.readthedocs.io/en/stable/)
  - Python Image Library image processing capabilities.
- [sqlparse](https://pypi.org/project/sqlparse/)
  - sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
  - AWS SDK for Python (Boto3) used to create, configure, and manage AWS S3 services.
- [jQuery](https://jquery.com/)
  - Used for the initialisation of the Bootstrap5 components functionality and enhance the shopping bag functionality.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
  - Templating language for Python.



### **Tools** ###

- [Git](https://git-scm.com/)
  - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
  - Used to store, host and deploy the project files and source code after being pushed from Git.
- [Gitpod](https://www.gitpod.io/)
  - An online IDE linked to the GitHub repository used for the majority of the code development.
- [Font-Awesome](https://fontawesome.com/icons?d=gallery)
  - Used for icons to enhance headings and add emphasis to text.
- [Heroku](https://www.heroku.com)
  - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [AWS S3](https://aws.amazon.com/s3/)
  - Amazon Simple Storage Service (Amazon S3) is an object storage service used to store the site static files
- [JSON Formatter](https://jsonformatter.org/)
  - Online JSON Formatter, validator and conversion tool
- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
  - The Django Secret Key Generator is used to generate a new SECRET_KEY for environment variables.
- [Adobe Lightroom](https://www.adobe.com/uk/products/photoshop-lightroom.html) 
  - For batch photo resizing and exporting for web
- [Adobe Spark](https://spark.adobe.com/sp)
  - Used to create the Sportswear Online logo
- [favicon.io](https://favicon.io/)
  - Used to create the website favicons
- [CSS Gradient Tool](https://cssgradient.io/)
  - Used to create the jumbotron radial gradient
- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
  - Used to greate the Django environment variables secret keys

---

## Credits ##

### **Inspiration** ##

The following sportswear online retailers' websites were the basis for the design and layout ideas:

- [JD Sports](https://www.jdsports.co.uk/)
- [Sports Direct](https://www.sportsdirect.com/)
- [Decathlon](https://www.decathlon.co.uk/)
- [Greaves Sports ](https://www.greavessports.com/)
- [MA Sports](https://www.masports.co.uk/)
- [MandM Direct](https://www.mandmdirect.com/)

### **Images** ###

- [Fashion Product Images Dataset](https://www.kaggle.com/paramaggarwal/fashion-product-images-dataset) Credit: Param Aggarwal @ www.kaggle.com
  - The dataset consists of 44,440 images and associated individual JSON data files containing the product information.

### **Acknowledgements** ###

- [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma/) Course material - in particular the Boutique Ado Django mini project
- [Simon Vardy](https://github.com/simonjvardy) for code snippets and README.md content.
- [Neringa Bickmore](https://github.com/neringabickmore/art-ial) art-ial GitHub repo for inspiration and README.md content ideas
- [Aukje van der Wal](https://github.com/byIlsa/story-chain) story-chain GitHub repo for inspiration and README.md content ideas
- [Daisy McGirr](https://github.com/Daisy-McG/ChatToTheMat) ChatToTheMat GitHub repo for inspiration and README.md content ideas
- [Stack Overflow](https://stackoverflow.com/)
  - [Limiting Floats to 2 decimal places](https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points)
  - [Writing json data to a file](https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file)
  - [Append data to a json file](https://stackoverflow.com/questions/12994442/how-to-append-data-to-a-json-file)
  - [Django test always returning code 301](https://stackoverflow.com/questions/21215035/django-test-always-returning-301)
  - [Python - List all the files in a directory](https://stackoverflow.com/questions/12199120/python-list-all-the-file-names-in-a-directory-and-its-subdirectories-and-then-p)
  - [Create a branch from another branch in git](https://stackoverflow.com/questions/4470523/create-a-branch-in-git-from-another-branch)
  - [JS count the number of occurrences of a character in a string](https://stackoverflow.com/questions/881085/count-the-number-of-occurrences-of-a-character-in-a-string-in-javascript)
  - [Django error: templatetag is not a registered tag library](https://stackoverflow.com/questions/40686201/django-1-10-1-my-templatetag-is-not-a-registered-tag-library-must-be-one-of)
- [dev.to](https://dev.to/gajesh/the-complete-django-allauth-guide-la3) Django Allauth configuration tutorial
- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
  - [Models: Options](https://docs.djangoproject.com/en/3.1/ref/models/options/)
  - [Loading initial data fixtures](https://docs.djangoproject.com/en/dev/howto/initial-data/#automatically-loading-initial-data-fixtures)
  - [Contrib: Admin](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)
- [Kite](https://www.kite.com/python/answers/how-to-loop-through-all-nested-dictionary-values-using-a-for-loop-in-python
) How to loop through all nested dictionary values using a for loop in Python
- [W3Schools](https://www.w3schools.com/howto/howto_css_hide_arrow_number.asp) How to hide number field arrows with CSS
- [Bootstrap v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) Documentation and code snippets used to build the majority of the templates
- [Coderwall](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata) How to use Django dumpdata and loaddata
- [Stack Abuse](https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/) Reading & writing json to a file in Python.