const colors = ['#800000', '#B8860B', '#000080', '#800080', '#FF4500'];

function getRandomColor() {
    const randomIndex = Math.floor(Math.random() * colors.length);
    return colors[randomIndex];
}

function fetchRandomNumber() {
    fetch('/number/')
        .then(response => response.json())
        .then(data => {
            const numberElement = document.getElementById('random-number');
            numberElement.textContent = data.number;
            numberElement.style.color = getRandomColor();

        })
        .catch(error => console.error('Error fetching number:', error));
}

document.addEventListener('DOMContentLoaded', () => {
    fetchRandomNumber();
    setInterval(fetchRandomNumber, 5000);
});
