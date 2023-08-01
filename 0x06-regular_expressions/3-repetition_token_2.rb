#!/usr/bin/env ruby
# This script takes a string as an argument and returns
# all occurrences of ‘h’, ‘b’, ‘t’, or ‘n’ in the string.
#
# It matches one or more occurrences of ‘t’ using the + character
# So the script matches any sequence of ‘h’, ‘b’, ‘t’, and one or more 'n’s.
puts ARGV[0].scan(/hbt+n/).join
