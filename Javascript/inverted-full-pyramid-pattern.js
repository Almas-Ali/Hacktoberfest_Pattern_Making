// variables
let pyramidRows = 10; // number of row of pyramids.
let pyramid = "";

//loops
for (let i = 0; i < pyramidRows; i++) {
    
    // adding spaces
    for (let j = 0; j < i; j++) pyramid += " ";
    
    // adding star
    for (let k = 0; k < (pyramidRows - i) * 2 - 1; k++) pyramid += "*";

    // line break
    pyramid += "\n";
}

// render in dom.
console.log(`<pre>${pyramid}</pre>`);