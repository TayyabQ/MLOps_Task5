document.getElementById('myForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const name = formData.get('name');
    const email = formData.get('email');

    try {
        const response = await fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email })
        });
        const data = await response.json();
        document.getElementById('message').innerText = data.message;
    } catch (error) {
        console.error('Error:', error);
    }
});
