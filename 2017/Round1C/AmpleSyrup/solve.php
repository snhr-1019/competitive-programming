<?php
ini_set('memory_limit', '256M');

$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
    $result = solve();

    echo 'Case #' . ($i + 1) . ': ';
    echo $result;
    echo "\n";
}

$R = [];
$H = [];
$N = 0;
$K = 0;
$dp = null;

function solve() {
  global $R, $H, $N, $K, $dp;

  $R = [];
  $H = [];
  $N = 0;
  $K = 0;
  $dp = null;

  list($N, $K) = preg_split("/ /u", trim(fgets(STDIN)), -1, PREG_SPLIT_NO_EMPTY);

  for ($i=0; $i < $N; $i++) {
    list($R[], $H[]) = preg_split("/ /u", trim(fgets(STDIN)), -1, PREG_SPLIT_NO_EMPTY);
  }

  array_multisort($R, SORT_ASC, SORT_NUMERIC, $H);

  return rec(0, $K);
}

function rec($i, $k) {
  global $R, $H, $N, $K, $dp;

  if (!empty($dp[$i][$k])) return $dp[$i][$k];

  if ($k == 0) {
    $dp[$i][$k] = 0;
  } else if ($N-$i == $k) {
    // 残り全部選ばないといけないとき
    if ($k==1) {
      $dp[$i][$k] = 2*pi()*$R[$i]*$H[$i] + pi()*$R[$i]*$R[$i]+ rec($i+1, $k-1);
    } else {
      $dp[$i][$k] = 2*pi()*$R[$i]*$H[$i] + rec($i+1, $k-1);
    }
  } else {
    if ($k==1) {
      $dp[$i][$k] = max(2*pi()*$R[$i]*$H[$i] + pi()*$R[$i]*$R[$i]+ rec($i+1, $k-1), rec($i+1, $k));
    } else {
      $dp[$i][$k] = max(2*pi()*$R[$i]*$H[$i] + rec($i+1, $k-1), rec($i+1, $k));
    }
  }
  return $dp[$i][$k];
}
