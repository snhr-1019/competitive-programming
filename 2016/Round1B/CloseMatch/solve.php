<?php
const SAME = 0;
const C_IS_BIGGER = 1;
const J_IS_BIGGER = 2;

$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
    $result = solve(trim(fgets(STDIN)));

    echo 'Case #' . ($i + 1) . ': ';
    echo $result;
    echo "\n";
}


function solve($n) {


    list($c, $j) = explode(" ", $n);

    $cChar = preg_split("//u", $c, -1, PREG_SPLIT_NO_EMPTY);
    $jChar = preg_split("//u", $j, -1, PREG_SPLIT_NO_EMPTY);

    $state = SAME;

    $cScore = "";
    $jScore = "";
    for ($i = 0; $i < count($cChar); $i++) {
        if ($cChar[$i] == "?" && $jChar[$i] == "?") {

            if ($state == SAME) {
                $cScore .= "0";
                $jScore .= "0";
            } else if ($state == C_IS_BIGGER) {
                $cScore .= "0";
                $jScore .= "9";
            } else if ($state == J_IS_BIGGER) {
                $cScore .= "9";
                $jScore .= "0";
            }
        } else if ($cChar[$i] != "?" && $jChar[$i] != "?") {
            $cScore .= $cChar[$i];
            $jScore .= $jChar[$i];

            if ($cChar[$i] > $jChar[$i]) {
                $state = C_IS_BIGGER;
            } else if ($cChar[$i] < $jChar[$i]) {
                $state = J_IS_BIGGER;
            }
        } else if ($cChar[$i] == "?") {
            $jScore = $jScore . $jChar[$i];
            if ($state == SAME) {
                $cScore .= $jChar[$i];
            } else if ($state == C_IS_BIGGER) {
                $cScore .= "0";
            } else if ($state == J_IS_BIGGER) {
                $cScore .= "9";
            }
        } else if ($jChar[$i] == "?") {
            $cScore = $cScore . $cChar[$i];
            if ($state == SAME) {
                $jScore .= $cChar[$i];
            } else if ($state == C_IS_BIGGER) {
                $jScore .= "0";
            } else if ($state == J_IS_BIGGER) {
                $jScore .= "9";
            }
        }
    }

    return $cScore . " " . $jScore;
}
