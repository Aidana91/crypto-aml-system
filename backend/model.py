import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

class CryptoGCN(nn.Module):
    def __init__(self, in_channels: int, hidden_channels: int, out_channels: int = 2):
        super(CryptoGCN, self).__init__()
        # Первый сверточный графовый слой
        self.conv1 = GCNConv(in_channels, hidden_channels)
        # Второй сверточный графовый слой
        self.conv2 = GCNConv(hidden_channels, hidden_channels)
        # Полносвязный слой для классификации
        self.classifier = nn.Linear(hidden_channels, out_channels)
        self.dropout = nn.Dropout(p=0.2)

    def forward(self, x, edge_index):
        # x: Признаки узлов [num_nodes, in_channels]
        # edge_index: Рёбра графа [2, num_edges]
        
        # 1-я агрегация соседей
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.dropout(x)
        
        # 2-я агрегация соседей
        x = self.conv2(x, edge_index)
        x = F.relu(x)
        
        # Классификация узла
        out = self.classifier(x)
        return F.log_softmax(out, dim=1)