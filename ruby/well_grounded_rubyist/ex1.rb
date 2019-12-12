puts "Reading Celsius temperature value from data file temp.dat ..."
celsius = File.read("temp.dat").to_i
fahrenheit = (celsius * 9 / 5) + 32
fh_file = File.new("temp.out", "w")
fh_file.puts fahrenheit
puts "Fahrenheit conversion written to temp.out"
