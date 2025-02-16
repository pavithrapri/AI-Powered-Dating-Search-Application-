document.getElementById("searchForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const lat = document.getElementById("lat").value;
    const lng = document.getElementById("lng").value;

    const response = await fetch("/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ location: { lat: parseFloat(lat), lng: parseFloat(lng) } })
    });

    const data = await response.json();
    document.getElementById("results").innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
});
