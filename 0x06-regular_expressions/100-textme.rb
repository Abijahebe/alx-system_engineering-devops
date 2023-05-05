#!/usr/bin/env ruby

puts ARGV[0].scan(/(?<=from|to|flags):(\+?\W+|[-?[0-1]:?]+)/).join(',')
