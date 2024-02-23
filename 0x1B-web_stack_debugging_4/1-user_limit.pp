# login with holberton user without any error message


exec { 'change_nofile_limit':
  command => "sed -i '/^holberton soft nofile/s/.*/nofile 5000/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q '^nofile 5000$' /etc/security/limits.conf",
}
