<?php

$str = trim(fgets(STDIN));
$substr1 = substr($str, 0, (strlen($str)-1)/2);
$substr2 = substr($str, (strlen($str)+3)/2-1, (strlen($str)-1)/2);
print (isKaibun($str) && isKaibun($substr1) && isKaibun($substr2)) ? "Yes" : "No";

function isKaibun($str) {
    $char = preg_split('//', $str, -1, PREG_SPLIT_NO_EMPTY);
    $count = count($char);
    for ($i=0; $i < floor($count / 2) ; $i++) { 
        if ($char[$i] != $char[$count-1-$i]) return false;
    }
    return true;
}