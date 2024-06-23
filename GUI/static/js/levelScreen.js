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
  function recordTurn(nowLevel, recordDate, totalTarget, totalTime) {
    this.nowLevel = nowLevel;
    this.recordDate = recordDate;
    this.totalTarget = totalTarget;
    this.totalTime = totalTime;
  }

  // Khởi tạo level
  var shuffledCheck;
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
    })
    .then(() => {
      // Bắt đầu trò chơi
      startGame();
    })
    .catch((error) => {
      console.error("Có lỗi xảy ra khi lấy dữ liệu:", error);
    });

  function getRandomTargets(level) {
    // Tạo một mảng chứa các đối tượng Target ngẫu nhiên
    var shuffled = [];

    // Tạo một bản sao của mảng level.listTargets để trộn ngẫu nhiên
    var copyListTargets = [...level.listTargets];

    // Trộn ngẫu nhiên các phần tử trong mảng copyListTargets
    copyListTargets.sort(() => 0.5 - Math.random());

    // Lấy targetCount phần tử đầu tiên từ mảng đã trộn
    shuffled = copyListTargets.slice(0, level.targetCount);
    // Console.log(shuffled)

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
      level.gameStatus = false;
      targetElement.remove();
    });

    GAMEAREA.appendChild(targetElement);
  }

  function startGame() {
    document.getElementById("typeInput").focus();
    if (!level) return;

    // Tạo danh sách ngẫu nhiên từ listTargets
    const shuffled = getRandomTargets(level);

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

  document.getElementById("typeInput").addEventListener("keydown", function (event) {
    if (event.code === "Space") {
      event.preventDefault();
      const textboxValue = document.getElementById("typeInput").value.trim();
      const fallingWords = document.querySelectorAll(".target");

      fallingWords.forEach((wordElement) => {
        if (wordElement.textContent === textboxValue) {
          wordElement.remove();

          // Tìm và cập nhật trạng thái của đối tượng trong level.poppedTargets
          const targetToUpdate = level.poppedTargets.find((t) => t.name === textboxValue);
          console.log(level.poppedTargets);
          if (targetToUpdate) {
            console.log("Đối tượng Target:", targetToUpdate);
            // Cập nhật trạng thái của đối tượng
            targetToUpdate.status = false; // Ví dụ cập nhật status thành false
            console.log(level.poppedTargets);

            // Thực hiện bất kỳ công việc nào khác sau khi cập nhật
          } else {
            console.log(`Không tìm thấy target với name '${textboxValue}'`);
          }
        }
      });

      document.getElementById("typeInput").value = "";
    }
  });
});
