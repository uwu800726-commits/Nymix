let userWallet = null;

document.getElementById('connectWalletBtn').addEventListener('click', () => {
    userWallet = "0x" + Array.from({length: 40}, () => Math.floor(Math.random()*16).toString(16)).join('');
    document.getElementById('walletStatus').innerText = `Conectado: ${userWallet.substring(0,6)}...${userWallet.substring(38)}`;
    document.getElementById('testNetworkBtn').disabled = false;
});

document.getElementById('testNetworkBtn').addEventListener('click', async () => {
    const loadingDiv = document.getElementById('loading');
    const resultsDiv = document.getElementById('results');
    const testBtn = document.getElementById('testNetworkBtn');

    testBtn.disabled = true;
    loadingDiv.classList.remove('hidden');
    resultsDiv.classList.add('hidden');

    try {
        const response = await fetch('/api/submit_test', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ wallet: userWallet })
        });

        const resData = await response.json();
        loadingDiv.classList.add('hidden');
        resultsDiv.classList.remove('hidden');

        if (response.ok) {
            document.getElementById('pingResult').innerText = `Ping: ${resData.results.ping}`;
            document.getElementById('downResult').innerText = `Bajada: ${resData.results.download_speed}`;
            document.getElementById('upResult').innerText = `Subida: ${resData.results.upload_speed}`;
            document.getElementById('rewardResult').innerText = `+${resData.reward_points} Puntos Nymix ganados!`;
        } else {
            document.getElementById('pingResult').innerText = `Error: ${resData.error}`;
            document.getElementById('downResult').innerText = '';
            document.getElementById('upResult').innerText = '';
            document.getElementById('rewardResult').innerText = '';
        }
    } catch (err) {
        loadingDiv.classList.add('hidden');
        resultsDiv.classList.remove('hidden');
        document.getElementById('pingResult').innerText = "Error de conexión con el backend local.";
    }
    testBtn.disabled = false;
});
