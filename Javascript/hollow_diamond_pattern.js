let x = 5;
let fill = "";
//my github: whoisraa
function whoisraa() {
  for (let i = 1; i <= x; i++) {
    for (let j = x; j > i; j--) {
      fill += " ";
    }
  
    for (let k = 0; k < i * 2 - 1; k++) {
      if (k === 0 || k === 2 * i - 2) {
        fill += "*";
      }
      else {
        fill += " ";
      }
    }
    fill += "\n";
  }

  for (let i = 1; i <= x - 1; i++) {
    for (let j = 0; j < i; j++) {
      fill += " ";
    }
  
    for (let k = (x - i) * 2 - 1; k >= 1; k--) {
      if (k === 1 || k === (x - i) * 2 - 1) {
        fill += "*";
      }
      else {
        fill += " ";
      }
    }
    fill += "\n";
  }
  return fill;
}

console.log(whoisraa());
