

const containEl = document.querySelector(".container");
const careers = ['YouTube', 'Web Developer', 'Freelancer', 'Instrutor'];

let careersIndex = 0;
let characterInder = 0;
updateText();




function updateText(){
    characterInder++;
    containEl.innerHTML = `<h1>I am ${careers[careersIndex].slice(0,1) === 'I'?'an':'a'} ${careers[careersIndex].slice(0,characterInder)}</h1>`;
    if(characterInder === careers[careersIndex].length){
        careersIndex++;
        characterInder = 0;
    }

    if(careersIndex === careers.length){
        careersIndex = 0;
    }
    setTimeout(updateText, 400);
}






