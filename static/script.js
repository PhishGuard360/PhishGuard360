


    document.addEventListener('DOMContentLoaded', function () {
        const form = document.getElementById('phishForm');

        form.addEventListener('submit', async function (event) {
            event.preventDefault(); 
            const urlContent = document.getElementById('urlContent').value.trim();

            // Basic validation
            if (!urlContent) {
                alert('Please enter a URL to analyze.');
                return;
            }

            try {
                const response = await fetch('/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ urlContent }),
                });

                if (response.ok) {
                    const result = await response.json();
                    
                    document.getElementById('urlPrediction').innerText = result['URL Prediction'] || "No prediction made.";
                    document.getElementById('resultSection').style.display = 'block'; // Show the results section
                    
                    alert(`Prediction: ${result['URL Prediction']}`);
                } else {
                    alert('Error: Something went wrong with the prediction!');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error: Unable to fetch predictions!');
            }
        });
    });