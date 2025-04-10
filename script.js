function closeError() {
  document.getElementById('glitch-overlay').classList.add('hidden');
}

function showGlitch() {
  document.body.classList.add('glitch');
  const screen = document.getElementById('glitch-overlay');
  screen.classList.remove('hidden');

  const audio = new Audio('https://freesound.org/data/previews/316/316847_4939433-lq.mp3'); // 警報音效
  audio.play();

  setTimeout(() => {
    document.body.classList.remove('glitch');
    screen.classList.add('hidden');
  }, 5000);
}

fetch('device-list.json')
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById('device-list');
    const devices = data.devices;

    for (const key in devices) {
      const d = devices[key];
      const div = document.createElement('div');
      div.className = 'device';
      div.innerHTML = `
        <strong>${d.device}</strong> (${d.os})<br>
        IP: ${d.ip} <br>
        擁有者: ${d.owner} <br>
        上次出現: ${new Date(d.lastSeen).toLocaleString()}
      `;
      list.appendChild(div);
    }

    // 模擬幾秒後崩壞
    setTimeout(showGlitch, 6000);
  })
  .catch(err => {
    console.error('載入裝置清單失敗：', err);
    showGlitch();
  });
