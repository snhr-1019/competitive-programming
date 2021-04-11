<?php
$problem_count = trim(fgets(STDIN));

for ($a = 0; $a < $problem_count; $a++) {
    list($sum, $r, $c) = solve();

    echo 'Case #' . ($a + 1) . ': ';
    echo $sum . " " . $r . " " . $c;
    echo "\n";
}

function solve() {
  $n = trim(fgets(STDIN));

  $matrix = [];
  for ($i=0; $i < $n; $i++) { 
    $matrix[] =  preg_split('/ /', trim(fgets(STDIN)));
  }

  $sum = 0;
  for ($i=0; $i < $n; $i++) { 
    $sum += $matrix[$i][$i];
  }

  //横
  $r = 0;
  for ($i=0; $i < $n; $i++) {
    $a = [];
    for ($j=0; $j < $n; $j++) {
      if (isset($a[$matrix[$i][$j]])) {
        $r++;
        break;
      }
      $a[$matrix[$i][$j]] = 1; 
    }
  }

  //縦
  $c = 0;
  for ($i=0; $i < $n; $i++) {
    $a = [];
    for ($j=0; $j < $n; $j++) {
      if (isset($a[$matrix[$j][$i]])) {
        $c++;
        break;
      }
      $a[$matrix[$j][$i]] = 1; 
    }
  }


  return array($sum, $r, $c);

}