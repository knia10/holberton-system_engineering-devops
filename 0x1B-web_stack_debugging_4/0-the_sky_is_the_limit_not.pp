exec {'fix_our_stack_so_that_we_get_to_0':
  command => "sed -i 's/worker_processes 4/worker_processes auto/g' /etc/nginx/nginx.conf",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

exec {'fix_unlimit':
  command => "sed -i 's/15/65536/g' /etc/default/nginx",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

exec {'nginx_restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
