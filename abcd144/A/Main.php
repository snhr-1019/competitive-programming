<?php

$n = (int)(fgets(STDIN));

for ($i = 1; $i <= 9; $i++) { 
    if ($n % $i != 0) continue;
    if ($n / $i > 9) continue;
    print "Yes";
    return;
}
print "No";
