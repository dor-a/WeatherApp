<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Weather Tracker README</title>
    <style>
        body { font-family: Arial, sans-serif; }
        h1, h2 { color: navy; }
        code { background-color: #f2f2f2; padding: 2px 4px; }
        .container { width: 80%; margin: auto; }
        .section { margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Global Weather Tracker: Real-Time Weather Data App</h1>

        <div class="section">
            <h2>Introduction</h2>
            <p>Global Weather Tracker is a Python-based application designed to fetch real-time weather data from various global locations. Leveraging the Weather API, this app provides up-to-the-minute temperature updates for a selection of countries, making it an invaluable tool for travelers, researchers, and weather enthusiasts.</p>
        </div>

        <div class="section">
            <h2>Technologies Used</h2>
            <ul>
                <li>Python</li>
                <li>Requests Library</li>
                <li>GeonamesCache</li>
                <li>dotenv for environment variable management</li>
                <li>Weather API</li>
            </ul>
        </div>

        <div class="section">
            <h2>Features</h2>
            <ul>
                <li>Fetches real-time weather data for five randomly chosen countries.</li>
                <li>Uses the Weather API to retrieve current temperatures and other weather details.</li>
                <li>Custom logging system for tracking and debugging.</li>
                <li>Easy configuration through environment variables.</li>
                <li>Works on any os system, include docker , k8s .</li>
            </ul>
        </div>

        <div class="section">
            <h2>Setup and Installation</h2>
            <p>To run this application on your local machine, follow these steps:</p>
            <ol>
                <li>Clone the repository: <code>git clone [repo-link]</code></li>
                <li>Install required Python packages: <code>pip install -r requirements.txt</code></li>
                <li>Set up your <code>.env</code> file with your API_KEY, MY_POD_NAME, and MY_NODE_NAME.</li>
                <li>Run the application: <code>python app.py</code></li>
            </ol>
        </div>

        <div class="section">
            <h2>Usage</h2>
            <p>Run the application using the command <code>python app.py</code>. The app will automatically update weather information every 5 minutes and log the data.</p>
        </div>

        <div class="section">
            <h2>Contribution and Support</h2>
            <p>Contributions to the Global Weather Tracker are welcome! Please read our contributing guidelines before submitting a pull request. For support, open an issue in the repository or contact [Your Email].</p>
        </div>

        <div class="section">
            <h2>License</h2>
            <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
        </div>
    </div>

</body>
</html>
