document.querySelectorAll('.component-button').forEach(button => {
    button.addEventListener('click', () => {
        const component = button.getAttribute('data-item');
        showComponentDescription(component);
    });
});

function showComponentDescription(component) {
    const descriptionContainer = document.getElementById('component-description');

    const descriptions = {
        processor: "Процессор — это мозг компьютера. Он обрабатывает команды и управляет всеми задачами. Пример: Intel Core i9, AMD Ryzen 7.",
        gpu: "Видеокарта отвечает за обработку графики. Пример: NVIDIA GeForce RTX 3080, AMD Radeon RX 6800.",
        motherboard: "Материнская плата соединяет все компоненты ПК и позволяет им взаимодействовать. Пример: ASUS ROG Strix Z490-E, MSI B450 Tomahawk.",
        ram: "Оперативная память (RAM) временно хранит данные для быстрого доступа процессора. Пример: Corsair Vengeance 16GB, G.SKILL Ripjaws 32GB.",
        ssd: "SSD — это твердотельный накопитель для хранения данных с высокой скоростью доступа. Пример: Samsung 970 Evo, Kingston A2000.",
        hdd: "Жесткий диск (HDD) — это устройство для долговременного хранения данных. Пример: Western Digital Blue 1TB, Seagate Barracuda 2TB."
    };

    descriptionContainer.textContent = descriptions[component] || "Описание не найдено.";
}
