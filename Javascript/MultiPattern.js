/*
Prints a multi pattern triangle
+-
+--
+---
+----
+-----
+------
+-------
+--------
+---------
+----------
+-----------
+------------
+-------------
+--------------
+---------------
+----------------
+-----------------
+------------------
********************
*/

let n = 20;
let string = "";

for (let i = 1; i <= n; i++) {
  // printing star
  for (let j = 0; j < i; j++) {
    if(i === n) {
      string += "*";
    }
    else {
      if (j == 0 || j == i + 1) {
        string += "+";
      }
      else {
        string += "-";
      }
    }
  }
  string += "\n";
}
console.log(string);
