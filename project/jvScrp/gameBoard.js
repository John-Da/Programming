import {countries} from '../jvScrp';


let gameBoard = '';

countries.forEach((country) => {
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
            <div class="btn" id="btn_ans">
                <button class="ans_btn" id="ans_1" data-image-id="${item.id}">${item.name}</button>
            </div>
        </div>
    `
}) 
