FROM php:7.2-apache

EXPOSE 80
#EXPOSE 8000
#ENV PORT 8000
## Ghetto Soln to change off port 80
#CMD sed -i "s/80/$PORT/g" /etc/apache2/sites-available/000-default.conf /etc/apache2/ports.conf && docker-php-entrypoint apache2-foreground


COPY src/ /var/www/html/
COPY flag.txt /flag

RUN chown -R www-data:www-data /var/www/html
