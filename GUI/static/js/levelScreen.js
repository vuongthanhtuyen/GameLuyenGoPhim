document.addEventListener("DOMContentLoaded", function () {
  let intervalId; // Biến lưu trữ setInterval ID

  // Định nghĩa lớp Target
  function Target(name, status) {
    this.name = name;
    this.status = status;
  }

  // Định nghĩa lớp Level
  function Level(id, gameStatus, listTargets, targetCount) {
    this.id = id;
    this.gameStatus = gameStatus;
    this.listTargets = listTargets;
    this.targetCount = targetCount;
  }

  // bản record turn dùng để post về
  function recordTurn(nowLevel, recordDate, totalTarget, totalTime){
    this.nowLevel =  nowLevel
    this.recordDate = recordDate 
    this.totalTarget = totalTarget
    this.totalTime = totalTime
  }

  // Khởi tạo level
  var level = new Level(1, true, [], 4);

  // Lấy dữ liệu từ Json
  const apiUrl = "/static/json/listWords.json";
  fetch(apiUrl)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok!" + response.statusText);
      }
      return response.json();
    })
    .then((data) => {
      console.log("Dữ liệu từ API:", data);
      if (!Array.isArray(data.words)) {
        throw new TypeError("Dữ liệu trả về không chứa mảng words");
      }
      // Tạo các đối tượng Target từ mảng words và gán cho level
      level.listTargets = data.words.map((item) => new Target(item, true));
      // Bắt đầu trò chơi
      startGame();
    })
    .catch((error) => {
      console.error("Có lỗi xảy ra khi lấy dữ liệu:", error);
    });

  // Hàm lấy ngẫu nhiên các mục từ listTargets
  function getRandomTargets(listTargets, targetCount) {
    var shuffled = listTargets.sort(() => 0.5 - Math.random());
    return shuffled.slice(0, targetCount);
  }

  // Hàm tạo phần tử span từ target
  function createTargetElement(target) {
    const GAMEAREA = document.getElementById("game-area");
    const targetElement = document.createElement("span");
    targetElement.textContent = target.name;
    targetElement.classList.add("target");
    targetElement.style.left = Math.random() * 90 + "%"; // Đặt vị trí ngẫu nhiên

    // Thêm sự kiện khi kết thúc hoạt ảnh
    targetElement.addEventListener("animationend", function () {
      level.gameStatus = false;
      targetElement.remove();
    });

    GAMEAREA.appendChild(targetElement);
  }

  // Bắt đầu trò chơi
  function startGame() {
    // Tự động focus vào ô textbox khi DOM đã sẵn sàng
    document.getElementById("typeInput").focus();
    if (!level) return; // Chờ đến khi level được khởi tạo

    const { listTargets, targetCount } = level;

    // Tạo danh sách ngẫu nhiên từ listTargets
    const shuffled = getRandomTargets(listTargets, targetCount);

    // Khởi tạo trò chơi với các mục tiêu ngẫu nhiên
    intervalId = setInterval(() => {
      if (shuffled.length === 0) {
        clearInterval(intervalId);
        return;
      }
      const randomTarget = shuffled.pop();
      createTargetElement(randomTarget);
    }, 1000); // Tạo từ mới mỗi giây
  }

  // Lấy dữ liệu từ ô textbox khi nhấn phím dấu cách
  document
    .getElementById("typeInput")
    .addEventListener("keydown", function (event) {
      if (event.code === "Space") {
        event.preventDefault();
        const textboxValue = document.getElementById("typeInput").value.trim();
        const fallingWords = document.querySelectorAll(".target");
        let found = false;

        fallingWords.forEach((wordElement) => {
          if (wordElement.textContent === textboxValue) {
            found = true;
            // Ẩn phần tử từ rơi
            wordElement.style.visibility = "hidden";

            // Tìm đối tượng target tương ứng và cập nhật status
            const target = level.listTargets.find(
              (t) => t.name === textboxValue
            );
            if (target) {
              target.status = false;
            }
          }
        });
        document.getElementById("typeInput").value = "";
      }
    });
});
