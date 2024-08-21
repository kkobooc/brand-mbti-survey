document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('survey-form');
    const ranges = form.querySelectorAll('input[type="range"]');

    ranges.forEach(range => {
        const span = document.getElementById(`${range.id}-value`);
        range.addEventListener('input', (event) => {
            span.textContent = event.target.value;
        });
    });

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = parseInt(value, 10); // 값을 정수로 변환합니다.
        });

        try {
            const response = await fetch('/submit-survey', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            console.log('Server response:', result);
            alert(result.message);
        } catch (error) {
            console.error('Error submitting survey:', error);
            alert('Failed to submit the survey.');
        }
    });
});
