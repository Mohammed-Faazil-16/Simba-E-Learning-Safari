// Initialize Charts
document.addEventListener('DOMContentLoaded', function () {
    const ctxProgress = document.getElementById('progressChart').getContext('2d');
    const ctxQuizResult = document.getElementById('quizResultChart').getContext('2d');
    const ctxPerformance = document.getElementById('performanceChart').getContext('2d');

    // Overall Progress Chart
    new Chart(ctxProgress, {
        type: 'line',
        data: {
            labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
            datasets: [{
                label: 'Progress Over Time',
                data: [10, 20, 30, 40],
                backgroundColor: 'rgba(255, 206, 86, 0.2)',
                borderColor: 'rgba(255, 206, 86, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Pie Chart for Quiz Results
    new Chart(ctxQuizResult, {
        type: 'pie',
        data: {
            labels: ['Correct', 'Incorrect'],
            datasets: [{
                data: [75, 25],
                backgroundColor: ['#4caf50', '#f44336'],
                borderColor: ['#ffffff', '#ffffff'],
                borderWidth: 1
            }]
        }
    });

    // Performance per Quiz Type (Bar Chart)
    new Chart(ctxPerformance, {
        type: 'bar',
        data: {
            labels: ['Addition', 'Subtraction', 'Multiplication', 'Division'],
            datasets: [{
                label: 'Scores',
                data: [85, 90, 78, 88],
                backgroundColor: 'rgba(255, 206, 86, 0.2)',
                borderColor: 'rgba(255, 206, 86, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
