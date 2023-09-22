# create a file with the following details

file { 'school':
	path => '/tmp/school'
	mode => '0744',	
	owner => 'www-data',
	group => 'www-data',
	content => 'I love Puppet',
}
