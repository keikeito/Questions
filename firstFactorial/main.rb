def FirstFactorial(num)
  sum = 1
  num.downto(1).each do|i|
    sum *=i
  end
  puts sum
end

FirstFactorial(4)
FirstFactorial(8)