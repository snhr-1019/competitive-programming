<?php
$problem_count = trim(fgets(STDIN));

for ($a = 0; $a < $problem_count; $a++) {
    echo 'Case #' . ($a + 1) . ': ';
    solve();
    echo "\n";
}

function solve() {
  $n = trim(fgets(STDIN));
  $c_start = $c_end = $j_start = $j_end = 0;
  $answer = "";
  $schedule;
  for ($i=0; $i < $n; $i++) {
    $schedule[] = preg_split('/ /', trim(fgets(STDIN)));
    $schedule[$i][2] = $i;
  }

  foreach($schedule as $key => $row) {
    $start[$key] = (int)$row[0];
  }
  array_multisort($start,SORT_ASC,$schedule);

  for ($i=0; $i < count($schedule); $i++) { 
    if ($c_end <= $schedule[$i][0]) {
      $schedule[$i][3] = "C";
      $c_end = $schedule[$i][1];
    } else if ($j_end <=$schedule[$i][0]) {
      $schedule[$i][3] = "J";
      $j_end = $schedule[$i][1];
    } else {
      echo "IMPOSSIBLE";
      return;
    }
  }

  foreach($schedule as $key => $row) {
    $index[$key] = (int)$row[2];
  }
  array_multisort($index,SORT_ASC,$schedule);

  for ($i=0; $i < count($schedule); $i++) { 
    echo $schedule[$i][3];
  }
  return;
}