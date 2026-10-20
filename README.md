# CryptoAML Guard System

[ 🇷🇺 Русский ] 

---

## 🇷🇺 Описание проекта

**CryptoAML Guard** — это программный прототип аналитической системы для обнаружения аномальных и мошеннических транзакций в децентрализованных финансовых (блокчейн) сетях с использованием **графовых нейронных сетей (GNN)**. 

Система предназначена для задач AML (Anti-Money Laundering) комплаенса, финансового мониторинга и автоматической оценки рисков (Risk Scoring) криптовалютных адресов и транзакций.

### 🛠 Технологический стек
* **Язык программирования:** Python 3.10+
* **Машинное обучение / GNN:** PyTorch, PyTorch Geometric (PyG) (архитектура GCN)
* **Бэкенд (API):** FastAPI, Uvicorn
* **Обработка данных:** NetworkX, Pandas, NumPy
* **Фронтенд и Визуализация:** HTML5, CSS3, JavaScript (ES6), Vis.js Network

### 🚀 Быстрый запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone [https://github.com/Aidana91/crypto-aml-system.git](https://github.com/Aidana91/crypto-aml-system.git)
   cd crypto-aml-system
2. **Запустите бэкенд:**
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
Сервер запустится по адресу: http://127.0.0.1:8000

 **Запустите интерфейс:**
Откройте файл frontend/index.html в вашем браузере (или через расширение Live Server в VS Code).


