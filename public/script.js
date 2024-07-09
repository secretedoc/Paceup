async function fetchPlaylist() {
    const playlistUrl = document.getElementById('playlistUrl').value;
    const dailyGoal = document.getElementById('dailyGoal').value;
    const playlistId = playlistUrl.split('list=')[1];

    if (!playlistId) {
        alert('Please enter a valid YouTube playlist URL');
        return;
    }

    try {
        const response = await fetch(`/api/playlist?playlistId=${playlistId}&dailyGoal=${dailyGoal}`);
        const data = await response.json();

        displayResults(data);
    } catch (error) {
        console.error('Error fetching playlist:', error);
    }
}

function displayResults(data) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `
        <p>Total Playlist Duration: ${data.totalDuration.toFixed(2)} hours</p>
        <p>Daily Video Goal: ${data.dailyVideoGoal} videos/day</p>
    `;
}
