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

🇬🇧 Project Description
CryptoAML Guard is a software prototype of an analytical system designed to detect anomalous and fraudulent transactions in decentralized financial (blockchain) networks using Graph Neural Networks (GNN).

The system is built for AML (Anti-Money Laundering) compliance, financial monitoring, and automated risk scoring of cryptocurrency addresses and transactions.

🛠 Tech Stack
Programming Language: Python 3.10+

Machine Learning / GNN: PyTorch, PyTorch Geometric (PyG) (GCN Architecture)

Backend API: FastAPI, Uvicorn

Data Processing: NetworkX, Pandas, NumPy

Frontend & Visualization: HTML5, CSS3, JavaScript (ES6), Vis.js Network

🚀 Quick Start
Clone the repository:

Bash
git clone [https://github.com/Aidana91/crypto-aml-system.git](https://github.com/Aidana91/crypto-aml-system.git)
cd crypto-aml-system
Run the backend server:

Bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
The server will run at: http://127.0.0.1:8000

Launch the frontend interface:

Open the frontend/index.html file in your browser (or use Live Server in VS Code).

