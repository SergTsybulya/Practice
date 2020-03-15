var roster = []

function addNew(){
  var addName = prompt('Enter the name please')
  roster.push(addName)
}

function remove(){
  var dellName = prompt('What name you wanna delete?')
  var index = roster.indexOf(dellName);
  if (index > -1) {
    roster.splice(index,1)
  }
}

function display(){
  console.log(roster);
}

var start = prompt("do you wanna start the app? yas/no")
var request = 'empty'

if (start === 'yas'){
  while (request!='Quit') {
    request = prompt('Choose your move: Add, Delete, Display or Quit')
    if (request === 'Add') {
      addNew()
    }
    else if (request === 'Delete') {
      remove()
    }
    else if (request === 'Display') {
      display()
    }
  }
}
alert("Thanks for using the Web App! Please refresh the page to start over.")
