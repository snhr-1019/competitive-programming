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
  list($D, $N) = preg_split("/ /u", $n, -1, PREG_SPLIT_NO_EMPTY);
  for ($i=0; $i < $N; $i++) {
    list($K[$i], $S[$i]) = preg_split("/ /u", fgets(STDIN), -1, PREG_SPLIT_NO_EMPTY);
    $time[$i] = ($D-$K[$i])/$S[$i];
  }
  return $D / max($time);
}
