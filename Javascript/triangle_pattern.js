// The pattern below is a triangle-shaped pattern using numbers
// To create the above pattern run 2 nested loops, internal loop will take care of rows
//(number of iterations and printing pattern) while the external loop will look for a column mechanism.

// Triangle One
let n = 5; // height of pattern
let string = "";
// External loop
for (let i = 1; i <= n; i++) {
    // Internal loop
    for (let j = 1; j <= i; j++) {
        string += j;
    }
    string += "\n";
}
console.log(string);

// Reverse Triangle Pattern
let n = 5; // height of pattern
let string = "";
// External loop
for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n - i + 1; j++) {
        string += j;
    }
    string += "\n";
}
console.log(string);
