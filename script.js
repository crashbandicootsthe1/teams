document.addEventListener("DOMContentLoaded", function () {
    const runScriptButton = document.getElementById("run-script-button");
    const outputDiv = document.getElementById("output-div");

    runScriptButton.addEventListener("click", async function () {
        try {
            const response = await fetch("/run-python-script", {
                method: "POST"
            });

            if (response.ok) {
                const result = await response.json();
                outputDiv.textContent = result.output;
            } else {
                outputDiv.textContent = "Error: Failed to run the script.";
            }
        } catch (error) {
            outputDiv.textContent = "Error: " + error.message;
        }
    });
});

