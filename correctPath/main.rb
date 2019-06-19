def CorrectPath(str)
  taken = []
  isOK = true
while isOK
  path = str.dup

  (0..path.length-1).each do |i|
      if path[i] == "?"
          path[i] = ["u","d","r","l"].sample
      end
  end

  if !taken.include?(path)
      if pathcheck(path)
        isOK = false
        return path
      else
        taken << path
      end  
  end
end
end

def pathcheck(str)
  pointerGrid = [1,1]
  hisotry = [[1,1]]
  goal = [5,5]
  str.each_char do |char|
    if char == "r"
      
      move = [pointerGrid[0] += 1, pointerGrid[1]]
    elsif char == "l"
         
      move = [pointerGrid[0] -= 1, pointerGrid[1]]  
    elsif char == "u"
      
      move = [pointerGrid[0],pointerGrid[1] -= 1]     
    elsif char == "d"
      
      move = [pointerGrid[0],pointerGrid[1] += 1]   
    end

    if isOutGrid(pointerGrid)
      return false
    end
    if !hisotry.include?(move)
      hisotry << move
    else
      return false
    end  

  end
  
  if pointerGrid == [5,5]
    return true
  else
    return false
  end

end

def isOutGrid(pointerGrid)
  if pointerGrid[0] > 5 or pointerGrid[0] < 0 or pointerGrid[1] > 5 or pointerGrid[1] < 0
    return true
  end

end

puts CorrectPath('???rrurdr?')
puts CorrectPath('drdr??rrddd?')