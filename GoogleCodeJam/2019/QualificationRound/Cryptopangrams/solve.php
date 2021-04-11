<?php
$problem_count = trim(fgets(STDIN));

for ($a = 0; $a < $problem_count; $a++) {
    $result = solve();

    echo 'Case #' . ($a + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve() {
  list($n, $l) = preg_split('/ /', trim(fgets(STDIN)));
  $arr = preg_split('/ /', trim(fgets(STDIN)));

  $prime_list = [];
  $prime_list2 = [];


  list($prime1, $prime2) = prime($arr[0]);
  
  if ($arr[$i+1] % $prime1 == 0) {
    $prime = $prime2;
    $next_prime = $prime1;
  } else {
    $prime = $prime1;
    $next_prime = $prime2;
  }

  $prime_list[] = $prime;
  $prime_list2[(int) $prime] = 0;
  
  for ($i = 1; $i < count($arr); $i++) { 
    $prime_list[] = $next_prime;
    $prime_list2[(int) $next_prime] = 0;
  
    $next_prime = $arr[$i] / $next_prime;
  }
  $prime_list[] = $next_prime;
  $prime_list2[(int) $next_prime] = 0;
  ksort($prime_list2);

  $i = 0;
  foreach($prime_list2 as $key => $value) {
    $prime_list2[$key] = chr(65 + $i);
    $i++;  
  }

  $result = [];
  for ($i=0; $i < count($prime_list); $i++) {
    $result[] = $prime_list2[$prime_list[$i]];
  }
 
  return implode('', $result);
}

function prime($n) {
  for ($i = 3; $i < $n; $i += 2) { 
    if ($n % $i == 0) {
      $m = $n / $i;
      return [$i, $m];
    }
  }
}