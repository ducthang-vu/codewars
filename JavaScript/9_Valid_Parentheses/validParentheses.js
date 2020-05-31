/*
Valid Parentheses

https://www.codewars.com/kata/52774a314c2333f0a7000688/train/javascript

Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100
*/


function validParentheses(parens){
    let regex = /\(\)/g
    while (parens.search(regex) != -1) parens = parens.replace(regex, '')
    return parens.length ? false : true
}


const test = [
    [validParentheses('(())'), true],
    [validParentheses(')(()))'), false],
    [validParentheses('('), false],
    [validParentheses('(())((()())())'), true]
]

console.table(test)


/* SOLUTION
function validParentheses(parens){
    var re = /\(\)/;
    while (re.test(parens)) parens = parens.replace(re, "");
    return !parens;
}
*/