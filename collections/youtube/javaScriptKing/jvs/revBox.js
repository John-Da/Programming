// import { testimonials } from "./data/review";

const testimonials = [
    {
        name: "Judy V",
        photoUrl: "https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dXNlcnxlbnwwfHwwfHx8MA%3D%3D",
        text: "I have been using apple software for years now and I can confidently say that it has been a game changer for me. It has all the features I need and more, making my work and personal tasks much more efficient and organized. Thank you, Apple!"
    },{
        name: "Dame W",
        photoUrl: "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8dXNlcnxlbnwwfHwwfHx8MA%3D%3D",
        text: "I can confidently say that it has been a game changer for me. Thank you, Apple!"
    },{
        name: "Anne W",
        photoUrl: "https://images.unsplash.com/photo-1499887142886-791eca5918cd?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjJ8fHVzZXJ8ZW58MHx8MHx8fDA%3D",
        text: "Thank you, Apple!"
    }
];

const imgEl = document.querySelector('img');
const textEl = document.querySelector('.usertext');
const usernameEl = document.querySelector('.username');

let idx = 0;
updateTesti();


function updateTesti(){
    const {name, photoUrl, text} = testimonials[idx];
    imgEl.src = photoUrl;
    textEl.innerText = text;
    usernameEl.innerText = name;
    idx++;
    if(idx === testimonials.length){
        idx = 0;
    }
    setTimeout(() => {
        updateTesti();
    }, 3500);
}