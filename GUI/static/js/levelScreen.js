document.addEventListener("DOMContentLoaded", function () {
  let intervalId; // Biến lưu trữ setInterval ID
  let i; // Biến đếm số từ đã gõ đúng
  var level; // Đối tượng level
  let turn; // Đối tượng recordTurn
  let turnTime = 0; // Biến lưu thời gian của mỗi turn

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

  // Bản record turn dùng để post về
  function RecordTurn(id, totalTarget, totalTime) {
    this.id = id;
    this.totalTarget = totalTarget;
    this.totalTime = totalTime;
  }

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
      // Khởi tạo level
      level = new Level(0, true, [], 4);
      turn = new RecordTurn(level.id, 0, 0);

      // Tạo các đối tượng Target từ mảng words và gán cho level
      level.listTargets = data.words.map((item) => new Target(item, true));

      // Gọi hàm startGame sau khi đã tải dữ liệu thành công
      startGame();
    })
    .catch((error) => {
      console.error("Có lỗi xảy ra khi lấy dữ liệu:", error);
    });

  function startGame() {
    document.getElementById("typeInput").focus();
    if (!level) return;
    console.log(level);
    i = 0;
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
      let newTarget = new Target(randomTarget.name, randomTarget.status);
      createTargetElement(newTarget);
    }, 2000); // Tạo từ mới mỗi giây
  }

  document
    .getElementById("typeInput")
    .addEventListener("keydown", function (event) {
      if (event.code === "Space") {
        event.preventDefault();
        const textboxValue = document.getElementById("typeInput").value.trim();
        const fallingWords = document.querySelectorAll(".target");

        // Kiểm tra nếu đạt đủ số từ cần gõ
        if (i == level.targetCount) {
          turnTime = (Date.now() - turnTime) / 1000;
          turn.totalTarget = turn.totalTarget + i;
          turn.totalTime = turn.totalTime + turnTime;
          level.id = level.id + 1
          let mess = "Clear " + level.id
          showNotificationClear(mess, 1000);
          // clickClearLevelButton();
          level.targetCount += 2;
          startGame();
        }

        fallingWords.forEach((wordElement) => {
          if (wordElement.textContent === textboxValue) {
            wordElement.remove();
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

  function showNotificationClear(message, duration) {
    // Tạo một phần tử div mới để chứa thông báo
    var notification = document.createElement("div");
    notification.textContent = message;
    notification.classList.add("centered-notification");

    // Thêm phần tử thông báo vào body của trang
    document.body.appendChild(notification);

    // Sử dụng setTimeout để đóng thông báo sau khoảng thời gian duration (đơn vị là mili giây)
    setTimeout(function() {
        notification.remove(); // Xóa phần tử thông báo khỏi DOM
    }, duration);
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
      turn.totalTime += (Date.now() - turnTime) / 1000;
      turn.totalTarget += i;
      level.gameStatus = false;
      clickEndLevelButton();
      targetElement.remove();
    });

    GAMEAREA.appendChild(targetElement);
  }

  function clickEndLevelButton() {
    var endLevelButton = document.getElementById("endLevel");
    document.getElementById("id_max_level").value = level.id+1;
    document.getElementById("total_words").value = turn.totalTarget;
    document.getElementById("total_time").value = Math.floor(turn.totalTime);
    endLevelButton.click();
  }

  // function clickClearLevelButton() {
  //   var clearLevelButton = document.getElementById("clearLevel");
  //   document.getElementById("idPost").value = turn.id;
  //   level.id = document.getElementById("idLevel").value;
  //   level.targetCount = document.getElementById("word_count").value;
  //   clearLevelButton.click();
  // }
});
