#!/usr/bin/env ruby
# Using the provided cases
# This is a ruby script that accepts one argument
# and pass it to a regular expression matching method

puts ARGV[0].scan(/hbt{2,5}n/).join
