#!/usr/bin/env ruby
# Exactly matching a string that starts with h ends with n and can have any single character

puts ARGV[0].scan(/(?<=from:)[+?\d\w]+|(?<=to:)[+?\d]+|(?<=flags:)[-?[0-1]:]+/).join","