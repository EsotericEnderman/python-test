const { readFileSync } = require("fs");

const binary = readFileSync("src/binary.txt").toString().split("\n").map(Number);

for (const bin of binary) {
    console.log("Octal: " + toOctal(bin));
    console.log("Hex: " + toHex(bin));
}

function toOctal(bin) {
    return parseInt(bin, 2).toString(8);
}

function toHex(bin) {
    return parseInt(bin, 2).toString(16);
}
