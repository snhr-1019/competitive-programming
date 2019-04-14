<?php
$problem_count = trim(fgets(STDIN));

for ($a = 0; $a < $problem_count; $a++) {
    $result = solve(trim(fgets(STDIN)));

    echo 'Case #' . ($a + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve($n) {
  $count = 0;

  $arr = str_split($n);
  $a = [];

  for ($i = 0; $i < count($arr); $i++) { 
    if ($arr[$i] === '4') {
      $a[] = 1;
    } else { 
      $a[] = 0;
    }
  }
  $a = intval(implode("", $a));
  $b = $n - $a;

  return $a . " " . $b;
}
