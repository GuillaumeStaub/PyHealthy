[![Badge langage](https://img.shields.io/static/v1?label=langage&message=Français&color=blue)](https://github.com/GuillaumeStaub/PyHealthy/blob/master/README.fr.md)
[![Badge langage](https://img.shields.io/static/v1?label=langage&message=Anglais&color=blue)](https://github.com/GuillaumeStaub/PyHealthy/blob/master/README.md)
# PyHealthy

## Why this program?

This application, based on the Terminal, queries the [OpenFoodFacts](https://fr.openfoodfacts.org) API to find a healthier substitute for a desired food. So if you want to find a substitute for your favorite American drink you just have to fill it in and the magic app returns you a much better counterpart for your extra pounds. In addition to displaying the substitute, PyHealthy, offers stores where to find it, its NutriScore and a link to OFF to view more information.

# General operation

First of all, you have to recover the data, for that I use the OpenFoodFacts API which is free and 100% free. The documentation is available on their website [website](https://en.wiki.openfoodfacts.org/API/Read/Search) . Once the operation of the API is well integrated (after having ripped all the hair 😱) I use the module [Requests](https://requests-fr.readthedocs.io/en/latest/) to make the request to OFF which returns data in json. The application cleans the data (empty data) and sets it aside, creates the database and inserts the cleaned data into it. For the database, I use a [SQLAlchemy](https://www.sqlalchemy.org) ORM communicating with a MySQL database.

# Visual

![visual_main_menu](datas/visual.png "Page d'accueil du programme")
<div align="center" font-style='italic'>Program Homepage.</div>

# Installation

To start, use the ![clone or download](datas/button.png) button on github and download ZIP to your computer, or copy the HTTPS link and use the terminal on your computer and type:
```
$ git clone https://github.com/GuillaumeStaub/PyHealthy.git
```
Check if python 3 is installed on your machine. To do this, open the terminal and type:

`$ python3 -V`

You have to get something like:

`Python 3.XX`

If python is not installed on your machine, go to the [Python](https://www.python.org) website, download  **Python 3.X. X** and follow the instructions.

If you are a Linux user, you can install Python from the console with the command `$ sudo apt-get install python3`

If you are a MacOS user, I recommend you use [HomeBrew](https://brew.sh/index_fr) follow the instructions on the site to install it then do: `$ brew install python3`
 ## ![Windows_icon](https://img.icons8.com/color/48/000000/windows-logo.png) For Windows users

### ![Mysql_logo](https://img.icons8.com/ios-filled/50/000000/mysql-logo.png) Install MySQL

1. Go to the [MySQL](ttps://dev.mysql.com/downloads/windows/installer/8.0.html) website and download MySQL, you do not have to register.
2. Open the exe you just downloaded
3. Several setup options are available, select the last  **Custom**
4. Click Next and then Execute
5. On the  **MySQL Server Configuration** page, set a password for the root user who will be the user we will use for the program.  **CAUTION** memorize or write it.
6. Check the path to MySQL in your computer for example: `C:\ProgramFiles\MySQL\MySQL Server 5.6\bin` and issue the following command: 
   ```
    set PATH =% PATH%; path\_to\_mysql\_bin
    ```
7. We will create the essential database for the use of the program. Go to the command prompt and type: 
   `mysql -u root -p` 
   Type your password and you're connected to MySQL
8.  We will create the database. To do this, type:
    ```SQL
    CREATE DATABASE name_of_your_database CHARACTER SET 'utf8mb4' COLLATE utf8mb4_bin;
    ```
    **The `collate utf8mb4_bin` is essential to the operation of the program it is essential.**

### Initializing the program

1. Open the console and navigate to the root of the PyHealthy project with the command `$ cd \ ... \ Pyhealthy`
   
2. All the operation of the program is based on the use of an environment variable contained in an  **.env** file . Indeed, it is inside this file that is stored constant `DATABASE_URL` :
   1. In the console still at the root folder of PyHealthy type `dir > .env`
   2. Open this file with a text editor if items are already present erase them
   3. Now write the following in the `.env` file : 
   ```
   DATABASE_URL = 'mysql+pymysql://root:votre_mot_de_passe@localhost/name_of_your_databse?charset=utf8mb4'
   ```
   1. Save and close the file
3. Check that pipenv is installed on your machine with `$ pipenv --version` if the answer looks like: `pipenv, version 2018.XX.XX` it's ok. Otherwise install pipenv with `$ pip install pipenv`
4. Once pipenv installed type the command 
   ```
   $ ~\PyHealthy pipenv install
   ```
5.  **If you start the program for the first time,** you must first initialize the query, create the database, and then fill it. For that, make sure you are at the root of PyHealthy and run this command: 
    ```bash
    $ ~\PyHealthy pipenv run python home.py --install [--count=100]
    ```
    *[--count]* is optional it matches the number of products you want to download from OpenFoodFact by category. It is preset to 100 products
6.  You can now use the program correctly with the command `pipenv run python home.py`

## ![MacOS_icon](https://img.icons8.com/plasticine/48/000000/mac-os.png) For MacOS users

### ![Mysql_logo](https://img.icons8.com/ios-filled/50/000000/mysql-logo.png) Install MySQL

1. Two possibilities :
   1. You can go to the MySQL [MySQL site](https://dev.mysql.com/downloads/mysql/#downloads) and download the DMG
   2. Or you use [HomeBrew](https://brew.sh/) use 
   ```
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   ```
    to install it. Then you make the command `$ brew install mysql to install mysql`to install mysql
2. To configure the password of the root user that we will use for the rest of the program: `/usr/local/mysql/bin/mysqladmin -u root password your_password`
3. For those who have installed MySQL via the MySQL site without using HomeBrew type the following command to use mysql from the terminal:
    ```
   echo 'export PATH=/usr/local/mysql/bin:$PATH' >> ~/.profile
   ```
4. We will create the essential database for the use of the program. Go to the command prompt and type: 
   `mysql -u root -p` 
   Type your password and you're connected to MySQL
5. We will create the database. To do this type: 
   ```SQL
    CREATE DATABASE name_your_database CHARACTER SET 'utf8mb4' COLLATE utf8mb4_bin;
    ```
     **The  utf8mb4_bin collate is essential to the operation of the program it is essential.** 

### Initializing the program

1. Open the terminal and navigate to the root of the PyHealthy project with the command `$ cd \ ... \ Pyhealthy`
   
2. The entire operation of the program is based on the use of an environment variable contained in the  **.env** file . Indeed it is inside this file that is stored constant `DATABASE_URL`.
   1.  In the console still at the root folder of PyHealthy type `$ touch .env`
   2.  Open this file with a text editor like vim or nano to choose `$ vim .env`
   3.  Now write the following in the `.env` file :  
   ```
   DATABASE_URL = 'mysql+pymysql://root:votre_mot_de_passe@localhost/name_of_your_database?charset=utf8mb4'
   ```
   4.  Save and close the file
3.  Check that pipenv is installed on your machine with` $ pipenv --version` if the answer looks like: `pipenv, version 2018.XX.XX` it's ok. Otherwise install pipenv with `$ pip3 install pipenv`
4.  Once pipenv installed type the command 
    ```
    $ ~ \ PyHealthy pipenv install
    ```
5.  **If you start the program for the first time** you must first initialize the query, create the database and fill it. For that make sure to be at the root of PyHealthy and run this command: 
     ```bash
     $ ~\PyHealthy pipenv run python home.py --install [--count=100]
     ```
    *[--count]* is optional it corresponds to number of products you want to download from OpenFoodFact by category. It is preset to 100 products
6.  You can now use the program correctly with the command `pipenv run python home.py`

## ![Linux_icon](https://img.icons8.com/color/48/000000/linux.png) For Linux Users

### ![Mysql_logo](https://img.icons8.com/ios-filled/50/000000/mysql-logo.png) Install MySQL
#### ![Debian_icon](https://img.icons8.com/color/30/000000/debian.png ) Debian or ![Ubuntu_icon](https://img.icons8.com/color/30/000000/ubuntu--v1.png)Ubuntu

* Run the following command: 
  ```
  sudo apt-get install mysql -server mysql-client 
  ```
  
### RedHat

* Execute the following command 
  ```
  sudo yum install mysql mysql-server
  ```
In any case to initialize the password of the root user that you will use for the continuation of the program type the following command:
```
sudo mysqladmin -u root -h localhost password your_password
```             

1. We will create the essential database for the use of the program. Go to the command prompt and type: 
   `mysql -u root -p`
    Type your password and you're connected to MySQL
2. We will create the database. To do this type: 
    ```SQL
    CREATE DATABASE name_of_your_database CHARACTER SET 'utf8mb4' COLLATE utf8mb4_bin;
    ```
**The `utf8mb4_bin collate`  is essential to the operation of the program it is essential.** 

### Initializing the program
1. Open the terminal and navigate to the root of the PyHealthy project with the command `$ cd \ ... \ Pyhealthy`
   
2. The entire operation of the program is based on the use of an environment variable contained in the  **.env** file . Indeed it is inside this file that is stored constant `DATABASE_URL`.
   1.  In the console still at the root folder of PyHealthy type `$ touch .env`
   2.  Open this file with a text editor like vim or nano to choose `$ vim .env`
   3.  Now write the following in the `.env` file :  
   ```
   DATABASE_URL = 'mysql+pymysql://root:votre_mot_de_passe@localhost/name_of_your_database?charset=utf8mb4'
   ```
   4.  Save and close the file
3.  Check that pipenv is installed on your machine with` $ pipenv --version` if the answer looks like: `pipenv, version 2018.XX.XX` it's ok. Otherwise install pipenv with `$ pip3 install pipenv`
4.  Once pipenv installed type the command 
    ```
    $ ~ \ PyHealthy pipenv install
    ```
5.  **If you start the program for the first time** you must first initialize the query, create the database and fill it. For that make sure to be at the root of PyHealthy and run this command: 
    ```bash
    $ ~\PyHealthy pipenv run python home.py --install [--count=100]
    ```
    *[--count]* is optional it corresponds to number of products you want to download from OpenFoodFact by category. It is preset to 100 products
6.  You can now use the program correctly with the command `pipenv run python home.py`


# Mobilized skills

* Select the appropriate programming languages ​​for application development **(Python is the best of Course!)**

* Work with an agile project methodology **(Trello and RDD)**

* Implement the data schema in the database

* Respect good development practices in force

* Manipulate data using an ORM

* Manipulate a REST API using Requests

# Features of the application

## Install

### Product Downloader

This package has several features that include the recovery of data via the API. The instantiation of the package makes it possible to initialize the parameters as soon as the request and to have access to the following functionalities:

* `recover_product ()` : A feature that queries OFF using the requests module. For the parameters of the query they are directly integrated into the Product Downloader package and the variable elements (page_size, category) are stored in the constants.

* `add_categroy (product: list)` : the OFF data do not meet 100% of our needs, because the categories are too precise and do not allow us a general classification of the products. This feature takes as parameter a list of dictionaries with each dictionary that corresponds to a product. We add to each product the key `main_category` and value the corresponding category. This will allow us a more general classification of our products in the BDD

### Product Cleaner

This package is very simple, it takes as input the raw data downloaded, it cleans them and checks if some data are not missing in which case it will abandon the product. The package returns a list of cleaned data ready to be inserted into the database.

* `is_valid ()` This function is used to check whether a desired data is empty or not. It will take as input a data of a product and return `True` if the data is present otherwise `False`
* `clean_product ()` This function retrieves the raw data contained in the instantiation of the package, and browses all the products one by one. On each product it uses the `is_valid ()` function. If `True` is returned it retrieves the data of interest to us and returns a dictionary for each product and adds it to the list of cleaned products. If it is `False` that is returned the product is abandoned.

### Install

This package is rather complex, it manages all the initialization of the previous packages, but also the construction of the database via the ORM SQLAlchemy. Install manages many things, in its initialization it downloads the data OFF, cleans them, creates all the tables of the BDD, connects to the BDD and initiates a session which will serve as intermediary between the program and the BDD in particular to insert Datas.

* `create_bdd ()` This feature allows you to create all the required tables in the database.

* `generate_category ()` Retrieves the category of each product. The category has a unique constraint on its name, so this method first checks whether the category is already in the database via an intermediate dictionary.

* `generate_stores ()` Here the program retrieves the list of stores contained in each product, for each store it checks if the store is not already in the database thanks to an intermediate dictionary, if the store is not there instantiates and adds it to the mapping session if there is already it retrieves the elements of the magazines contained in the intermediate dictionary. In all cases, `generate_stores ()` attaches a product to all the stores it contains, and vice versa thanks to an intermediate table configured in the constants. `store_product`

* `load_datas_db ()` Scrolls through all the products in the cleaned data list, calls the `generate_category ()` and `generate_stores ()` functions , instantiates each Product, and commits all data to the DB.

* `main ()` Main feature of the installation. Instantiates all classes needed for installation.

### Progress Bar

This package simply serves to initialize a loading bar while the data is loading and integrating into the DB. It is therefore a package that contains asynchronous features thanks to the Threading module. The initialization of the package contains a calculation representing an average rate of treatment for a product.

* `run ()` A for loop that has each turn advance the load bar. The loading time is calculated thanks to the calculation carried out at initialization.

----

## DataBase

### Product

This package represents the  **product** table of the database, it contains an *id*, *name*, *nutriscore*, *url*, *category_id*. It also contains a relationship between product and store via an intermediary table. *category_id* is a foreign key that points to the category table. Each product belongs to a single category.

* `select_products (session, category)` Query viaSQLAlchemy, which returns 10 random products corresponding to a category.

* `find_healthy (session, fat_product, category_)` Query that returns a product of the same category as the one previously selected by the user with a smaller numerictrouble

* `load_product (product_id, session)` Query that returns a product based on the idpassed parameter

### Category

This package represents the Table  **category** with its *id* and *name*.

* `select_categories (session)` Query that retrieves all categories from the category table

### Store

This package represents the Table  **store** with its *id* and *name*.

### Favorite

This package represents the table  **favorites** with its *id* and the *id* of the substituted product and the substitute.

* `select_favorites (session)` Query that returns all favorites from the favorites table

## User Interface

### Customer

This package contains all the features that will allow to interact with the user. Each method of the Client class corresponds to a "menu" of the UI. The user will then be able to give instructions to the program by choosing the category, the product, to display his favorites.

* `home ()` This feature is the "main menu" of the application that offers the user two options, substitute a product or access his favorites.

* `category_choice ()` This feature allows the user to select the category of their choice. The query from the category table is then used, and the id and category name are associated in a dictionary. The user can thus select the one of his choice using the id. This method returns the id chosen by the user

* `product_choice ()` Here, this method uses the `select_products ()` query to retrieve 10 random products based on the category selected by the user. The method displays the 10 products by associating them with a number. The user selects the product by typing the corresponding number. The feature returns the answer.

* `substitue ()` This method is the heart of the program. Indeed, here, the program queries the database to find a product in the same category as that selected by the user, but with a lower nutriscore. Then the user has the choice to save the result with `save_products ()`, return to the main menu or exit the program.

* `load ()` and `display_favorites ()` These features allow to load all the favorites and to display them, so the user can consult the previous substitutions that he saved.

### Menu

Menu is a client overlay, it facilitates navigation between menus. Indeed thanks to menu, the user can navigate from menu to menu even with the possibility to go back. All Client menus are contained in a dictionary and the user can move back and forth between the menus.

## Home

### Home

This is the package that initializes the entire program. The click module is used to start either program initialization (OFF query, database build, data integration) with the `--install` command or to launch the client. Safeties are put in place to prevent the user from doing manipulations that could cause damage to the program.

# Contribute to the program 

* Fork it
* Create your feature branch (`git checkout -b my-new-feature`)
* Commit your changes (`git commit -am 'Add some feature'`)
* Push to the branch (`git push origin my-new-feature`)
* Create new Pull Request