let currentNewsIndex = 0;
let newsData = [];

function loadNewsData() {
    fetch('newsData.json')
        .then(response => response.json())
        .then(data => {
            newsData = data.news;
            loadNextNews(); // 初始化新闻加载
        })
        .catch(error => console.error('Error loading the news data:', error));
}

function loadNextNews() {
    if (currentNewsIndex < newsData.length) {
        const newsItem = newsData[currentNewsIndex];
        const newsContainer = document.getElementById('newsContainer');
        newsContainer.innerHTML = `<h2>${newsItem.title}</h2><p>${newsItem.content}</p><button onclick="verifyNews(${newsItem.fake})">Verify</button>`;
        currentNewsIndex++;
    } else {
        alert('No more news!');
        currentNewsIndex = 0; // Reset for replayability
    }
}

function verifyNews(isFake) {
    const newsContainer = document.getElementById('newsContainer');
    if (isFake) {
        // 播放声音
        playSound();
        newsContainer.innerHTML = `<img src="cosimo.jpeg" alt="Fake News"><p class="fake-news-text">Haha, fake news!</p>`;
        setTimeout(loadNextNews, 5300); // Wait for 3 seconds before loading the next news
    } else {
        alert('Wrong, this news is true!');
        loadNextNews(); // Load the next news item
    }
}

function playSound() {
    var audio = new Audio('fake.mp3'); // 替换成您的音频文件路径
    audio.play();
}

window.onload = loadNewsData; // Use loadNewsData to start the game
