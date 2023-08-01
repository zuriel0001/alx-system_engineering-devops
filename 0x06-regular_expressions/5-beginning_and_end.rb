#!/usr/bin/env ruby
# The script matches any sequence that starts with ‘h’,
#       has any single character in between, and ends with ‘n’.
puts ARGV[0].scan(/^h.n$/).join
