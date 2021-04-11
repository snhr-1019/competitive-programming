<?php
$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
  $a = trim(fgets(STDIN));
  $result = solve($a);
}

function solve($a) {
  $initialMatrix = [
    -1 => [-1 => false, 0 => false, 1 => false],
    0 => [-1 => false, 0 => false, 1 => false],
    1 => [-1 => false, 0 => false, 1 => false],
  ];

  $matrix = $initialMatrix;
  $centerX = 10;
  $centerY = 10;

  while(true) {
    printf("%d %d\n", $centerX, $centerY);
    list($retX, $retY) = fscanf(STDIN, "%s %s");
    if ($retX == 0 && $retY == 0) {
      return 0;
    }
    if ($retX == -1 && $retY == -1) {
      return -1;
    }

    $matrix[$retX - $centerX][$retY - $centerY] = true;

    if (isAllTrue($matrix)) {
      $centerY += 3;
      $matrix = $initialMatrix;
    }
  }
  return;
}

function isAllTrue($matrix) {
  for ($i = -1; $i <= 1 ; $i++) {
    for ($j = -1; $j <= 1; $j++) {
      if ($matrix[$i][$j] == false) {
        return false;
      }
    }
  }
  return true;
}
