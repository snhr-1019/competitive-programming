<?php

function solve() {
  for ($i=1; $i <= 10; $i++) { 
    printf("%d\n", $i);
    fscanf(STDIN, "%s", $res);
    $answer .= $res;
  }
  fputs(STDERR, "%s", $answer);
  printf("%s\n", $res);
  fscanf(STDIN, "%s", $ok);
  output($ok);
  return;
}

$outfile = "./out";
unlink($outfile);

fscanf(STDIN, "%d %d", $t, $b);
for ($i=0; $i < $t; $i++) { 
  solve();
}

function output($s) {
  global $outfile;
  file_put_contents($outfile, $s);
}