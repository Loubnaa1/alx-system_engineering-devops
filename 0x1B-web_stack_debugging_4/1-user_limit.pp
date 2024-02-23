# login with holberton user without any error message

exec { 'set-holberton-soft-nofile':
  command => "sed -i 's/nofile/nofile 5000' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q 'nofile 5000$' /etc/security/limits.conf",
}

exec { 'set-holberton-hard-nofile':
  command => "sed -i 's/nofile/nofile 5000' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q 'nofile 5000$' /etc/security/limits.conf",
}
