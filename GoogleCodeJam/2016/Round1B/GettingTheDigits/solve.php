<?php
$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
    $result = solve(trim(fgets(STDIN)));

    echo 'Case #' . ($i + 1) . ': ';
    echo $result;
    echo "\n";
}

function solve($n) {
    $arr = [
        "Z" => 0,
        "W" => 0,
        "U" => 0,
        "X" => 0,
        "G" => 0,
        "O" => 0,
        "N" => 0,
        "I" => 0,
        "V" => 0,
        "T" => 0,
        "M" => 0,
        "F" => 0,
        "S" => 0,
        "E" => 0,
        "H" => 0,
        "R" => 0,
    ];

    foreach (preg_split("//u", $n, -1, PREG_SPLIT_NO_EMPTY) as $char) {
        $arr[$char]++;
    }

    $result[0] = $arr["Z"];
    $arr["E"] -= $arr["Z"];
    $arr["R"] -= $arr["Z"];
    $arr["O"] -= $arr["Z"];
    $arr["Z"] -= $arr["Z"];

    $result[2] = $arr["W"];
    $arr["T"] -= $arr["W"];
    $arr["O"] -= $arr["W"];
    $arr["W"] -= $arr["W"];

    $result[4] = $arr["U"];
    $arr["F"] -= $arr["U"];
    $arr["O"] -= $arr["U"];
    $arr["R"] -= $arr["U"];
    $arr["U"] -= $arr["U"];

    $result[6] = $arr["X"];
    $arr["S"] -= $arr["X"];
    $arr["I"] -= $arr["X"];
    $arr["X"] -= $arr["X"];

    $result[8] = $arr["G"];
    $arr["E"] -= $arr["G"];
    $arr["I"] -= $arr["G"];
    $arr["H"] -= $arr["G"];
    $arr["T"] -= $arr["G"];
    $arr["G"] -= $arr["G"];




    $result[1] = $arr["O"];
    $arr["N"] -= $arr["O"];
    $arr["E"] -= $arr["O"];
    $arr["O"] -= $arr["O"];

    $result[5] = $arr["F"];
    $arr["I"] -= $arr["F"];
    $arr["V"] -= $arr["F"];
    $arr["E"] -= $arr["F"];
    $arr["F"] -= $arr["F"];

    $result[7] = $arr["V"];
    $arr["S"] -= $arr["V"];
    $arr["E"] -= $arr["V"];
    $arr["E"] -= $arr["V"];
    $arr["N"] -= $arr["V"];
    $arr["V"] -= $arr["V"];

    $result[9] = $arr["I"];
    $arr["N"] -= $arr["I"];
    $arr["N"] -= $arr["I"];
    $arr["E"] -= $arr["I"];
    $arr["I"] -= $arr["I"];

    $result[3] = $arr["T"];

    ksort($result);

    $str = "";
    foreach ($result as $num => $count) {
        for($i = 0; $i < $count; $i++) {
            $str = $str . $num;
        }
    }

    return $str;
}
