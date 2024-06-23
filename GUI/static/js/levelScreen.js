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
    this.poppedTargets = [];
  }

  // Bản record turn dùng để post về
  function recordTurn(nowLevel, totalTarget, totalTime) {
    this.nowLevel = nowLevel;
    this.totalTarget = totalTarget;
    this.totalTime = totalTime;
  }

  // Khởi tạo level
  var i = 0;
  var level = new Level(1, true, [], 4);
  var turn = new recordTurn(level.id, 0, 0);
  var turnTime = 0;

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
      if (!Array.isArray(data.words)) {
        throw new TypeError("Dữ liệu trả về không chứa mảng words");
      }
      // Tạo các đối tượng Target từ mảng words và gán cho level
      level.listTargets = data.words.map((item) => new Target(item, true));
      startGame();
    })
    .catch((error) => {
      console.error("Có lỗi xảy ra khi lấy dữ liệu:", error);
    });

  function startGame() {
    document.getElementById("typeInput").focus();
    if (!level) return;

    // Tạo danh sách ngẫu nhiên từ listTargets
    const shuffled = getRandomTargets(level);
    turnTime = Date.now();
    // Khởi tạo trò chơi với các mục tiêu ngẫu nhiên
    intervalId = setInterval(() => {
      if (shuffled.length === 0) {
        clearInterval(intervalId);
        return;
      }
      var randomTarget = shuffled.pop();
      // Thêm đối tượng đã pop vào mảng poppedTargets (tạo bản sao)
      let newTarget = new Target(randomTarget.name, randomTarget.status);
      level.poppedTargets.push(newTarget);
      createTargetElement(newTarget);
    }, 1000); // Tạo từ mới mỗi giây
  }

  document
    .getElementById("typeInput")
    .addEventListener("keydown", function (event) {
      if (event.code === "Space") {
        event.preventDefault();
        const textboxValue = document.getElementById("typeInput").value.trim();
        const fallingWords = document.querySelectorAll(".target");
        if (i == level.targetCount) {
          turnTime = (Date.now() - turnTime) / 1000;
          clickClearLevelButton();
        }
        fallingWords.forEach((wordElement) => {
          if (wordElement.textContent === textboxValue) {
            wordElement.remove();
            // Tìm và cập nhật trạng thái của đối tượng trong level.poppedTargets
            if (level.listTargets.find((t) => t.name === textboxValue)) {
              i++;
            }
          }
        });

        document.getElementById("typeInput").value = "";
      }
    });

  function getRandomTargets(level) {
    // Tạo một mảng chứa các đối tượng Target ngẫu nhiên
    var shuffled = [];
    var copyListTargets = [...level.listTargets];
    copyListTargets.sort(() => 0.5 - Math.random());
    shuffled = copyListTargets.slice(0, level.targetCount);
    return shuffled;
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
      turn.totalTime =
        turn.totalTime + (turnTime = (Date.now() - turnTime) / 1000);
      turn.totalTarget = turn.totalTarget + i;
      level.gameStatus = false;
      clickEndLevelButton();
      targetElement.remove();
    });

    GAMEAREA.appendChild(targetElement);
  }

  function clickEndLevelButton() {
    var endLevelButton = document.getElementById("endLevel");
    document.getElementById("id_max_level").value = turn.id;
    document.getElementById("total_words").value = turn.totalTarget;
    document.getElementById("total_time").value = turn.totalTime;
    endLevelButton.click();
  }
  function clickClearLevelButton() {
    var clearLevelButton = document.getElementById("clearLevel");
    turn.totalTarget = turn.totalTarget + i;
    turn.totalTime = turn.totalTime + turnTime;
    clearLevelButton.click();
  }
});
