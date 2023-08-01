#!/usr/bin/env ruby
# regular expression that will match the cases in attached to question
#   number of "t" should be 2 min and 5 max
puts ARGV[0].scan(/hbt{2,5}n/).join
