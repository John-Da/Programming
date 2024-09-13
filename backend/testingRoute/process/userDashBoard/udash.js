// Navbar Close and Open
document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const openButton = document.getElementById('openButton');
    const closeButton = document.querySelector('.closer');


    openButton.addEventListener('click', function(event) {
        event.preventDefault(); 
        sidebar.classList.add('open');
    });


    closeButton.addEventListener('click', function(event) {
        event.preventDefault(); 
        sidebar.classList.remove('open');
    });
});


// ----------- Expense Chart ----------------- //

const expenseChart = document.getElementById('expenseChart');
const expenseData = {
    labels:["Buying", "Fixing", "Others"],
    percentage:[50, 20, 30]
};
const ul = document.querySelector(".expenseDetails ul");

new Chart(expenseChart,{
    type:"doughnut",
    data:{
        labels:expenseData.labels,
        datasets:[{
            data:expenseData.percentage
        }],
    },
    options:{
        borderWidth:0,
        hoverBorderWidth:1,
        plugins:{
            legend:{
                display:false,
            }
        }
    },
});


const populateUl = () =>{
    expenseData.labels.forEach((l, i) => {
        let li = document.createElement("li");
        li.innerHTML = `${l}: <span class="percentage">${expenseData.percentage[i]}%</span>`;
        ul.appendChild(li);
    });
};

populateUl();


// ----------- Chart 1 ----------------- //

const chartOneChart = document.getElementById('chartOne');
const chartOneData = {
    labels:["Buying", "Fixing", "Others"],
    percentage:[70, 10, 20]
};
const chartOneul = document.querySelector(".chartOneDetails ul");

new Chart(chartOneChart,{
    type:"doughnut",
    data:{
        labels:chartOneData.labels,
        datasets:[{
            data:chartOneData.percentage
        }],
    },
    options:{
        borderWidth:0,
        hoverBorderWidth:1,
        plugins:{
            legend:{
                display:false,
            }
        }
    },
});

const chartOneUl = () =>{
    chartOneData.labels.forEach((l, i) => {
        let li = document.createElement("li");
        li.innerHTML = `${l}: <span class="percentage">${chartOneData.percentage[i]}%</span>`;
        chartOneul.appendChild(li);
    });
};

chartOneUl();

// ----------- Chart 2 ----------------- //

const chartTwoChart = document.getElementById('chartTwo');
const chartTwoData = {
    labels:["Buying", "Fixing", "Others"],
    percentage:[30, 60, 10]
};
const chartTwoul = document.querySelector(".chartTwoDetails ul");

new Chart(chartTwoChart,{
    type:"doughnut",
    data:{
        labels:chartTwoData.labels,
        datasets:[{
            data:chartTwoData.percentage
        }],
    },
    options:{
        borderWidth:0,
        hoverBorderWidth:1,
        plugins:{
            legend:{
                display:false,
            }
        }
    },
});

const chartTwoUl = () =>{
    chartTwoData.labels.forEach((l, i) => {
        let li = document.createElement("li");
        li.innerHTML = `${l}: <span class="percentage">${chartTwoData.percentage[i]}%</span>`;
        chartTwoul.appendChild(li);
    });
};

chartTwoUl();



// ---------- Calendar --------------

flatpickr("#calendarContainer", {
    inline: true,
    dateFormat: "Y-m-d",
    defaultDate: "today",
});
