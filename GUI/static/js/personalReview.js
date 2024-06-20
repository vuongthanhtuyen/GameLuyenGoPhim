let myChart;

class PersonalReview {
    constructor(id, recordWord) {
        this.id = id;
        this.recordWord = recordWord;
    }
}

// Lưu đối tượng vào Local Storage
function savePersonalReview(id, recordWord) {
    let reviews = JSON.parse(localStorage.getItem('personalReviews')) || [];
    
    // Kiểm tra xem id đã tồn tại trong Local Storage chưa
    let exists = reviews.some(review => review.id === id);
    if (!exists) {
        let review = new PersonalReview(id, recordWord);
        reviews.push(review);
        localStorage.setItem('personalReviews', JSON.stringify(reviews));
    }
}
// Lấy dữ liệu từ Local Storage và hiển thị trên biểu đồ đường
function loadChartData() {
    let reviews = JSON.parse(localStorage.getItem('personalReviews')) || [];
    let labels = reviews.map(review => `#${review.id}`);
    let data = reviews.map(review => review.recordWord);

    const ctx = document.getElementById('myChart').getContext('2d');

    if (myChart) {
        myChart.destroy(); // Hủy biểu đồ cũ nếu nó tồn tại
    }

    myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
                fill: false
            }]
        },
        options: {
            scales: {
                y: {
                    display: true,
                    beginAtZero: true,
                    ticks: {
                        color: '#b1b0b0',  // Set the color of the y-axis labels
                        padding: 0  // Remove padding to place y-axis right at the edge
                    }
                }

                ,
                x: {
                    display: false,

                }
            },
            plugins: {
                legend: {
                    display: false // Hide the legend
                }
            }

        }
        
    });
}

// Hàm để xóa dữ liệu từ Local Storage
function clearData() {
    localStorage.removeItem('personalReviews');
    loadChartData(); // Tải lại dữ liệu và cập nhật biểu đồ
    location.reload(); // Tải lại trang
}

// Xử lý dữ liệu từ Python khi tải trang
function handleDataFromPython(dataFromPython) {
    if (dataFromPython) {
        savePersonalReview(dataFromPython.id, dataFromPython.recordWord);
    }
    loadChartData(); // Tải dữ liệu và hiển thị biểu đồ
}


// Gán sự kiện click cho nút Clear Data
document.getElementById('clearDataButton').addEventListener('click', clearData);

// Tải dữ liệu và hiển thị biểu đồ khi trang được tải lần đầu
loadChartData();

// Gọi hàm để xử lý dữ liệu từ Python (dữ liệu này sẽ được truyền từ file HTML)
document.addEventListener('DOMContentLoaded', () => {
    const dataFromPython = JSON.parse(document.getElementById('data-from-python').textContent);
    handleDataFromPython(dataFromPython);
});
