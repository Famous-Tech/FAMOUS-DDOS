const translations = {
    en: {
        title: "FAMOUS DDOS",
        domainLabel: "Domain:",
        rpsLabel: "Requests Per Second:",
        startButton: "Start Attack"
    },
    fr: {
        title: "FAMOUS DDOS",
        domainLabel: "Domaine:",
        rpsLabel: "Requêtes Par Seconde:",
        startButton: "Démarrer l'attaque"
    },
    ht: {
        title: "FAMOUS DDOS",
        domainLabel: "Domèn:",
        rpsLabel: "Rekèt Pou Chak Segond:",
        startButton: "Kòmanse Atak"
    }
};

function changeLanguage() {
    const language = document.getElementById('language').value;
    document.getElementById('title').innerText = translations[language].title;
    document.getElementById('domain-label').innerText = translations[language].domainLabel;
    document.getElementById('rps-label').innerText = translations[language].rpsLabel;
    document.getElementById('start-button').innerText = translations[language].startButton;
}

function startAttack() {
    const domain = document.getElementById('domain').value;
    const rps = document.getElementById('rps').value;

    fetch('/start-attack', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ domain, rps })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
