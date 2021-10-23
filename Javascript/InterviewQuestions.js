//Write a closure in javascript

let add = (a) => {
  return function (b) {
    console.log(a + b);
  };
};

//calll thee function
add(5)(10);

//check if strings are anagram to each other
let firstItem = "Mary";
let secondItem = "Armys";

function checkAnagram(i, j) {
  let one = i.toLowerCase();
  let two = j.toLowerCase();
  const itemOne = one.split("").sort().join("");
  const itemTwo = two.split("").sort().join("");

  return itemOne === itemTwo;
}

console.log(checkAnagram(firstItem, secondItem));

//linear search using js
//linear search

let items = [1, 2, 3, 7, 8, 9, 11];
function linearSearch(number) {
  for (i of items) {
    if (i === number) {
      console.log(i);
      break;
    }
  }
}

linearSearch(1);

//algorithmic complexity is O(n);
