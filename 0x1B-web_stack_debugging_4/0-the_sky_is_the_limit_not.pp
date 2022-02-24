exec {'fix_unlimit':
  command => "sed -i 's/15/65536/g' /etc/default/nginx",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

exec {'nginx_rstart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
