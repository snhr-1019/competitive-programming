<?php
$problem_count = trim(fgets(STDIN));

for ($i = 0; $i < $problem_count; $i++) {
    $first_num = trim(fgets(STDIN));
    $first_array = searchLine($first_num);

    $second_num = trim(fgets(STDIN));
    $second_array = searchLine($second_num);

    $result = array_intersect($first_array, $second_array);

    echo 'Case #' . ($i + 1) . ': ';

    switch (count($result)) {
        case 1:
            echo reset($result);
            break;
        case 0:
            echo 'Volunteer cheated!';
            break;
        default:
            echo 'Bad magician!';
    }

    echo "\n";
}

function searchLine($line_num) {
    for ($i = 1; $i <= 4; $i++) {
        if ($i == $line_num) {
            $line = trim(fgets(STDIN));
        } else {
            trim(fgets(STDIN));
        }
    }
    return preg_split('/ /', $line);
}