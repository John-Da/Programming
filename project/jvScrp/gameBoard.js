import {countries} from './data';


let gameBoard = '';

game.forEach((item) => {
    random_index = Math.floor(Math.random() * countries.id);
    selected_img = countries[random_index];

    const itemId = item.id;
    let matchingImage;

    itemId.forEach((image) => {
        if (image.id === itemId){
            matchingImage = image;
        }
    });

    gameBoard += 
    `
        <div class="content-left">
            <div class="image">
                <img src="${item.image}" id="image">
            </div>
        </div>

        <div class="content-right">
            <div class="question">
                <h2>What country is this?</h2>
            </div>
            <div class="btn">
                <button class="ans_btn" id="ans_1" data-image-id="${item.id}">${item.name}</button>
                <button class="ans_btn" id="ans_2" data-image-id="${item.id}">${item.name}</button>
                <button class="ans_btn" id="ans_3" data-image-id="${item.id}">${item.name}</button>
                <button class="ans_btn" id="ans_4" data-image-id="${item.id}">${item.name}</button>
            </div>
        </div>

    `
})


document.querySelector('.gameContent').innerHTML = gameBoard;


















// function get_random_image(){
    
    // document.getElementById('image').src = `./images/c${selected_img}`;
// }

