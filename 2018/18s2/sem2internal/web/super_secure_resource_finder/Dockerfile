FROM php:7.2-apache

EXPOSE 80

# in debug mode I'm attaching the volumes to easily edit data
# but in the final build eveyrthing will be copied over 

RUN chown -R www-data:www-data /var/www/html
COPY files/000-default.conf /etc/apache2/sites-available/
RUN mkdir /var/www/html2

COPY files/index.php /var/www/html
COPY files/index2.php /var/www/html2/index.php
COPY files/flag.php /var/www/html2/flag.php
COPY files/admin.php /var/www/html2/admin.php

# hide flag in /etc/passwd
RUN echo "\n\n\n# flag{fi_file_le_4_the_win}"  >> /etc/passwd

# build process for headless chrome + selenium 
RUN echo "=== Building headless chrome ==="

# install python tools and dev packages 
RUN apt-get update \ 
	&& apt-get install -q -y --no-install-recommends python3-dev python3-pip python3-setuptools python3-wheel gcc \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# set python3 as default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
	&& update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

RUN echo "installing chrome" 

# [Reference: https://jpmelos.com/articles/how-use-chrome-selenium-inside-docker-container-running-python/]
# install chrome & chromium-driver
RUN apt-get update
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN apt-get -y install /chrome.deb || apt-get -yf install && rm -rf /var/lib/apt/lists/* 
RUN rm /chrome.deb 

RUN apt-get update && apt-get install -y zip libgconf-2-4 && rm -rf /var/lib/apt/lists/*
COPY files/chromedriver.zip /usr/local/bin/
WORKDIR /usr/local/bin
RUN unzip chromedriver.zip && rm chromedriver.zip
RUN chmod +x chromedriver

# install selenium:  https://stackoverflow.com/a/48983008 
RUN pip3 install --no-cache-dir selenium==3.8.0

# remove any things along the way
RUN apt-get autoremove && apt-get autoclean

# make sure triggerxss.py is runnable
COPY files/triggerxss.py /etc/
RUN chmod a+x /etc/triggerxss.py

#make temp folder for XSS payloads
RUN mkdir /var/www/html/payloads/
RUN chmod a+w /var/www/html/payloads/
