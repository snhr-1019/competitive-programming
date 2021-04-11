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
  list($D, $P) = preg_split("/ /u", $n, -1, PREG_SPLIT_NO_EMPTY);

  $arr = preg_split("//u", $P, -1, PREG_SPLIT_NO_EMPTY);

  $numOfShot = 0;
  $currentDamage = 1;
  $damageArr = [];
  for ($i=0; $i < count($arr); $i++) {
    if ($arr[$i] == "S") {
      $numOfShot++;
      $damageArr[] = $currentDamage;
    } else {
      $currentDamage *= 2;
    }
  }
  if ($numOfShot > $D) {
   return "IMPOSSIBLE";
  }
  $swapCount = 0;
  while (true) {
    if (array_sum($damageArr) <= $D) {
      return $swapCount;
    }
    $damageArr[array_search(max($damageArr),$damageArr)] /= 2;
    $swapCount++;
  }
}
