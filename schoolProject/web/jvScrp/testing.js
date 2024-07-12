// import { countries } from "./data";


const buttonContainer = document.getElementById('button-container');

function createButton(id, text){
    var button = document.createElement('button');
    button.id = id;
    button.innerHTML = text;
    button.addEventListener("click", function() {
        alert(text + " clicked"); // answer check
    });
    return button;
}

for (var i = 1; i <= 4; i++){
    var button = createButton('button', 'button name');
    buttonContainer.appendChild(button);
}



