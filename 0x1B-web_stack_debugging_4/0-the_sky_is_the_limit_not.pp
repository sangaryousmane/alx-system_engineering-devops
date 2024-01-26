# Increase the amount of traffics for nginx

# Configure ulimit
exec { 'fix--ulimit-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx'
  path    => '/usr/local/bin/:/bin/',
}

# Restart nginx
exec {'restart-nginx-for-changes':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/'
}
