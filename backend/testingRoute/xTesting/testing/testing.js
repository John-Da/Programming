function openNav() {
    document.getElementById("mySidenav").style.left = "0"; // Show sidenav
    document.getElementById("main").style.marginLeft = "250px"; // Shift main content
}

function closeNav() {
    document.getElementById("mySidenav").style.left = "-250px"; // Hide sidenav
    document.getElementById("main").style.marginLeft = "0"; // Reset main content
}