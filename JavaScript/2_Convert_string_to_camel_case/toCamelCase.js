/*
https://www.codewars.com/kata/517abf86da9663f1d2000003/train/javascript

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
toCamelCase("the-stealth-warrior") // returns "theStealthWarrior"

toCamelCase("The_Stealth_Warrior") // returns "TheStealthWar
*/


function toCamelCase(str){
    var words = str.split(/[-_]/g)
    for (let i = 1; i < words.length; i++) {
        words[i] = words[i][0].toUpperCase() + words[i].slice(1)
    }
    return words.join('')
}


/* SOLUTION
function toCamelCase(str){
      var regExp=/[-_]\w/ig;
      return str.replace(regExp,function(match){
            return match.charAt(1).toUpperCase();
       });
}
*/


// QUICK TEST//
const test = [
    [toCamelCase(''), ''],
    [toCamelCase("the_stealth_warrior"), "theStealthWarrior"],
    [toCamelCase("A-B-C"), "ABC"],
]

console.table(test)
