const sideBar = document.getElementById("sideBar")
const mainPage = document.getElementById("main")
const arrowout = document.getElementById("menubar")



// function openCloseNav(){
//     let isClose = sideBar.style.left === "-250px";
//     let mainMargin = mainPage.style.marginLeft === "0";
//     let menuVb = arrowout.style.visibility === "visible";

//     sideBar.style.left = isClose ? "250px" : "0px";
//     mainPage.style.marginLeft = mainMargin ? "200px" : "0px";
//     arrowout.style.visibility = menuVb ? "visible" : "hidden";
// }


function openNav(){
    sideBar.style.left = "0";
    mainPage.style.marginLeft = "200px";
    arrowout.style.visibility = "hidden";
}

function closeNav(){
    sideBar.style.left = "-250px";
    mainPage.style.marginLeft = "0";
    arrowout.style.visibility = "visible";
}