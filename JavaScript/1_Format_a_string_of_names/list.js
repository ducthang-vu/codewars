/*

https://www.codewars.com/kata/53368a47e38700bd8300030d/train/javascript


Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
*/


function list(names){
    if (names.length == 0) {return ''}
    text = names[0].name
    if (names.length == 1) {return text}
    for (let i = 1; i < names.length - 1; i++) {
      text += ', ' + names[i].name
    }
    return text + ' & ' + names[names.length - 1].name 
  }


/* SOLUTION

function list(names) {
  var xs = names.map(p => p.name)
  var x = xs.pop()
  return xs.length ? xs.join(", ") + " & " + x : x || ""
}

*/


// QUICK TEST
const quickTest = [
  [list([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]), 'Bart, Lisa & Maggie'],
  [list([ {'name': 'Bart'}, {'name': 'Lisa'} ]), 'Bart & Lisa'],
  [list([ {'name': 'Bart'} ]), 'Bart'],
  [list([  ]), ''],
]

console.table(quickTest)