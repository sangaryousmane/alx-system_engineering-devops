# use puppet to kill a process
exec { 'Kill me now':
  command => 'pkill -9 -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
