# Fix 500 error when GET HTTP method requested to Apache webserver

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
