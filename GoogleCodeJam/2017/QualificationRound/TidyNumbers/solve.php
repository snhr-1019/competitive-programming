<?php
$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
    $result = solve(trim(fgets(STDIN)));

    echo 'Case #' . ($i + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve($n) {
  while(true) {
    $arr = preg_split("//u", $n, -1, PREG_SPLIT_NO_EMPTY);
    for ($i = 1; $i < count($arr); $i++) {
      if ($arr[$i] == 0) {
        $arr[$i-1]--;
        for ($k=$i; $k < count($arr); $k++) {
          $arr[$k] = 9;
        }
        $n = implode($arr);
        continue 2;
      }

      if ($arr[$i-1] > $arr[$i]) {
        $arr[$i-1]--;
        for ($k=$i; $k < count($arr); $k++) {
          $arr[$k] = 9;
        }
        $n = implode($arr);
        continue 2;
      }
    }
    break;
  }
  return intval(implode($arr));
}
