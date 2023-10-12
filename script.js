document.addEventListener("DOMContentLoaded", function () {
    const runScriptButton = document.getElementById("run-script-button");
    const outputDiv = document.getElementById("output-div");

    runScriptButton.addEventListener("click", async function () {
        // Make an HTTP request to the API endpoint that triggers the script execution
        const response = await fetch("/api/execute-script");

        if (response.ok) {
            const result = await response.json();
            outputDiv.textContent = JSON.stringify(result, null, 2);
        } else {
            outputDiv.textContent = "Error: Failed to run the script.";
        }
    });
});
