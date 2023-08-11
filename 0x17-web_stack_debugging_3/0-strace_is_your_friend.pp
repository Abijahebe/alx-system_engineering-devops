# A puppet manuscript to replace a line in a file on a server

file { '/etc/apache2/sites.available/000-default.conf':
  ensure  => present,
  content => template('apache2/000-default.conf.erb'),
  notify  => Service['apache2'],
}
