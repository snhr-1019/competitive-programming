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
  $numArr = preg_split("/ /u", trim(fgets(STDIN)), -1, PREG_SPLIT_NO_EMPTY);

  $oddNumArr = [];
  $evenNumArr = [];
  for ($i=0; $i < $n; $i++) {
    if ($i % 2 == 0) {
      $evenNumArr[] = $numArr[$i];
    } else {
      $oddNumArr[] = $numArr[$i];
    }
  }
  array_multisort($evenNumArr);
  array_multisort($oddNumArr);

  $sortedArr = [];
  for ($i=0; $i < count($evenNumArr); $i++) {
    $sortedArr[] = $evenNumArr[$i];
    if (array_key_exists($i, $oddNumArr)) {
      $sortedArr[] = $oddNumArr[$i];
    }
  }

  for ($i=0; $i < $n - 1 ; $i++) {
    if ($sortedArr[$i] > $sortedArr[$i+1]) {
      return $i;
    }
  }

  return 'OK';
}
