<?php
$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
    $result = solve(trim(fgets(STDIN)));

    echo 'Case #' . ($i + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve($n) {
  $count = 0;
  list($pancake, $k) = preg_split("/ /u", $n, -1, PREG_SPLIT_NO_EMPTY);

  $arr = preg_split("//u", $pancake, -1, PREG_SPLIT_NO_EMPTY);

  for ($i=0; $i < count($arr)-$k+1; $i++) {
     if ($arr[$i] == "-") {

       for ($j=$i; $j < $i+$k; $j++) {
         $arr[$j] = reverse($arr[$j]);
       }
       $count++;
     }
  }

  for ($i=0; $i < count($arr); $i++) {
     if ($arr[$i] == "-") {
       return "IMPOSSIBLE";
     }
  }

  return $count;
}

function reverse($str) {
  return $str == "+" ? "-" : "+";
}
