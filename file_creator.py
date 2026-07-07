import os

# Create index.html
dir_path = '/home/rojo/workspaces/Nymix'
index_html_path = os.path.join(dir_path, 'index.html')
with open(index_html_path, 'w') as file:
    file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nymix MVP</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <button id="connect-wallet">Connect Wallet</button>
        <button id="test-network">Test Network</button>
    </div>
    <script src="app.js"></script>
</body>
</html>''')

# Create style.css
css_path = os.path.join(dir_path, 'style.css')
with open(css_path, 'w') as file:
    file.write('''body {
    font-family: Arial, sans-serif;
    background-color: #333;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}
.container {
    text-align: center;
}
button {
    padding: 10px 20px;
    background-color: #555;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
button:hover {
    background-color: #777;
}''')

# Create app.js
js_path = os.path.join(dir_path, 'app.js')
with open(js_path, 'w') as file:
    file.write('''document.addEventListener('DOMContentLoaded', function() {
    const loadAnimation = document.createElement('div');
    loadAnimation.innerHTML = '<p>Loading...</p>';
    loadAnimation.style.position = 'fixed';
    loadAnimation.style.top = '0';
    loadAnimation.style.left = '0';
    loadAnimation.style.width = '100%';
    loadAnimation.style.height = '100%';
    loadAnimation.style.backgroundColor = 'rgba(255, 255, 255, 0.7)';
    loadAnimation.style.display = 'flex';
    loadAnimation.style.justifyContent = 'center';
    loadAnimation.style.alignItems = 'center';
    document.body.appendChild(loadAnimation);

    setTimeout(() => {
        loadAnimation.remove();
        // Simulate network test
        alert('Network test completed!');
    }, 2000);
});''')
