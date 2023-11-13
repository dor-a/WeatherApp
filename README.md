<!DOCTYPE html>
<html lang="en">

<body>
    <div class="container">
        <h1>Global Weather Tracker: Real-Time Weather Data App</h1>
        <div class="section">
            <h2>Introduction</h2>
            <p>Global Weather Tracker is a Python-based application designed to fetch real-time weather data from various global locations. Leveraging the Weather API, this app provides up-to-the-minute temperature updates for a selection of countries, making it an invaluable tool for travelers, researchers, and weather enthusiasts.</p>
        </div>
        <div>
            <h2>Technologies Used</h2>
            <ul>
                <li>Python</li>
                <li>Requests Library</li>
                <li>GeonamesCache</li>
                <li>dotenv for environment variable management</li>
                <li>Weather API</li>
            </ul>
        </div>
        <div>
            <h2>Features</h2>
            <ul>
                <li>Fetches real-time weather data for five randomly chosen countries.</li>
                <li>Uses the Weather API to retrieve current temperatures and other weather details.</li>
                <li>Custom logging system for tracking and debugging.</li>
                <li>Easy configuration through environment variables.</li>
                <li>Works on any os system, include docker , k8s .</li>
            </ul>
        </div>
        <div>
            <h2>Setup and Installation</h2>
            <p>To run this application on your local machine, follow these steps:</p>
            <ol>
                <li>Create a user and obtain API Key from :<code>(https://www.weatherapi.com/)</code></li>
                <li>Clone the repository: <code>git clone [repo-link]</code></li>
                <li>Install required Python packages: <code>pip install -r requirements.txt</code></li>
                <li>Set up your <code>.env</code> file with your API_KEY=<code>12345678910</code></li>
                <li>Run the application: <code>python app.py</code></li>
            </ol>
        </div>
        <div>
            <h2>Usage</h2>
            <p>Run the application using the command <code>python app.py</code>. The app will automatically update weather information every 5 minutes and log the data.</p>
        </div>
        <div>

</body>
</html>

