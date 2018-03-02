# Selenium Template

A simple example of selenium test written in Python

## Requirements

### Basic requirements (for Mac):

 1. [Homebrew](http://brew.sh/)

 2. Python

	```
	$ brew install python
	```

 3. Chromedriver

	```
	$ brew install chromedriver
	```

## Setup

```
$ pip install selenium==3.8.0
```

## Test run

```
$ git clone https://github.com/joyzoursky/selenium-template.git
$ cd selenium-template
$ python test_script.py
```

## Running in docker image

```
$ git clone https://github.com/joyzoursky/selenium-template.git
$ cd selenium-template
$ docker run -it -v $(pwd):/usr/workspace joyzoursky/python-chromedriver:3.6-alpine3.7-selenium sh
/ # cd /usr/workspace
/usr/workspace # python test_script.py
```
