// Данные о каждом компоненте
const componentsData = {
    cpu: {
        title: "Процессор",
        description: "Процессор — это мозг компьютера. Он обрабатывает команды и управляет всеми задачами. Пример: Intel Core i9, AMD Ryzen 7.",
        image: "images/cpu.png"
    },
    gpu: {
        title: "Видеокарта",
        description: "Видеокарта отвечает за обработку графики. Пример: NVIDIA GeForce RTX 3080, AMD Radeon RX 6800.",
        image: "images/gpu.png"
    },
    motherboard: {
        title: "Материнская плата",
        description: "Материнская плата соединяет все компоненты ПК и позволяет им взаимодействовать. Пример: ASUS ROG Strix Z490-E, MSI B450 Tomahawk.",
        image: "images/motherboard.png"
    },
    ram: {
        title: "Оперативная память",
        description: "Оперативная память временно хранит данные для быстрого доступа процессора. Пример: Corsair Vengeance 16GB, G.SKILL Ripjaws 32GB.",
        image: "images/ram.png"
    },
    storage: {
        title: "Накопитель",
        description: "Накопитель (SSD или HDD) — это устройство для долговременного хранения данных. Пример: Samsung 970 Evo, Western Digital Blue.",
        image: "images/storage.png"
    }
};

// Функция для обновления информации о компоненте
function updateComponentInfo(item) {
    const title = document.querySelector('.component-title');
    const description = document.querySelector('.component-description');
    const image = document.getElementById('component-image');

    if (componentsData[item]) {
        title.innerText = componentsData[item].title;
        description.innerText = componentsData[item].description;
        image.src = componentsData[item].image;
        image.style.display = "block";
    } else {
        title.innerText = "Выберите компонент";
        description.innerText = "Нажмите на кнопку для получения информации.";
        image.style.display = "none";
    }
}

// Добавляем обработчики событий для кнопок
document.querySelectorAll('.component-button').forEach(button => {
    button.addEventListener('click', () => {
        const item = button.getAttribute('data-item');
        updateComponentInfo(item);
    });
});
