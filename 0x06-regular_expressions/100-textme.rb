#!/usr/bin/env ruby
# This script takes a string as an argument and returns all
#       occurrences of a sequence that matches the pattern:
#       [from:<phone_number>] [to:<phone_number>] [flags:<digit>:<digit>:<digit>:<digit>:<digit>]
puts ARGV[0].scan(/\[from:(\+?\w+)\] \[to:(\+?\w+)\] \[flags:(-?\d:-?\d:-?\d:-?\d:-?\d)\]/).join(",")
