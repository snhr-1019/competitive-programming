<?php
$problem_count = trim(fgets(STDIN));

for ($a = 0; $a < $problem_count; $a++) {
    $result = solve();

    echo 'Case #' . ($a + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve() {
  $n = trim(fgets(STDIN));
  $lydia_arr = str_split(trim(fgets(STDIN)));

  $result = [];
  for ($i = 0; $i < count($lydia_arr); $i++) {
    $result[] = $lydia_arr[$i] == 'S' ? 'E' : 'S';
  }

  return implode($result);
}
