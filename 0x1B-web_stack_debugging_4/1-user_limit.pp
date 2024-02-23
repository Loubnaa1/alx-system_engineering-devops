# login with holberton user without any error message

exec { 'set-holberton-soft-nofile':
  command => "sed -i '/^holberton soft nofile/c\holberton soft nofile 5000' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q '^holberton soft nofile 5000$' /etc/security/limits.conf",
}

exec { 'set-holberton-hard-nofile':
  command => "sed -i '/^holberton hard nofile/c\holberton hard nofile 5000' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q '^holberton hard nofile 5000$' /etc/security/limits.conf",
}
