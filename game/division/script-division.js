let correctAnswer = 0;
let coinCount = 0;

function generateQuestion() {
    // Generate two random numbers for division
    let num2 = Math.floor(Math.random() * 9) + 1; // Divisor
    let num1 = Math.floor(Math.random() * 9) + 1; // Initial number

    // Calculate the dividend that is divisible by num2
    num1 = num1 * num2;

    // Calculate correct answer
    correctAnswer = num1 / num2;

    // Display the question
    document.getElementById('question').textContent = `What is ${num1} ÷ ${num2}?`;

    // Generate random answers and assign the correct one randomly
    let correctPosition = Math.floor(Math.random() * 4);
    let options = [];

    for (let i = 0; i < 4; i++) {
        if (i === correctPosition) {
            options.push(correctAnswer);
        } else {
            let wrongAnswer;
            do {
                wrongAnswer = Math.floor(Math.random() * 20) + 1;
            } while (wrongAnswer === correctAnswer || options.includes(wrongAnswer));
            options.push(wrongAnswer);
        }
    }

    // Display options
    for (let i = 0; i < 4; i++) {
        document.getElementById(`option${i+1}`).textContent = options[i];
    }

    // Clear feedback message
    document.getElementById('feedback').textContent = '';
}

function checkAnswer(selectedOption) {
    const selectedAnswer = document.getElementById(`option${selectedOption + 1}`).textContent;
    if (parseInt(selectedAnswer) === correctAnswer) {
        document.getElementById('feedback').textContent = 'Correct! You earned 5 coins!';
        coinCount += 5;
    } else {
        document.getElementById('feedback').textContent = 'Oops! Try again!';
    }
    document.getElementById('coinCount').textContent = coinCount;
}

// Initialize the game with the first question
window.onload = generateQuestion;
