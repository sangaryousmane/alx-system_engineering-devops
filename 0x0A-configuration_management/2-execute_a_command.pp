# use puppet to kill a process

exec { 'kill me now':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'],
}
