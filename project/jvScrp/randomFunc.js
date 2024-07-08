import {countries} from './data';



function get_random_image(){
    random_index = Math.floor(Math.random() * countries.length);
    selected_img = countries[random_index];
    document.getElementById('image').src = `./images/c${selected_img}`;
}


