let n = 5;
let string = "";

// reversed pyramid pattern
for (let i = 0; i < n; i++) {
  // printing spaces
  for (let j = 0; j < i; j++) {
    string += " ";
  }
  // printing star
  for (let k = 0; k < (n - i) * 2 - 1; k++) {
    string += "*";
  }
  string += "\n";
}
// pyramid pattern
for (let i = 2; i <= n; i++) {
  // printing spaces
  for (let j = n; j > i; j--) {
    string += " ";
  }
  // printing star
  for (let k = 0; k < i * 2 - 1; k++) {
    string += "*";
  }
  string += "\n";
}
console.log(string);
