#f = open("sample.in")
#f = open("A-small-practice.in")
f = open("A-large-practice.in")

num = f.gets

f.each_with_index {|line, case_num|
  max_shyness, str = line.split(" ")
  sum = 0
  ans = 0
  str.split("").each_with_index {|cnt, level|
    level = level.to_i
    cnt = cnt.to_i

    next if cnt == 0

    if level == 0
      s = 1
    else
      s = sum
    end

    if sum < level
      ans += (level - sum)
      sum += (level - sum)
    end
    sum += cnt
  }
  puts "Case #" + (case_num + 1).to_s + ": " + ans.to_s
}
f.close
