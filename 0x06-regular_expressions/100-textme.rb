#!/usr/bin/env ruby
# Your script should output: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/(?<=from:)[+?\d\w]+|(?<=to:)[+?\d]+|(?<=flags:)[-?[0-1]:]+/).join","