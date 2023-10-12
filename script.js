document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("script-form");
    const outputText = document.getElementById("output-text");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const inputData = document.getElementById("input-data").value;

        // Make an HTTP request to your serverless function
        const response = await fetch('/your-serverless-function-endpoint', {
            method: 'POST',
            body: JSON.stringify({ data: inputData }),
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (response.ok) {
            const result = await response.json();
            outputText.textContent = JSON.stringify(result, null, 2);
        } else {
            outputText.textContent = 'Error: Failed to run the script.';
        }
    });
});
