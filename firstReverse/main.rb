def FirstReverse(str) 
  reverseWord = ''
  (str.length-1).downto(0).each { |i| reverseWord += str[i]}
  puts reverseWord
end

FirstReverse('coderbyte')
FirstReverse('I Love Code')