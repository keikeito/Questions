def LongestWord(sen)
  splitWords = sen.split(" ")
  logestWord = ""
  splitWords.each do |str|
    if str.match(/[a-zA-Z\s]+/) 
      extractWord = str.match(/[a-zA-Z\s]+/)[0]

      if extractWord.length > logestWord.length
        logestWord = extractWord
      end
    end
  end
  puts logestWord
end

LongestWord('fun&!! time')
LongestWord('I love dogs')