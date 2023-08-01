#!/usr/bin/env ruby
# This script takes a string as an argument and returns all occurrences
# of ‘h’, ‘b’, ‘t’, or ‘n’ in the string.
# It matches zero or more occurrences of ‘t’ in addition to ‘h’, ‘b’, and ‘n’.
puts ARGV[0].scan(/hbt*n/).join
