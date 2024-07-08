import {countries} from './data';



export function get_random_image(){
    random_index = Math.floor(Math.random() * countries.id);
    selected_img = countries[random_index];
    document.getElementById('image').src = `./images/c${selected_img}`;
}

export function get_random_nameBtn(){
    random_index = Math.floor(Math.random() * countries.id);
    selected_img = countries[random_index];
    document.getElementById('image').src = `./images/c${selected_img}`;
}


function get_countDown(){
    var a = 60;
    var b = a;

    var t = setInterval(() => {
        var s = document.getElementById('timer');
        s.style.strokeDashoffset = -(450 - a) / b;
        a = a < 10 ? '0' + a: a;
        document.getElementById('timer').innerHTML = a;
        setTimeout(() => {
            s.style.transition = '2s';
        }, 10);
        a--;
        if (a == -1){
            clearInterval(t);
        }
    }, 1000);
}