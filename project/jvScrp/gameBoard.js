var images = [
    {src: 'https://via.placeholder.com/200?text=Image1', name: 'Image 1'},
    {src: 'https://via.placeholder.com/200?text=Image2', name: 'Image 2'},
    {src: 'https://via.placeholder.com/200?text=Image3', name: 'Image 3'},
    {src: 'https://via.placeholder.com/200?text=Image4', name: 'Image 4'}
];

var score = 0;

// Function to shuffle an array
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

// Function to display a new random image and buttons
function displayNewImage() {
    // Select a random image
    var randomImage = images[Math.floor(Math.random() * images.length)];

    // Display the image
    var imageContainer = document.getElementById('imageContainer');
    imageContainer.innerHTML = ''; // Clear previous image
    var imgElement = document.createElement('img');
    imgElement.src = randomImage.src;
    imageContainer.appendChild(imgElement);

    // Shuffle and create buttons
    var buttonContainer = document.getElementById('buttonContainer');
    buttonContainer.innerHTML = ''; // Clear previous buttons
    var buttonNames = images.map(img => img.name);
    buttonNames = shuffle(buttonNames);
    for (var i = 0; i < buttonNames.length; i++) {
        var button = document.createElement('button');
        button.innerHTML = buttonNames[i];
        button.addEventListener('click', function() {
            if (this.innerHTML === randomImage.name) {
                score++;
            } else {
                score = score;
            }
            document.getElementById('score').innerText = 'Score: ' + score;
            displayNewImage(); // Display a new image and buttons after clicking
        });
        buttonContainer.appendChild(button);
    }
}

// Initial call to display the first image and buttons
displayNewImage();


