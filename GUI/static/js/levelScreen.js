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
          event.preventDefault();
          const textboxValue = document.getElementById('typeInput').value.trim();
          const fallingWords = document.querySelectorAll('.word');
          let found = false;

          fallingWords.forEach(wordElement => {
            if (wordElement.textContent === textboxValue) {
              found = true;
              wordElement.remove(); // Xóa phần tử từ rơi
            }
          });
          document.getElementById("typeInput").value = "";
        }
        ;
    });
  });