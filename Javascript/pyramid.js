let n = 5
let string = ""

//External loop
for (let i = 1; i <= n; i++) {
  //printing spaces
  for (let j = n; j > i; j--) {
    string += " "
  }
  //printing star
  for (let k = 0; k < 2 * i - 1; k++) {
    string += "*";
  }
  string += "\n"
}

document.write(`<pre>${string}</pre>`)