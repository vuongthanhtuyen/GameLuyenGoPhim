document.addEventListener("DOMContentLoaded", function() {
    // Tự động focus vào ô textbox khi DOM đã sẵn sàng
    document.getElementById('typeInput').focus();

    fetch('/static/json/listWords.json')
      .then(response => response.json())
      .then(data => {
        const words = data.words;
        const gameArea = document.getElementById('game-area');

        function createWordElement(word) {
          const wordElement = document.createElement('div');
          wordElement.textContent = word;
          wordElement.classList.add('word');
          wordElement.style.left = Math.random() * 90 + '%';
          gameArea.appendChild(wordElement);
        }

        function startGame() {
          setInterval(() => {
            const randomWord = words[Math.floor(Math.random() * words.length)];
            createWordElement(randomWord);
          }, 1000);
        }

        startGame();
      });
      // Lấy dữ liệu từ ô textbox khi nhấn phím dấu cách
      document.getElementById('typeInput').addEventListener('keydown', function(event) {
        if (event.code === 'Space') {
          const textboxValue = document.getElementById('typeInput').value;
          document.getElementById('displayText').textContent = textboxValue;
        };
    });
  });