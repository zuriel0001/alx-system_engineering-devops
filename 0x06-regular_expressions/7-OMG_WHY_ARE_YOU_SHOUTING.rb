#!/usr/bin/env ruby
# This script takes a string as an argument and returns all
#    occurrences of uppercase letters in the string. 
puts ARGV[0].scan(/[A-Z]/).join
