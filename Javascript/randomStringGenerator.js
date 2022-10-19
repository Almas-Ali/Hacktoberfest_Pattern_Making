function randomStringPattern(input) {
    var text = "";
    var possible;
    for (var j = 0; j < input.length; j++) {
      if (input[j] == " ") {
          possible = ' ';
      } else if ((input[j] == input[j].toUpperCase()) && (input[j] != input[j].toLowerCase())) {
          possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      } else if ((input[j] == input[j].toLowerCase()) && (input[j] != input[j].toUpperCase())) {
          possible = "abcdefghijklmnopqrstuvwxyz";
      } else if ('0123456789'.indexOf(input[j]) !== -1) {
          possible = "0123456789";
      } else {
          possible = "#!@~$%^&*)-_"
      }
      text += possible.charAt(Math.floor(Math.random() * possible.length));
      }
    return text;
  }
  console.log(randomStringPattern("OktoberFest Yeah"));