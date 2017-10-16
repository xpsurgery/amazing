#! env ruby

require './amazing'

rows = 10
cols = 10

rows = ENV['ROWS'].to_i if ENV['ROWS']
cols = ENV['COLS'].to_i if ENV['COLS']

Amazing.doit(cols, rows)
puts $result

