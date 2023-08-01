#!/usr/bin/env ruby
# The script only matches the first occurrence of
# ‘h’, ‘b’, ‘t’, or ‘n’ in the string
puts ARGV[0].scan(/hb?tn/).join
