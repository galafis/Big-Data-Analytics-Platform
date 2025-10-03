document.addEventListener('DOMContentLoaded', () => {
    const dataForm = document.getElementById('data-form');
    const dataInput = document.getElementById('data-input');
    const analyticsResults = document.getElementById('analytics-results');

    if (dataForm) {
        dataForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const data = dataInput.value;

            try {
                const response = await fetch('/api/process', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ data: data }),
                });
                const result = await response.json();
                analyticsResults.textContent = JSON.stringify(result, null, 2);
            } catch (error) {
                console.error('Error processing data:', error);
                analyticsResults.textContent = 'Error processing data.';
            }
        });
    }

    // Fetch and display analytics results on page load
    async function fetchAnalytics() {
        try {
            const response = await fetch('/api/analytics');
            const result = await response.json();
            // Display results in a more user-friendly format if needed
            console.log('Analytics results:', result);
        } catch (error) {
            console.error('Error fetching analytics:', error);
        }
    }

    fetchAnalytics();
});

