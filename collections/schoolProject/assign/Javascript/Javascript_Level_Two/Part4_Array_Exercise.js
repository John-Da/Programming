// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

function addNew(name){
    roster.push(name);
}
addNew("Alic")

console.log(roster);


// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array


// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

function remove(name){
    const index = roster.indexOf(name);
    if (index < -1){
        roster.splice(index, 1);
    }
}

console.log(remove("Alice"))


// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.


// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.

function addNew(name) {
  roster.push(name);
}

function remove(name) {
  const index = roster.indexOf(name);
  if (index !== -1) {
    roster.splice(index, 1);
  }
}

function display() {
  console.log("Student Roster:");
  roster.forEach((student, index) => {
    console.log(`${index + 1}. ${student}`);
  });
}

function askForAction() {
  let action = prompt("Enter an action (add, remove, display, quit):").toLowerCase();
  return action;
}

function startApp() {
    let useApp = prompt("Do you want to use the web app? (yes/no)").toLowerCase();
    if (useApp !== "yes") {
        console.log("Goodbye!");
        return;
    }
    else {
        while (true) {
            let action = askForAction();

            if (action === "add") {
            let name = prompt("Enter the name of the student to add:");
            addNew(name);
            } else if (action === "remove") {
            let name = prompt("Enter the name of the student to remove:");
            remove(name);
            } else if (action === "display") {
            display();
            } else if (action === "quit") {
            console.log("Goodbye!");
            break;
            } else {
            console.log("Invalid action. Please enter add, remove, display, or quit.");
            }
        }
    }
}

// Start the application
startApp();
