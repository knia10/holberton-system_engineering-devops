exec { 'configuration_hard_nofile':
  command => "sed -i '/holberton hard nofile/s/5/65535/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

exec { 'configuration_soft_nofile':
  command => "sed -i '/holberton soft nofile/s/4/65000/g' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
