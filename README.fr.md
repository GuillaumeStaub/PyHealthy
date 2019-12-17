[![Badge langage](https://img.shields.io/static/v1?label=langage&message=Français&color=blue)](https://github.com/GuillaumeStaub/PyHealthy/blob/master/README.fr.md)
[![Badge langage](https://img.shields.io/static/v1?label=langage&message=English&color=blue)](https://github.com/GuillaumeStaub/PyHealthy/blob/master/README.md)
# PyHealthy

# Pourquoi ce programme ?

Cette application, basée sur le Terminal, interroge l'API d'[OpenFoodFacts](https://fr.openfoodfacts.org) afin de trouver un substitut plus sain à un aliment recherché. Donc si si vous voulez trouver un substitut à votre boisson américaine préférée vous avez juste à la renseigner et magie l'application vous retourne un équivalent bien meilleur pour vos kilos en trop. En plus d'afficher le substitut, PyHealthy, vous propose des magasins où le trouver, son NutriScore et un lien vers OFF pour visionner d'avantages d'informations.

# Fonctionnement général

Tout d'abord, il faut récupérer les données, pour cela, j'utilise l'API d'OpenFoodFacts qui est libre et 100% gratuite. La documentation est disponible sur leur [site](https://en.wiki.openfoodfacts.org/API/Read/Search).<br>
Une fois le fonctionnement de l'API bien intégré (après s'être arraché tous les cheveux 😱) j'utilise le module [Requests](https://requests-fr.readthedocs.io/en/latest/) afin d'effectuer la requête vers OFF qui renvoie des données en json. L'application nettoie les données (les données vides) et les mets de côté, elle crée la base de données et y insèrent les données nettoyées. Pour la base de données, j'utilise un ORM [SQLAlchemy](https://www.sqlalchemy.org) communiquant avec une base de données MySQL.

# Visuels

![visual_main_menu](datas/visual.png "Page d'accueil du programme")
<div align="center" font-style='italic'>Page d'accueil du programme.</div>

# Installation
Pour commencer, utilisez le bouton [![clone or download](datas/button.png)](https://github.com/GuillaumeStaub/PyHealthy#branch-select-menu)  sur github et téléchargez ZIP sur votre ordinateur, ou copiez le lien HTTPS et utilisez le terminal sur votre ordinateur et tapez :

`$ git clone https://github.com/GuillaumeStaub/PyHealthy.git `

Vérifiez si python 3 est installé sur votre machine. Pour cela, ouvrez le terminal et tapez :

`$ python3 -V`

Vous devez obtenir quelque chose come :

`Python 3.X.X` 

Si python n'est pas installé sur votre machine, allez sur le site de [Python](https://www.python.org), télécharger **Python 3.X. X** et suivez les instructions.

Si vous êtes utilisateur de Linux, vous pouvez installer Python depuis la console avec la commande `$ sudo apt-get install python3`

Si vous êtes un utilisateur de MacOS, je vous recommande d'utiliser [HomeBrew](https://brew.sh/index_fr) suivez les instructions sur le site pour l'installer puis faites : `$ brew install python3`
## ![Windows_icon](https://img.icons8.com/color/48/000000/windows-logo.png) Pour les utilisateurs de Windows


### ![Mysql_logo](https://img.icons8.com/ios-filled/50/000000/mysql-logo.png) Installer MySQL

1. Rendez-vous sur le site de [MySQL](https://dev.mysql.com/downloads/windows/installer/8.0.html) et téléchargez MySQL, vous n'êtes pas obligés de vous inscrire.
2. Ouvrez l'exe que vous venez de télécharger 
3. Plusieurs options de setup sont proposées, sélectionnez le dernier **Custom**
4. Cliquez sur Next puis Execute
5. Sur la page **MySQL Server Configuration** configurez un mot de passe pour l'utilisateur root qui sera l'utilisateur que nous utiliserons pour le programme. **ATTENTION** mémorisez le ou écrivez le. 
6. Vérifiez le chemin vers MySQL dans votre ordinateur par exemple : `C:\Program Files\MySQL\MySQL Server 5.6\bin` et faites la commande suivante :
   ```
   set PATH=%PATH%;chemin_vers_mysql_bin
   ```
7. Nous allons créer la base de données essentielle à l'utilisation du programme. Rendez-vous dans l'invite de commande et tapez : 
   `mysql -u root -p`
Tapez votre votre mot de passe  et vous voilà connecté à MySQL
8. Nous allons créer la base de données. Pour cela, tapez : 
```SQL
CREATE DATABASE nom_de_votre_base CHARACTER SET 'utf8mb4' COLLATE utf8mb4_bin;
```
**Le `collate utf8mb4_bin` est indispensable au fonctionnement du programme il est essentiel.**

### Initialisation du programme


1. Ouvrez la console et naviguez jusqu'à la racine du projet PyHealthy avec la commande `$ cd \...\Pyhealthy`

2. Tout le fonctionnement du programme est basé sur l'utilisation d'une variable d'environnement contenu dans un fichier **.env**. En effet, c'est à l'intérieur de ce fichier qu'est stockée la constante `DATABASE_URL`.
   1. Dans la console toujours au niveau du dossier racine de PyHealthy tapez `dir > .env`
   2. Ouvrez ce fichier avec un éditeur de texte si des éléments sont déjà présents effacez les 
   3. Maintenant écrire dans le fichier `.env`les éléments suivants : 
   ```
   DATABASE_URL = 'mysql+pymysql://root:votre_mot_de_passe@localhost/nom_de_votre_base_de_données?charset=utf8mb4'
   ```
   4. Sauvegardez et fermez le fichier
   
3. Vérifiez que pipenv est installé sur votre machine avec `$ pipenv --version`si la réponse ressemble à : `pipenv, version 2018.XX.XX`c'est ok. Sinon installez pipenv avec `$ pip install pipenv`
4. Une fois pipenv installé tapez la commande 
   ```
   $ ~\PyHealthy pipenv install
   ```
5. **Si vous démarrez le programme pour la première fois,** vous devez d'abord initialiser la requête, la création de la base de données et son remplissage. Pour cela, assurez-vous bien d'être à la racine de PyHealthy et lancez cette commande: 
    ```bash
    $ ~\PyHealthy pipenv run python home.py --install [--count=100]
    ```
    *[--count]* est optionnel il correspond au nombre de produits que vous souhaitez télécharger d'OpenFoodFact par catégorie. Il est préréglé à 100 produits

6. Vous pouvez maintenant utiliser correctement le programme avec la commande `pipenv run python home.py`

## ![MacOS_icon](https://img.icons8.com/plasticine/48/000000/mac-os.png) Pour les utilisateurs de MacOS

### ![Mysql_logo](https://img.icons8.com/ios-filled/50/000000/mysql-logo.png) Installer MySQL
1. Deux possibilités :
   1. Vous pouvez vous rendre sur le site de MySQL [MySQL](https://dev.mysql.com/downloads/mysql/#downloads) et télécharger le DMG
    2. Ou vous utilisez [HomeBrew](https://brew.sh/)
   ```
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   ```
    pour l'installer. Puis vous faites la commande `$ brew install mysql` pour installer mysql
2. Pour configurer le mot de passe de l'utilisateur root que nous utiliserons pour la suite du programme : `/usr/local/mysql/bin/mysqladmin -u root password votre_mot_de_passe`
3. Pour ceux qui ont installé MySQL via le site de MySQL sans avoir utiliser HomeBrew tapez la commande suivant pour utiliser mysql depuis le terminal :
   ```
   echo 'export PATH=/usr/local/mysql/bin:$PATH' >> ~/.profile
   ```
4. Nous allons créer la base de données essentielle à l'utilisation du programme. Rendez-vous dans l'invite de commande et tapez : 
   `mysql -u root -p`
Tapez votre votre mot de passe  et vous voilà connecté à MySQL
5. Nous allons créer la base de données. Pour cela tapez : 
    ```SQL
    CREATE DATABASE nom_de_votre_base CHARACTER SET 'utf8mb4' COLLATE utf8mb4_bin;
    ```
    **Le `collate utf8mb4_bin` est indispensable au fonctionnement du programme il est essentiel.**
### Initialisation du programme


1. Ouvrez le terminal et naviguez jusqu'à la racine du projet PyHealthy avec la commande `$ cd \...\Pyhealthy`

2. Tout le fonctionnement du programme est basé sur l'utilisation d'une variable d'environnement contenu dans le fichier **.env**. En effet c'est à l'intérieur de ce fichier qu'est stockée la constante `DATABASE_URL`.
   1. Dans la console toujours au niveau du dossier racine de PyHealthy tapez `$ touch .env`
   2. Ouvrez ce fichier avec un éditeur de texte comme vim ou nano au choix `$ vim .env`
   3. Maintenant écrire dans le fichier `.env`les éléments suivants : 
   ```
   DATABASE_URL = 'mysql+pymysql://root:votre_mot_de_passe@localhost/nom_de_votre_base_de_données?charset=utf8mb4'
   ```
   4. Sauvegardez et fermez le fichier
   
3. Vérifiez que pipenv est installé sur votre machine avec `$ pipenv --version`si la réponse ressemble à : `pipenv, version 2018.XX.XX`c'est ok. Sinon installez pipenv avec `$ pip3 install pipenv`
4. Une fois pipenv installé tapez la commande 
   ```
   $ ~\PyHealthy pipenv install
   ```
5. **Si vous démarrez le programme pour la première fois** vous devez d'abord initialiser la requête, la création de la base de données et son remplissage. Pour cela assurez-vous bien d'être à la racine de PyHealthy et lancez cette commande: 
    ```bash
    $ ~\PyHealthy pipenv run python home.py --install [--count=100]
    ```
    *[--count]* est optionnel il correspond au nombre de produits que vous souhaitez télécharger d'OpenFoodFact par catégorie. Il est préréglé à 100 produits

6. Vous pouvez maintenant utiliser correctement le programme avec la commande `pipenv run python home.py`

## ![Linux_icon](https://img.icons8.com/color/48/000000/linux.png) Pour les utilisateurs de Linux

### ![Mysql_logo](https://img.icons8.com/ios-filled/50/000000/mysql-logo.png) Installer MySQL
#### ![Debian_icon](https://img.icons8.com/color/30/000000/debian.png )Sous Debian ou ![Ubuntu_icon](https://img.icons8.com/color/30/000000/ubuntu--v1.png)Ubuntu
- Exécutez la commande suivante :
   ```
   sudo apt-get install mysql-server mysql-client
   ```
### ![RedHat_icon](https://img.icons8.com/windows/30/000000/redhat.png)Sous RedHat
- Executez la commande suivante
    ```
    sudo yum install mysql mysql-server
    ```
Dans tous les cas pour initialiser le mot de passe de l'utilisateur root que vous utiliserons pour la suite du programme tapez la commande suivant : 
```
sudo mysqladmin -u root -h localhost password votre_mot_de_passe
```
1. Nous allons créer la base de données essentielle à l'utilisation du programme. Rendez-vous dans l'invite de commande et tapez : 
   `mysql -u root -p`
Tapez votre votre mot de passe  et vous voilà connecté à MySQL
2. Nous allons créer la base de données. Pour cela tapez : 
    ```SQL
    CREATE DATABASE nom_de_votre_base CHARACTER SET 'utf8mb4' COLLATE utf8mb4_bin;
    ```
    **Le `collate utf8mb4_bin` est indispensable au fonctionnement du programme il est essentiel.**
### Initialisation du programme


1. Ouvrez le terminal et naviguez jusqu'à la racine du projet PyHealthy avec la commande `$ cd \...\Pyhealthy`

2. Tout le fonctionnement du programme est basé sur l'utilisation d'une variable d'environnement contenu dans le fichier **.env**. En effet c'est à l'intérieur de ce fichier qu'est stockée la constante `DATABASE_URL`.
   1. Dans la console toujours au niveau du dossier racine de PyHealthy tapez `$ touch .env`
   2. Ouvrez ce fichier avec un éditeur de texte comme vim ou nano au choix `$ vim .env`
   3. Maintenant écrire dans le fichier `.env`les éléments suivants : 
   ```
   DATABASE_URL = 'mysql+pymysql://root:votre_mot_de_passe@localhost/nom_de_votre_base_de_données?charset=utf8mb4'
   ``` 
   4. Sauvegardez et fermez le fichier
   
3. Vérifiez que pipenv est installé sur votre machine avec `$ pipenv --version`si la réponse ressemble à : `pipenv, version 2018.XX.XX`c'est ok. Sinon installez pipenv avec `$ pip3 install pipenv`
4. Une fois pipenv installé tapez la commande 
   ```
   $ ~\PyHealthy pipenv install
   ```
5. **Si vous démarrez le programme pour la première fois** vous devez d'abord initialiser la requête, la création de la base de données et son remplissage. Pour cela assurez-vous bien d'être à la racine de PyHealthy et lancez cette commande: 
    ```bash
    $ ~\PyHealthy pipenv run python home.py --install [--count=100]
    ```
    *[--count]* est optionnel il correspond au nombre de produits que vous souhaitez télécharger d'OpenFoodFact par catégorie. Il est préréglé à 100 produits

6. Vous pouvez maintenant utiliser correctement le programme avec la commande `pipenv run python home.py`

# Compétences mobilisées

- Sélectionner les langages de programmation adaptés pour le développement de l'application **(Python is the best of Course!)**
- Travailler avec une méthodologie de projet agile **(Trello et RDD)**
- Implémenter le schéma de données dans la base
- Respecter les bonnes pratiques de développement en vigueur
- Manipuler les données à l'aide d'un ORM
- Manipuler une API REST à l'aide de Requests

# Fonctionnalités de l'application

## <span style="color: #26B260"> Install </span>

### Product Downloader

Ce package a plusieurs fonctionnalités qui s'occupent notamment de récupérer les données via l'API. L'instanciation du package permet d'initialiser les paramètres dès la requête et d'accéder aux fonctionnalités suivantes :

- `recover_product()` : fonctionnalité qui s'occupe d'interroger OFF à l'aide du module requests. Pour les paramètres de la requête ils sont directement intégrés au package Product Downloader et les éléments variables (page_size, category) sont stockés dans les constantes.

- `add_categroy(product:list)`: les données d'OFF ne répondent pas à 100% de nos besoins, en effet les catégories sont trop précises et nous permettent pas un classement général des produits. Cette fonctionnalité prend en paramètre une liste de dictionnaires avec chaque dictionnaire qui correspond à un produit. On ajoute à chaque produit la clé `main_category` et en valeur la catégorie correspondante. Cela nous permettra un classement plus général de nos produits dans la BDD

### Product Cleaner

Ce package est très simple il prend en entrée les données brutes téléchargées , il les nettoie et vérifie si certaines données ne sont pas manquantes auquel cas il abandonnera le produit. Le package renvoie une liste de données nettoyées prêtes à être insérées dans la base.

- `is_valid()` Cette fonctionnalité permet de vérifier si une donnée voulue est vide ou non. Il prendra en entrée une données d'un produit et renvoie `True` si la donnée est présente sinon `False`
- `clean_product()` Cette fonctionnalité récupère les données brutes contenues dans l'instanciation du package, et parcourt tous les produits un par un . Sur chaque produit elle utilise la fonction `is_valid()` si `True` est retourné elle récupère les données qui nous intéressent et renvoie un dictionnaire pour chaque produit et l'ajoute à la liste des produits nettoyés. Si c'est `False` qui est renvoyé le produit est abandonné.

### Install

Ce package est plutôt complexe il gère toute l'initialisation des packages précédents, mais aussi la construction de la base de données via l'ORM SQLAlchemy. Install gère beaucoup de choses, dans son initialisation il télécharge les données OFF, les nettoie, créé toutes les tables de la BDD, se connecte à la BDD et initialise une session qui servira d'intermédiaire entre le programme et la BDD notamment pour y insérer des données.

- `create_bdd()` Cette fonctionnalité permet de créer toutes les tables requises de la base de données.
- `generate_category()` Permet de récupérer la catégorie de chaque produit. La catégorie a une contrainte unique sur son nom, cette méthode vérifie donc d'abord si la catégorie est déjà dans la base via un dictionnaire intermédiaire.
- `generate_stores()` Ici le programme récupère la liste des magasins contenus dans chaque produit, pour chaque magasin il vérifie si le magasin n'est pas déjà dans la base grâce encore à un dictionnaire intermédiaire, si le magasin n'y est pas il l'instancie et l'ajoute à la session de mappage s'il y est déjà il récupère les éléments du magasins contenus dans le dictionnaire intermédiaire. Dans tous les cas `generate_stores()`rattache un produit à tous les magasins qu'il contient, et inversement grâce à une table intermédiaire configurée dans les constantes. `store_product`
- `load_datas_db()` Parcourt tous les produits contenus dans la liste de données nettoyées, appel les fonctionnalités `generate_category()` et `generate_stores()`, instancie chaque Produit et commit toutes les données dans la BDD.
- `main()` Fonctionnalité principale de l'installation. Instancie toutes les classes nécessaires à l'installation.

### Progress Bar

Ce package sert simplement à initialiser une barre de chargement pendant que les données se téléchargent et s'intègrent dans la BDD. C'est donc un package qui contient des fonctionnalités asynchrones grâce au module Threading. L'initialisation du package contient un calcul représentant un taux moyen de traitement pour un produit.

- `run()` Une boucle for qui a chaque tour fait avancer la barre de chargement. Le temps de chargement est calculé grâce au calcul réalisé à l'initialisation.

--------------------------------------------------------------------------------

## <span style="color: #26B260"> DataBase </span>

### Product

Ce package représente la Table **product** de la base de données, elle contient un _id_, _name_, _nutriscore_, _url_, _category_id_. Elle contient également une relation entre produit et store via une table intérmédiaire. _category_id_ est une clé étrangère qui pointe vers la table catégorie. Chaque produit appartient à une seule catégorie.

- `select_products(session, category)` Requête viaSQLAlchemy, qui permet de retourner 10 produits au hasard correspondant à une catégorie.
- `find_healthy(session, fat_product, category_)`Requête qui retourne un produit de la même catégorie que celui préalablement sélectionné par l'utilisateur avec unnutriscoreplus faible
- `load_product(product_id, session)` Requête qui renvoie un produit en fonction de l'idpassé en paramètre

### Category

Ce package représente la Table **category** avec son _id_ et son _name_.

- `select_categories(session)` Requête qui récupère toutes les catégories de la table catégorie

### Store

Ce package représente la Table **store** avec son _id_ et son _name_.

### Favorites

Ce package représente la Table **favorites** avec son _id_ et les _id_ du produit substitué et du substitut.

- `select_favorites(session)` Requête qui retourne tous les favoris de la table favoris

--------------------------------------------------------------------------------

## <span style="color: #26B260"> User Interface </span>

### Client

Ce package contient toutes les fonctionnalités qui vont permettre d'interagir avec l'utilisateur. Chaque méthode de la classe Client correspond à un "menu" de l'UI. L'utilisateur va alors pouvoir donner des instructions au programme en choisissant la catégorie, le produit, d'afficher ses favoris.

- `home()` Cette fonctionnalité est le "menu principal" de l'application qui propose à l'utilisateur deux options, substituer un produit ou accéder à ses favoris.
- `category_choice()` Cette fonctionnalité permet à l'utilisateur de sélectionner la catégorie de son choix. La requête de la table catégorie est utilisée ensuite l'id et le nom de la catégorie sont associés dans un dictionnaire. L'utilisateur peut ainsi sélectionner celle de son choix à l'aide de l'id . Cette méthode retourne l'id choisit par l'utilisateur
- `product_choice()` Ici, cette méthode utilise la requête `select_products()` pour récupérer 10 produits au hasard selon la catégorie sélectionnée par l'utilisateur. La méthode affiche les 10 produits en les associant à un chiffre. L'utilisateur sélectionne le produit en tapant le chiffre correspondant. La fonctionnalité retourne la réponse.
- `substitue()` Cette méthode est le cœur du programme. En effet, ici, le programme interroge la base de données pour trouver un produit dans la même catégorie que celui sélectionné par l'utilisateur, mais avec un nutriscore plus faible. Puis l'utilisateur a le choix de sauvegarder le résultat avec `save_products()`, de retourner au menu principal ou de quitter le programme.
- `load()` et `display_favorites()` Ces fonctionnalités permettent de charger tous les favoris et de les afficher, ainsi l'utilisateur peut consulter les précédentes substitutions qu'il a sauvegardé

### Menu

Menu est une surcouche de client, il facilite la navigation entre les menus. En effet grâce à menu, l'utilisateur peut naviguer de menu en menu même avec la possibilité de revenir en arrière. Tous les menus de Client sont contenus dans un dictionnaire et l'utilisateur peut aller et venir entre les menus.

--------------------------------------------------------------------------------

## <span style="color: #26B260"> Home </span>
### Home
C'est le package qui initialise tout le programme. Le module click est utilisé pour permettre de lancer soit l'initialisation du programme (requête OFF, construction de la base de données, intégration des données) avec la commande `--install` ou de lancer le client. Des sécurités sont mises en place pour éviter à l'utilisateur de faire des manipulations qui pourraient causer des dommages au programme.

# Contibuer au programme 

* Fork le
* Créez votre banche `git checkout -b my-new-feature`
* Commit les changements `git commit -am 'Add some feature'`
* Push ta branche `git push origin my-new-feature`
* Créez une Pull Request