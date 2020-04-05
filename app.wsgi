<VirtualHost *:80>
     # Add machine's IP address (use ifconfig command)
     ServerName 172.26.8.108
     # Give an alias to to start your website url with

     WSGIDaemonProcess expensesTracker python-path=/var/www/html/expensesTracker:/var/www/html/expensesTracker/flask_env/lib/python3.8/site-packages
     WSGIProcessGroup expensesTracker


     WSGIScriptAlias /expensesTracker /var/www/html/expensesTracker/app.wsgi
     <Directory /var/www/html/expensesTracker/expensesTracker/>
     		# set permissions as per apache2.conf file
            Options FollowSymLinks
            AllowOverride None
            Require all granted
     </Directory>
     ErrorLog ${APACHE_LOG_DIR}/error.log
     LogLevel warn
     CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>