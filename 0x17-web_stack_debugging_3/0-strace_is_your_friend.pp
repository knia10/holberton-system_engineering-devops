# fix HTTP/1.0 500 Internal Server Error

exec {'Modified phpp in settings file':
    command  => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
    provider => shell
}
exec {'restart apache2':
    command => 'sudo /etc/init.d/apache2 restart',
    path    => ['/bin', '/usr/bin', '/usr/sbin']
}
