var fname = prompt("First Name: ")
var lname = prompt("Last Name: ")
var age = prompt("Age: ")
var height = prompt("Height (cm): ")
var pet = prompt("Pet: ")

let conditionCheck = false

if (fname[0] === lname[0] && (age > 20 && age < 30) && (height >= 170) && (pet[pet.length -1].toLowerCase() === 'y')){
    console.log('Alert: message!')
}
else{
    console.log('Not found yet!')
}