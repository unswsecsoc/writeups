FROM php:7.2-apache

EXPOSE 80

# in debug mode I'm attaching the volumes to easily edit data
# but in the final build eveyrthing will be copied over 
COPY files/ /var/www/html
WORKDIR /var/www/html

RUN mv recon.conf /etc/apache2/sites-enabled/ 
RUN chown -R www-data:www-data /var/www/html


