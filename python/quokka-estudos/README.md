## Quokka is dead! Long live the Quokka!

Hi,

QuokkaCMS growed in to an amazing project and there are many users using the currrent version.

The problem is that too many feature requests lead in to too many issues to fix and implement.

The lack of contributors lead in to a slow pace development.

So I decided to kill this version! and start a brand new one[1] which is going to be more simple and many things will be moved in to external plugins.

So I'll need to maintain only the small core of the CMS and plugins would be maintained by community.

I am also removing the MongoDB dependency (it will be optional)

If you want to follow the Quokka Rewrite please take a look in to temporary repository [1] and once it is ready to release I'll archive this existing version in another branch and replace `master` branch of this repo with the new CMS.

The existing codebase will be kept in another branch but will not be actively maintained, only hotfixes and community PRs will be accepted, but the evolution of the project will be focused in `quokka new generation`

[1]  https://github.com/rochacbruno/quokka_ng/blob/master/README.md

Suggestions please use the issues on the new repo.


Cheers!

Long live the Quokka!!!










----------------------------------


[![Flask Registered](https://img.shields.io/badge/flask-registered-green.svg?style=flat)](https://github.com/pocoo/metaflask)
[![Travis CI](http://img.shields.io/travis/quokkaproject/quokka.svg)](https://travis-ci.org/quokkaproject/quokka)
[![Coverage Status](https://coveralls.io/repos/github/quokkaproject/quokka/badge.svg?branch=development)](https://coveralls.io/github/quokkaproject/quokka?branch=development)
[![Code Health](https://landscape.io/github/quokkaproject/quokka/development/landscape.svg?style=flat)](https://landscape.io/github/quokkaproject/quokka/development)
[![Updates](https://pyup.io/repos/github/quokkaproject/quokka/shield.svg)](https://pyup.io/repos/github/quokkaproject/quokka/)


[![Stories in Ready](https://badge.waffle.io/quokkaproject/quokka.png?label=ready&title=Ready)](http://waffle.io/quokkaproject/quokka)
[![irc #quokkaproject](https://img.shields.io/badge/IRC-%23quokkaproject-green.svg?style=flat)](http://webchat.freenode.net/?channels=%23quokkaproject&uio=d4)

[![Twitter](http://img.shields.io/badge/twitter-@quokkaproject-green.svg)](http://twitter.com/quokkaproject)
<a href="http://smallactsmanifesto.org" title="Small Acts Manifesto"><img src="http://smallactsmanifesto.org/static/images/smallacts-badge-80x15-blue.png" style="border: none;" alt="Small Acts Manifesto" /></a>
<a target="_blank" href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&amp;business=rochacbruno%40gmail%2ecom&amp;lc=BR&amp;item_name=quokkaproject&amp;no_note=0&amp;currency_code=USD&amp;bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHostedGuest"><img alt='Donate with Paypal' src='http://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif' /></a>

[![wercker status](https://app.wercker.com/status/e9cbc4497ee946083aa19fbd3f756c91/m "wercker status")](https://app.wercker.com/project/bykey/e9cbc4497ee946083aa19fbd3f756c91)
[![Launch on OpenShift](http://launch-shifter.rhcloud.com/button.svg)](https://openshift.redhat.com/app/console/application_type/custom?cartridges%5B%5D=python-2.7&cartridges%5B%5D=mongodb-2.4&initial_git_url=https://github.com/quokkaproject/quokka.git&name=quokka&initial_git_branch=master)

Quokka project
===============================================

### Flask and MongoDB powered CMS

<p align="center">
<img src="docs/logo.png" alt="quokka cms" />
</p>


Quokka is a flexible content management platform powered by Python, Flask and MongoDB.

You can use Quokka CMS to publish a blog, a web portal, intranet, document management system and you can install existing quokka-modules such as quokka-cart to create an e-commerce app or you can easily create a new quokka-module to fit your needs.

#### Quokka Dashboard (based in Flask-Admin)

<p align="center">
<img src="docs/quokka_dashboard_content.png" alt="quokka cms admin content dashboard" />
</p>


> Quokka runs on Python 2.7  (Python 3 support is being developed)


## See yourself

User 'admin@example.com' and passwd 'admin' to login in to /admin

- Development Demo: http://development.quokkaproject.org  (unstable - development branch)


# Get Quokka


# Using Docker

The easiest way to run Quokka for development or production is using quokkaCMS + Gunicorn + Supervisor under a Docker Container. You can see the instructions in the following repository: https://github.com/quokkaproject/docker-gunicorn-supervisor


##  Get Quokka to run locally for development or deployment

```bash
git clone https://github.com/quokkaproject/quokka --branch master --single-branch
cd quokka
```

> if you are cloning to contribute to the project just clone it without the "--branch=master --single-branch" part

### Run Quokka

Install needed packages in your local computer

You can install everything you need in your local computer or if preferred use a virtualenv for Python

#### Mongo

* Quokka requires a MongoDB instance running to connect.

    1. If you don't have a MongoDB instance running, you can quickly configure it:

        * Download from [here](https://www.mongodb.org/downloads)
        * Unzip the file
        * Open a separate console
        * Run it inside the MongoDB directory:
        ```bash
        ./bin/mongod --dbpath /tmp/
        ```
        > WARNING: If you want to persist the data, give another path in place of ```--dbpath /tmp```


    2. If you already have, just define your MongoDB settings:
        ```bash
        $ $EDITOR quokka/local_settings.py
        ===============quokka/quokka/local_settings.py===============
        MONGODB_DB = "yourdbname"
        MONGODB_HOST = 'your_host'
        MONGODB_PORT = 27017
        MONGODB_USERNAME = None
        MONGODB_PASSWORD = None
        =============================================================
        
        # You can also use envvars `export QUOKKA_MONGO_DB="yourdbname"` 
        ```

    3. If you have Docker installed you can simply run the official Mongo image
        ```bash
        cd quokka
        docker run -d -v $PWD/etc/mongodata:/data/db -p 27017:27017 mongo
        ```

#### O.S Requirements (optional)

* O.S Requirements (for media conversions) you may need the following requirements on your operating system

    1. Ubuntu/Debian
        ```bash
        sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev
        ```
    2. Alpine Linux
        ```bash
        apk add gcc python py-pip libjpeg zlib zlib-dev tiff freetype git py-pillow python-dev musl-dev
        ```
    3. RedHat & Fedora
       ```bash
       sudo yum install libtiff-devel libjpeg-devel zlib-devel freetype-devel python-devel
       ```

#### Python requirements
Install all needed python packages

> If you have a virtualenv, activate it! `source env/bin/activate` or `workon env`

```bash
pip install -r requirements/requirements.txt
```

#### Create admin user, sample data and run!

* Initial data, users and running commands


    3. Create a superuser  (required to login on admin interface)
        ```bash
        $ manage accounts_createsuperuser
        you@email.com
        P4$$W0Rd
        ```

    4. Populate with sample data (optional if you want sample data for testing)
        ```bash
        $ manage populate

        ```
        > credentials for /admin will be email: admin@example.com passwd: admin

    5. Run
        ```bash
        $ manage runserver --host 0.0.0.0 --port 5000
        ```
        - Site on [http://localhost:5000](http://localhost:5000)
        - Admin on [http://localhost:5000/admin](http://localhost:5000/admin)
        

## Deployment

Check ``wsgi.py``, ``wsgi_gunicorn.py`` and scripts under /etc folder for deployment options or check documentation

## DOCS
Documentation is not complete yet, but is being written at:

http://quokkaproject.org/documentation

> If you want to help writing the docs please go to https://github.com/quokkaproject/quokkaproject.github.io


Also there is a [Wiki](https://github.com/quokkaproject/quokka/wiki)
===============================================

> NOTE: the content from wiki will be moved to /documentation

* [About & Features](https://github.com/quokkaproject/quokka/wiki/about)
* [Installing and running](https://github.com/quokkaproject/quokka/wiki/installation)
* [Requirements](https://github.com/quokkaproject/quokka/wiki/requirements)
* [Extending & Installing modules](https://github.com/quokkaproject/quokka/wiki/plugins)
* [Admin interface](https://github.com/quokkaproject/quokka/wiki/screencast)
* [Project tree](https://github.com/quokkaproject/quokka/wiki/project-tree)
* [Team & Committers](https://github.com/quokkaproject/quokka/graphs/contributors)


Hosting
=======

You can host a Quokka website in any VPS or cloud which supports Python and Flask + MongoDB access, a good option is to host the database in MongoLab if your hosting server does not provide Mongo.

- PythonAnywhere can run Quokka with Mongo hosted at MongoLab
- DigitalOcean is a good option for a VPS
- Jelastic Cloud has the easiest Quokka deployment - http://docs.jelastic.com/ru/quokka-cms
- OpenShift [one click deploy](https://openshift.redhat.com/app/console/application_type/custom?cartridges%5B%5D=python-2.7&cartridges%5B%5D=mongodb-2.4&initial_git_url=https://github.com/quokkaproject/quokka.git&name=quokka&initial_git_branch=master)


![python](docs/python_powered.png)
&nbsp;
![flask](docs/flask_powered.png)
&nbsp;
![mongo](docs/mongo_powered.jpg)
&nbsp;

## Details and Features

#### Bit.ly integration

Quokka has Bit.ly integration to short post urls. In quokka/settings.py you can find the details of how
to configure with your data. Check both items: ```SHORTENER_SETTINGS``` and ```SHORTENER_ENABLED```. By default
the shortener is disable, but you can change it putting True in the ```SHORTENER_ENABLED``` config.

> Do not change settings.py file, use a local_settings.py or export ```QUOKKA_SHORTENED_ENABLED="@bool true"``` to your env

## FAQ

### Why another CMS?

There is a large number of great CMS's in Python ecosystem (Plone, Opps, Mezannine, DjangoCMS etc), each one has its own patterns for extension development and theme management. A CMS can take a its role as "Product" or as "Platform" and for Quokka the idea is to play in both scenarios, The CMS should be easy to deploy, extensions and themes should be "drop-in", it should be easy to develop extensions and also it should use a "schema-free" database. Until Quokka there was no CMS filling all these needs.

### Why Flask?

Because Flask is Pythonic! In my research + experience it is the best framework to develop applications which rely on "pluggable features" thanks to its Blueprints and Extension patterns, also Flask plays well with any DB/ORM of choice. (see next question)

### Why MongoDB?

Because database scheme migrations are no-happy for CMS and a Quokka CMS must be always happy to work with, so no-schema-migrations is needed with MongoDB! and Mongo is the easiest, flexible and most suitable NoSQL for CMS, also there is excellent extensions for Flask (MongoEngine and Flask-Admin) which supports MongoDB!

### Why the project is named "Quokka?"

Because it is the happiest animal in the world!

#### 20 FACTS ABOUT QUOKKAS

- 1. Happiest animal in the world because they are known for how much they smile.
- 2. They are marsupials
- 3. They live on rottnest island named after quokkas because a Dutch guy thought they were large rats. Rottnest means "rats nest"
- 4. They can climb trees
- 5. Herbivores-they eat leaves,stems,grass,etc;
- 6. They are nocturnal
- 7. They can live for long periods of time, living off of the fat stored in their tails lol
- 8. Females usually give birth once a year
- 9. Quokkas are old enough to have babies at 1.5 years old!!
- 10. Live 5-10 years
- 11. Declining population—logging, pollution, killed by foxes,pet dogs, pet cats, humans,etc;😭😭
- 12. They live in tall grass near water
- 13. Btw if you meet a quokka don't feed it anything due to declining population because it could affect them
- 14. Quokkas highest speed is 20mph
- 15. They don't chew food.they just swallow it
- 16. Closely related to the Rock Wallaby (in the picture^^^)
- 17. Scientific name is Setonix Brachyurus
- 18. Joey stays with mom for 35 weeks
- 19. Quokkas recycle a small amount of their bodies waste products
- 20. They create their own trails and paths to get food and runaway from predators.

## License
This project is licensed under the [MIT license](http://opensource.org/licenses/MIT), see `LICENSE` for more details.

This project adheres to the [Open Code of Conduct][code-of-conduct]. By participating, you are expected to honor this code.
[code-of-conduct]: http://todogroup.org/opencodeofconduct/#QuokkaProject/rochacbruno@gmail.com
