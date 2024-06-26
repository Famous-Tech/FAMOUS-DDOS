function startAttack() {
    const domain = document.getElementById('domain').value;
    const rps = document.getElementById('rps').value;
    const language = document.getElementById('language').value;

    fetch('/start-attack', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ domain, rps, language })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
