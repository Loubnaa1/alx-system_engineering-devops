# Login with holberton without problem

exec { 'set holberton nofile soft':
  command => '/bin/echo "soft nofile 50000" >> /etc/security/limits.conf',
  unless  => '/bin/grep -q "^soft nofile 50000$" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}

exec { 'set holberton nofile hard':
  command => '/bin/echo "hard nofile 60000" >> /etc/security/limits.conf',
  unless  => '/bin/grep -q "^hard nofile 60000$" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}
