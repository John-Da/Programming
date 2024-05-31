

const bodyEl = document.querySelector('body');
const containEl = document.querySelector(".text-container");
const careers = ['YouTube', 'Web Developer', 'Freelancer', 'Instrutor'];

let careersIndex = 0;
let characterInder = 0;
updateText();


bodyEl.addEventListener('mousemove', (event) => {
    const xPos = event.offsetX;
    const yPos = event.offsetY;
    const spanEl = document.createElement("span");
    
    spanEl.style.left = xPos + "px";
    spanEl.style.top = yPos + "px";

    const size = Math.random()*100;

    spanEl.style.width = size + "px";
    spanEl.style.height = size + "px";
    bodyEl.appendChild(spanEl);
    setTimeout(() => {
        spanEl.remove();
    }, 3000);
});


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
    setTimeout(updateText, 240);
}





