# login with holberton user without any error message

exec { 'set-holberton-soft-nofile':
  command => "sed -i 's/soft nofile/soft nofile 5000' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q 'soft nofile 5000$' /etc/security/limits.conf",
}

exec { 'set-holberton-hard-nofile':
  command => "sed -i 's/hard nofile/hard nofile 5000' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q 'hard nofile 5000$' /etc/security/limits.conf",
}
