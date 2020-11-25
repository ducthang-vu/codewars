/* 
Split Strings

https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/javascript

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') // should return ['ab', 'c_']
solution('abcdef') // should return ['ab', 'cd', 'ef']
*/

function solution(str){
    if (str) {
        let parts = str.match(/([A-Za-z]{2}|[A-Za-z])/g)
        if  (parts[parts.length -1].length == 1) parts[parts.length -1] += '_'
        return parts
    } else return []
}


/*SOLUTION
function solution(s){
    return (s+"_").match(/.{2}/g)||[]
}
*/