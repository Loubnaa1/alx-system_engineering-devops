# login with holberton user without any error message

exec { 'increase_nofile_limit':
  command => "/bin/sed -i '/^holberton\s/ s/soft nofile [0-9]\+/soft nofile 4000/' /etc/security/limits.conf && /bin/sed -i '/^holberton\s/ s/hard nofile [0-9]\+/hard nofile 4000/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}
