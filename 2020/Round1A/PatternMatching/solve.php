<?php
$problem_count = trim(fgets(STDIN));

for ($a = 0; $a < $problem_count; $a++) {
    solve($a);
}

function solve($a) {
  $n = trim(fgets(STDIN));

  $strArr = [];
  for ($i=0; $i < $n; $i++) { 
    $strArr[] =  preg_split('/\*/', trim(fgets(STDIN)))[1];
  }
  usort($strArr, function($a, $b) {return strlen($a) > strlen($b);});

  for ($i=0; $i < $n-1; $i++) {
    $res = preg_match('/' . $strArr[$i]. '$/', $strArr[$i+1]); 
    if (preg_match('/' . $strArr[$i]. '$/', $strArr[$i+1]) === 0) {
      echo 'Case #' . ($a + 1) . ': ';
      echo '*';
      echo "\n";
      return;
    }
  }
  echo 'Case #' . ($a + 1) . ': ';
  echo $strArr[$i];
  echo "\n";
}