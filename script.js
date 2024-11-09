document.getElementById('command-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const commandInput = document.getElementById('command-input').value.trim();
    
    if (!commandInput) {
        alert("Please enter a valid command.");
        return;
    }

    // Disable input and button while processing
    document.getElementById('command-input').disabled = true;
    document.querySelector('button').disabled = true;
    document.getElementById('result').textContent = "Processing...";

    try {
        const response = await fetch('http://127.0.0.1:5000/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: commandInput }),
        });

        const data = await response.json();

        if (data.error) {
            document.getElementById('result').textContent = `Error: ${data.error}`;
        } else {
            document.getElementById('result').textContent = data.result;
        }
    } catch (error) {
        document.getElementById('result').textContent = "Error: Unable to connect to the server.";
    } finally {
        // Re-enable input and button after processing
        document.getElementById('command-input').disabled = false;
        document.querySelector('button').disabled = false;
    }
});
