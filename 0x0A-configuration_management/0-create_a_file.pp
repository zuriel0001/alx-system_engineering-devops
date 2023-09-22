# create a file with the following details

file { 'school':
	content => 'I love Puppet',
	group => 'www-data',
	mode => '0744',
	owner => 'www-data',
	path => '/tmp/school',
}
