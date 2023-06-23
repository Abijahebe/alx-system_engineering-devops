# executes a comand using puppet

exec { 'kill_a_process':
  command => '/usr/bin/pkill killmenow',
}
