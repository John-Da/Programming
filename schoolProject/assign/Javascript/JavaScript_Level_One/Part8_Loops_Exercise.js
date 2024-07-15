/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop
var word = "hello";
let count = 0;
// // While Loop
while(count < 5){
    console.log("hello");
    count+=1;
}

// // For Loop
var word = "hello";
for (var i = 0; i < 5; i++){
    console.log(word)
}



/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
let j = 0;
while(j <= 25){
    if (j % 2){
        console.log(j);
    }
    j++;
}



// METHOD TWO
// For Loop

for (var a = 0; a <= 25; a++){
    if (a % 2){
        console.log(a);
    }
}