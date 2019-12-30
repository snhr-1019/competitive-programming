"use strict";
function Main(input) {
    const args = input.trim().split(' ');
    console.log('%s%s', args[1], args[0]);
}
Main(require("fs").readFileSync("/dev/stdin", "utf8"));