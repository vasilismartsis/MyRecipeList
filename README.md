_\*This project was created for education purposes for a class of International Hellenic University_

**Period:** Spring Semester 2019-2020

**Course:** Online Value Added Services

**Author:** Martsis Vasileios

**Theme:** MyRecipeList

# MyRecipeList

### **1\. Addressed to:**

     The service that has been implemented as a website called MyRecipeList, is an online service in which the user can search for recipes based on the ingredients available. This service is aimed at people who own, limited or want to experiment with new, cooking materials. This service, unlike other similar services on the internet, which provide a simple recipe search by name, can free the hands of people belonging to the above categories. A particular example of a category of people who could help is those who are facing financial problems that may lead to a lack of ingredients needed to make many recipes. Another category of people are those who want to be involved in the art of cooking but do not have special knowledge in this field.

### **2\.** Technical Characteristics:

#### **2.1. Implementation:** 

     The service is implemented as a website. This choice was made because as a website, it is accessible from any device that has a browser and is not dependent on the operating system of each device unlike other applications that are for example implemented exclusively for mobile phones or computers.

     The service currently supplies the recipes from a ready-made semi-free API called Spoonacular but also from its local database which contains so far only the recipes that have been imported by me. The user is also given the opportunity to enter his own recipe into the system.

##### **2.1.1.** Back end:

     The application is implemented in Python, Javascript, html and CSS. The Flask library is used in Python. This library is one of the most popular libraries for developing web applications in Python. This library allows the user to create a server on their system that will host the application website. It also provides many features that greatly facilitate application development.

##### **2.1.2.** Base:

     The database used by the application is SQLite3, the feature of which is that it is stored in the application system as a file with a .sqlite3 extension. This database is very easy to use for small applications but can very easily be converted to another (eg) MySQL in case the application is further expanded in the future.

     The Pthon library used by the application to manage database connectivity is SQLAlchemy. It is a library that allows communication with the database at a higher programming level, providing the programmer with ready-made functions for this purpose.

##### **2.1.3.** Front end:

HTML-CSS and Javascript were used for the appearance and client side functionality of the application. For its best appearance, in some places the application uses templates from Bootstrap.

#### **2.2. Main page function:** 

     The main part of the application is the page that contains the directory in which the user will search for recipes by putting in an Input box the names of its available ingredients separated by commas. The choice of this input method was made because it allows the user to put without restriction any component he wants, but also because the other, equally user-friendly alternatives, such as selecting components through an alternative input e.g. . Checkboxes would require the developer too much time to search and enter the various components.

     As soon as the user enters the desired ingredients and presses the Search button, a list of recipes will appear, assorted by the Spoonacular API and the system database, sorted so that the first ones to use are displayed. the user will miss as few components as possible.

     Once the button is pressed, an asynchronous Fech request is sent to the server (a more recent and advanced version of XMLHttpRequest), while an XMLHttpRequest is sent to Spoonacular. Then the server takes the necessary steps in order to receive the appropriate recipes from the database and after receiving them to sort them based on their completeness in the ingredients. The recipes are then sent to the client in Json format and displayed conveniently to the user.

     The user now will see a list of recipes, the photo of the food, a link to the recipe site or the description of the recipe, as well as three categories: Missing, Used, Unused. The Missing category shows the ingredients needed in the recipe but the user does not have it, the Used category shows the ingredients needed in the recipe and the user owns it, while the Used category shows the ingredients that are not needed in the recipe and is owned by the user.

     In order to minimize the use of the free API used by the application (because this API allows limited requests to free users), a certain number of recipes are displayed with each search and if the user wants to see more, he can click the "Show" button More ”at the bottom of the page to upload additional recipes.

#### **2.3. Function of the AddRecipe page:** 

     The second most important function of the application is the AddRecipe footer. This page allows the user to add their own recipe to the database. The following fields are available on the page: Title, Image, link, Description, Ingredients. In the Title field the user is asked to enter the title of the recipe, respectively in the Image field the link for a photo of the recipe, in the link field the site from which the recipe was obtained, in the Description field the description of the recipe and in the Ingredients field the ingredients required for its realization. The link field is optional and in case it is left blank, its role is taken by the Description field, thus enabling the user to enter any description he wishes. For the Ingredients field, when the user enters the first component into it, a second identical field appears. This process is repeated each time the user fills in the new field. Finally these fields are sent to the database by pressing the "Send your Recipe" button.

     It should be noted that the user can use this feature only if he has an account in the database and is logged in, which refers us to the next operation of the application

#### **2.4. Login System operation:** 

     As in most applications, for the smooth operation of the application and the control of traffic on the server, it is necessary to use a login system. This system works as follows. If you do not already have an account, the user must first go through the registration process. So when he goes to the Register page (which he can access from the Login page), he is given the opportunity to register in the system by entering his details (username and password). Once he has an account, the user can now log in to the system by going to the Login page. The user can access the Login page by clicking the Login button in the Navigation Bar (Header) at the top of the page and then log in by entering his details in the appropriate fields (username and password).

     It is worth noting that for the sake of confidentiality, the passwords, before being stored in the database, go through a Hashing system of the python werkzeug.security library. When connecting, the two passwords are now compared using the same library in order to verify the user's identity.

#### **2.5. To API:** 

     The application, like most applications of its own, has its own API. In order for the user to access it he must make a GET request on the page " [/ getDbIngredients](https://translate.google.com/translate?hl=en&prev=_t&sl=el&tl=en&u=http://root/getDbIngredients) " with parameter "ingredients". That is, for example, the form: " [http: // root / getDbIngredients? Ingredients = salt, sugar](https://translate.google.com/translate?hl=en&prev=_t&sl=el&tl=en&u=http://root/getDbIngredients%3Fingredients%3Dsalt,sugar) ".

#### **2.6. Scalability:** 

     Thanks to the flexibility of Flask and Javascript, it was possible to separate the project into several independent scripts and folders, which allows the program to be extended and edited in the future.

The Spoonacular API can very easily be replaced in the future by a similar API with minimal changes to the server code.

#### **2.7. Use between different devices:** 

     The final page of the application has been constructed so that it can be used on different types of devices without affecting the appearance. The HTML elements adapt their size and position accordingly in order to appear properly to the user.

### **3\.** A look at the structure of the application folders and files:

The application is structured as shown in the image below:

![](https://user-images.githubusercontent.com/57602090/136194215-d303ebe8-3d05-4a19-819e-abfe7b29b6b7.png)

_Figure (1) - Folder and file structure_

The main folder contains all the Python (.py) files, the database file (.sqlite3), and 2 subfolders. These two subfolders must have the names "static" and "templates" in order for the developer to use all the features of Flask properly. The static folder contains all the css and javascript files and the graphical elements of the application (images). The templates folder contains all the templates that will be used with Flask, ie all the Html files.

### **4\.** Advantages and disadvantages of using Python for Web Developing:

#### **4.1. Advantages:** 

     The main advantage of using Python to develop a Web application is the ease of use of the language itself. Python being a relatively new programming language, provides the user with a huge collection of tools and libraries that allow the developer to personalize it each time according to the needs of its application. Using these tools one can, for example, turn his system into a server in a matter of minutes.

     Also the feature of Python which is the replacement of the brackets with simple empty Tabs, but also the fact that it has made the question marks at the end of the commands unnecessary, make the programming in this language much more relaxed and the code much more readable and as a result easier to be expanded.

     An advantage can also be considered that using Python allows the programmer to learn and practice a programming language that is increasingly used in the world of the labor market.

#### **4.2. Disadvantages:** 

     The main disadvantage of using Python to develop a Web application is the lack of online support (Tutorials, Forums, etc.). Because developing an application in this way is a relatively new method in the world of Web Developing, the content that a programmer can find on the internet is very limited, making the application development process much more difficult and time consuming. For example, if the developer encounters a technical problem or is looking to find an alternative method to implement a piece of code, it should rely mainly on Python, Flask, etc. Documentation.

Another downside is the limited number of Hosting Providers that support Python (such as [www.pythonanywhere.com](https://translate.google.com/translate?hl=en&prev=_t&sl=el&tl=en&u=http://www.pythonanywhere.com/) ).

     One could also consider the need to use the many different Python libraries required to develop a complete Web application as a disadvantage, although I personally find this feature more flexible in software development.

### **5\.** Additional functions: 

     An important function of the application is the way the recipes are sorted on the server before sending them and displaying them to the user. This classification is as follows. Once the desired ingredients arrive on the server, on which the user wants to search for recipes, the server will make the appropriate requests to the database, which will return only the recipes that contain these ingredients by adding them to a list. As for the recipes received from Spoonacular, they are classified in a similar way on the company's servers.

<table><tbody><tr><td><p>for i in range ( 0 , len (ingredientsClientList)):&nbsp;&nbsp;&nbsp;&nbsp;</p><p>&nbsp;&nbsp;&nbsp;&nbsp;recipesDbList + = recipes.query.filter (recipes.ingredients.like ( "%" + ingredientsClientList [i] + "%" )). all ()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p></td></tr></tbody></table>

_Figure (2) - Example of a recipe request from the database_

     It then converts the fields in this list into Python objects and adds 3 more field-lists to each object, usedIngredients, unusedIngredients and missedIngredients. The recipe list then goes through a BubbleShort function that sorts them based on the missedIngredients field , and after converting this object to a Json string, sends the list to the client.

### **6\.** Comparison with alternative techniques: 

     At the moment the application is mainly based on the Spoonacular API (since the local database is empty). However, this API, like most similar APIs available on the Internet, is not completely free. The company that manages it sets a request limit on its server, which it achieves by giving the API user a unique key when creating an account on its page. In case the account exceeds the requirements due to it, some money charges will apply depending on the package selected in the current account.

     The alternative that was originally implemented is Web Scraping. This technique involves some steps aimed at extracting data from various free recipe pages in order. The first step involves reading the source code of the page, the second extracting information from it using specific regular expressions (grep), and the third processing the explained data and storing it in the database. However, this technique also has some disadvantages, which are the reason why it was not used from the beginning in the application.

     The first disadvantage is that there is a risk of exporting incorrect information from the page we are targeting. wrong fields.

     The second disadvantage is that even if the data export works without errors, the slightest change in the source code of the page on the part of its owner, can lead to the collapse of the entire system.

These two are the main reasons why this technology was not used, this of course does not make it impossible to integrate it into the application in the future.

### **7\.** Possible future revenue streams: 

     If the service is used professionally in the future, there may be future revenue streams from it. The most common source of revenue that could be integrated into an application is an in-page ad system.

     Another source of revenue could be charging users who wish to use the application API (something similar to what the company from which the application's API is currently sourced does).

### **8\.** Other services that can stand on the specific service: 

     In addition to the direct use of the application by humans, there are various services-applications, which can stand on it using the services it provides to perform their own functions

     An ideal example is to use the application API from a smart refrigerator. Today's smart refrigerators have a built-in ability to count the ingredients and foods they contain and the automatic purchase of missing products that have been defined as necessary by the user. Using the API of the MyRecipeList page, the smart refrigerator will be able to present the recipes that can be implemented based on the ingredients contained in it, but also to automatically buy the ingredients needed to implement the desired recipes that have been selected. by the owner.

     A similar use to the API example above could be made by an automated system in a supermarket, which would look at what ingredients consumers have bought and suggest additional ingredients they would need in order to make a recipe.

     Another example could be the use of the application API by other similar services, which, however, lack the ability to search for recipes based on ingredients.

### **9\.** Epilogue and conclusions:

     This text was a presentation of the MyRecipeList website, a service that provides its user with the ability to search for recipes based on the ingredients available. The back-end part of this service is implemented in Python, while the front-end part is in Html, Javascript and Css. The user interface of the page is simple and designed to be addressed to all social and age groups who wish to use it. The service currently uses the Spoonacular API but also provides the user with its own API along with the ability to add its own recipe to the system.

     So this service aims to offer help to people who for any reason have limited cooking ingredients but also to enrich the knowledge of many people on cooking thus enabling all its users to enrich their daily recipes with new flavors.
