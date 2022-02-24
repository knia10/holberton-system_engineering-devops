exec {'fix_our_stack_so_that_we_get_to_0':
  command => "sed -i 's/worker_processes 4/worker_processes auto/g' /etc/nginx/nginx.conf",
  path    => ['/bin', '/usr/bin', '/usr/sbin']

exec {'nginx_rstart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
