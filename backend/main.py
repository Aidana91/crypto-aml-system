from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
import random
from model import CryptoGCN

app = FastAPI(title="Crypto AML Detection API", version="1.0")

# Включаем CORS для свободного подключения фронтенда (index.html)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализация модели
IN_FEATURES = 16
HIDDEN_DIM = 32
model = CryptoGCN(in_channels=IN_FEATURES, hidden_channels=HIDDEN_DIM)
model.eval()

class AnalyzeRequest(BaseModel):
    wallet_address: str

@app.get("/")
def root():
    return {"status": "Online", "system": "GNN Crypto Fraud Detection System"}

@app.post("/api/v1/analyze")
def analyze_transaction(request: AnalyzeRequest):
    address = request.wallet_address
    
    # 1. Имитация получения локального графа вокруг проверяемого адреса
    # В реальности здесь выборка подграфа из Neo4j или датасета Elliptic
    num_neighbors = random.randint(3, 6)
    
    # Генерация случайного графа для демо
    x = torch.randn((num_neighbors + 1, IN_FEATURES))
    
    # Создаем связи: проверяемый узел (0) соединен с соседями (1..N)
    source_nodes = [0] * num_neighbors + list(range(1, num_neighbors + 1))
    target_nodes = list(range(1, num_neighbors + 1)) + [0] * num_neighbors
    edge_index = torch.tensor([source_nodes, target_nodes], dtype=torch.long)
    
    # 2. Инференс (предсказание) GNN-модели
    with torch.no_grad():
        out = model(x, edge_index)
        probs = torch.exp(out)[0]  # Вероятности для целевого узла 0
        fraud_prob = float(probs[1].item())
    
    # Нормализуем Risk Score для стабильности демо
    risk_score = round(fraud_prob * 100, 1)
    status = "HIGH RISK (Suspicious)" if risk_score > 50 else "LOW RISK (Clean)"
    
    # 3. Формирование графа для визуализации (Vis.js / Cytoscape)
    nodes = [{"id": 0, "label": f"Target:\n{address[:8]}...", "color": "#FF4D4D" if risk_score > 50 else "#2ECC71"}]
    edges = []
    
    for i in range(1, num_neighbors + 1):
        is_suspicious = random.choice([True, False]) if risk_score > 50 else False
        color = "#E74C3C" if is_suspicious else "#95A5A6"
        nodes.append({"id": i, "label": f"Addr_{i}", "color": color})
        edges.append({"from": 0, "to": i})
        
    return {
        "address": address,
        "risk_score": risk_score,
        "status": status,
        "model_used": "Graph Convolutional Network (GCN)",
        "graph_data": {
            "nodes": nodes,
            "edges": edges
        }
    }