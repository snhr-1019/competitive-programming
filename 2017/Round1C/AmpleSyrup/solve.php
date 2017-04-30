<?php
$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
    $result = solve();

    echo 'Case #' . ($i + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve() {
  $R = [];
  $H = [];
  list($N, $K) = preg_split("/ /u", trim(fgets(STDIN)), -1, PREG_SPLIT_NO_EMPTY);

  for ($i=0; $i < $N; $i++) {
    list($R[], $H[]) = preg_split("/ /u", trim(fgets(STDIN)), -1, PREG_SPLIT_NO_EMPTY);
  }

  array_multisort($R, SORT_ASC, SORT_NUMERIC, $H);

  return rec(0, $K, $R, $H, $N, $K);
}

function rec($i, $k, $R, $H, $N, $K) {
  if ($k == 0) {
    return 0;
  } else if ($N-$i == $k) {
    // 残り全部選ばないといけないとき
    if ($k==1) {
      return 2*pi()*$R[$i]*$H[$i] + pi()*$R[$i]*$R[$i]+ rec($i+1, $k-1, $R, $H, $N, $K);
    } else {
      return 2*pi()*$R[$i]*$H[$i] + rec($i+1, $k-1, $R, $H, $N, $K);
    }
  } else {
    if ($k==1) {
      return max(2*pi()*$R[$i]*$H[$i] + pi()*$R[$i]*$R[$i]+ rec($i+1, $k-1, $R, $H, $N, $K), rec($i+1, $k, $R, $H, $N, $K));
    } else {
      return max(2*pi()*$R[$i]*$H[$i] + rec($i+1, $k-1, $R, $H, $N, $K), rec($i+1, $k, $R, $H, $N, $K));
    }
  }
}
