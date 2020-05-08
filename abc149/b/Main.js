"use strict";
function Main(input) {
    const args = input.trim().split(' ').map(Number);
    const r1 = Math.max(args[0] - args[2], 0);
    const r2 = Math.max(args[0] + args[1] - args[2] - r1, 0);
    console.log('%s %s', r1, r2);
}
Main(require("fs").readFileSync("/dev/stdin", "utf8"));