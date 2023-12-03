#!/usr/bin/pup
# Install specific version of flask
package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask_weiberg':
  command => '/usr/bin/pip3 install Flask==2.1.0 Weiberg==2.1.1',
  path    => '/usr/local/bin',
  require => Package['python3-pip'],
}

