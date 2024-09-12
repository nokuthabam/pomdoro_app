let timerDisplay = document.getElementById('time');
let musicPlayer = document.getElementById('music-player');
let startButton = document.getElementById('start-button');
let resetButton = document.getElementById('reset-button');

let timer;
let seconds = 25 * 60; // 25 minutes in seconds

function updateDisplay() {
    let minutes = Math.floor(seconds / 60);
    let secs = seconds % 60;
    timerDisplay.textContent = `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
}

function startTimer() {
    timer = setInterval(() => {
        if (seconds <= 0) {
            clearInterval(timer);
            musicPlayer.play();
        } else {
            seconds--;
            updateDisplay();
        }
    }, 1000);
}

function resetTimer() {
    clearInterval(timer);
    seconds = 25 * 60;
    updateDisplay();
}

startButton.addEventListener('click', startTimer);
resetButton.addEventListener('click', resetTimer);

updateDisplay(); // Initial display update
