// Make sure to have the crimeData variable properly defined in your HTML file as mentioned earlier.

var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: crimeData.labels, // Your X-axis labels (dates, categories, etc.)
        datasets: [{
            label: 'Crime Reports',
            backgroundColor: '#1c355a', // Background color of the line area
            borderColor: '#1c355a', // Border color of the line
            borderWidth: 1.6, // Thickness of the line
            pointBackgroundColor: '#fff', // Color of the data points
            pointBorderColor: '#1c355a', // Border color of the data points
            pointHoverBackgroundColor: '#1c355a', // Background color when hovered
            pointHoverBorderColor: '#fff', // Border color when hovered
            pointRadius: 0, // Radius of the data points
            data: crimeData.counts // Your Y-axis data (counts, values, etc.)
        }]
    },
    options: {
        animation: {
            duration: 10000 // Duration of the animation of the line draw
        },
        scales: {
            y: {
                beginAtZero: true, // Start the Y-axis from zero
                grid: {
                    display: false // Do not display grid lines for Y-axis
                }
            },
            x: {
                grid: {
                    display: false // Do not display grid lines for X-axis
                }
            }
        },
        elements: {
            line: {
                tension: 0.4 // Smoothness of the line curve
            }
        },
        responsive: true, // Make sure the chart is responsive
        maintainAspectRatio: false, // Maintain the aspect ratio
        plugins: {
            legend: {
                display: true, // Display the legend
                position: 'top', // Position of the legend
            }
        }
    }
});
