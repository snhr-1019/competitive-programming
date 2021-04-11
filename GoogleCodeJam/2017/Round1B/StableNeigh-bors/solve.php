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
  list($N, $R, $O, $Y, $G, $B, $V) = preg_split("/ /u", $n, -1, PREG_SPLIT_NO_EMPTY);

  if (max($R, $Y, $B) > array_sum([$R, $Y, $B]) - max($R, $Y, $B)) return 'IMPOSSIBLE';

  $colors = ['R', 'Y', 'B'];
  $nums = [$R, $Y, $B];
  array_multisort($nums, SORT_NUMERIC, SORT_DESC, $colors);

  $result = '';
  $diff = $nums[1] + $nums [2] - $nums[0];
  for($i=0; $i<$N; $i++) {
    $result .= $colors[0];
    $nums[0]--;

    if ($nums[1] > 0) {
      $result .= $colors[1];
      $nums[1]--;
      $i++;

      if ($diff > 0) {
        $result .= $colors[2];
        $diff--;
        $i++;
      }
    } else {
      $result .= $colors[2];
      $nums[2]--;
      $i++;
    }
  }

  return $result;
}
