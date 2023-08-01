#!/usr/bin/env ruby
# This script takes a string as an argument and returns
# all occurrences of ‘h’, ‘b’, ‘t’, or ‘n’ in the string.
puts ARGV[0].scan(/hbt+n/).join
