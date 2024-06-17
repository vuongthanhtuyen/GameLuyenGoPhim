document.addEventListener("DOMContentLoaded", function() {
  let intervalId;  // Biến lưu trữ setInterval ID

  // Tự động focus vào ô textbox khi DOM đã sẵn sàng
  document.getElementById('typeInput').focus();

  // Fetch dữ liệu từ file JSON
  fetch('/static/json/listWords.json')
    .then(response => response.json())
    .then(data => {
      const words = data.words; // Lấy danh sách từ từ dữ liệu JSON
      const gameArea = document.getElementById('game-area');

      // Tạo phần tử từ
      function createWordElement(word) {
        const wordElement = document.createElement('div');
        wordElement.textContent = word;
        wordElement.classList.add('word');
        wordElement.style.left = Math.random() * 90 + '%'; // Đặt vị trí ngẫu nhiên
        gameArea.appendChild(wordElement);

        // Thêm event listener cho sự kiện animationend
        wordElement.addEventListener('animationend', function() {
          // Dừng tạo từ mới khi một từ hoàn thành animation
          clearInterval(intervalId);
        });
      }

      // Bắt đầu trò chơi
      function startGame() {
        intervalId = setInterval(() => {
          const randomWord = words[Math.floor(Math.random() * words.length)];
          createWordElement(randomWord);
        }, 1000); // Tạo từ mới mỗi giây
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
  });
});
