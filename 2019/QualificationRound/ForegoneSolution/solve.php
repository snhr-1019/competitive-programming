<?php
$problem_count = trim(fgets(STDIN));

for ($a = 0; $a < $problem_count; $a++) {
    $result = solve(trim(fgets(STDIN)));

    echo 'Case #' . ($a + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve($n) {
  $arr = str_split($n);
  $a = [];
  $b = [];
  for ($i = 0; $i < count($arr); $i++) { 
    if ($arr[$i] === '4') {
      $a[] = 1;
      $b[] = 3;
    } else { 
      if (count($a) > 0) {
        $a[] = 0;
      }
      if (count($b) > 0 || $arr[$i] > 0) {
        $b[] = $arr[$i];
      }
    }
  }

  return implode("", $a) . " " . implode("", $b);
}
