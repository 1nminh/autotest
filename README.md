# Automatic software testing

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run this project you required:

```
Python 3. or newer

pip 9.0.1 or newer

geckodriver (0.18.0)
```
Required Packages:

* astroid (1.6.1)
* decorator (4.2.1)
* Django (2.0.2)
* docutils (0.14)
* isort (4.3.3)
* lazy-object-proxy (1.3.1)
* lxml (4.1.1)
* mccabe (0.6.1)
* numpy (1.14.0)
* pandas (0.22.0)
* pip (9.0.1)
* pkg-resources (0.0.0)
* pylint (1.8.2)
* python-dateutil (2.6.1)
* pytz (2017.3)
* robotframework (3.0.2)
* robotframework-selenium2library (3.0.0)
* robotframework-seleniumlibrary (3.0.1)
* selenium (3.9.0)
* setuptools (38.5.0)
* six (1.11.0)
* wheel (0.30.0)
* wrapt (1.10.11)

### Installing

* [Anaconda](https://www.anaconda.com/download/) - download the python 3.6 version(32bit/64bit your choice)

* After install open **Anaconda Promt** (you can serach for it in windows search after the installation)

* Use the command (Replace the "PackageName" with the name of the Required Packages above)

```
pip install "PackageName"
```

* [Anaconda](https://github.com/mozilla/geckodriver/releases/) - download the geckodriver v0.18.0 (32/64 bit of your choice)

Extract file you downloaded to C:\data\workspace\

Use windows search type **edit the system environment variables** press enter

choose **environment variables**

Choose **path** in your **user variables** click **edit** - then **new**

paste in the following line

```
C:\data\workspace\
```

Click **ok** - after that you good to go

## Running the project

* After installed all the package rediect the Anaconda Promt to the project folder and type

```
python manage.py runserver
```

## License

TIC - TMA


