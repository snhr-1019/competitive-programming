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

  for ($a = 1; $a < $n; $a++) { 
    $b = $n - $a;
    if (strpos($a, '4') === false && strpos($b, '4') === false) {
      return $a . " " . $b;
    }
  }
}
