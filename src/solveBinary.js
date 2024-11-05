const { readFileSync } = require("fs");

const binary = readFileSync("src/binary.txt").toString().split("\n").map(Number);

for (const bin of binary) {
    console.log("Octal: " + toOctal(bin));
    console.log("Hex: " + toHex(bin));
    console.log("Decimal: " + toDecimal(bin));
}

function toOctal(bin) {
    return parseFloat(bin, 2).toString(8);
}

function toHex(bin) {
    return parseFloat(bin, 2).toString(16);
}

function toDecimal(bin) {
    return parseFloat(bin, 2).toString(10);
}
