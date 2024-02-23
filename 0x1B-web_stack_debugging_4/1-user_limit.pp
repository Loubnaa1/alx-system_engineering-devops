# login with holberton user without any error message

exec { 'update_nofile_limits':
  command => "sed -i 's/nofile \\+[0-9][0-9]*/nofile 5000/g' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q 'nofile 5000' /etc/security/limits.conf",
}
