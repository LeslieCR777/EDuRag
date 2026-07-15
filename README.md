# EDuRag - 智能问答系统

> **Edu**cation + **R**etrieval-**A**ugmented **G**eneration

一个集成了 MySQL 知识库问答和 RAG（检索增强生成）的智能问答系统，专为教育场景设计。

## 系统架构

```
integrated_qa_system/
├── app.py              # FastAPI 服务入口 (WebSocket + REST API)
├── new_main.py         # 系统核心编排
├── mysql_qa/           # MySQL 知识库问答模块
│   ├── db/             # 数据库连接
│   ├── cache/          # Redis 缓存
│   ├── retrieval/      # BM25 检索
│   └── data/           # 知识问答数据
├── rag_qa/             # RAG 检索增强生成模块
│   ├── core/           # 核心逻辑 (分类器、向量库、策略选择)
│   ├── edu_document_loaders/  # 文档加载器 (PDF/PPT/Docx/图片OCR)
│   ├── edu_text_spliter/      # 文本分割器
│   └── models/         # 模型文件 (BERT、BGE-M3、BGE-Reranker)
└── static/             # 前端页面
```

## 功能特点

- **双引擎问答**: 同时支持结构化 MySQL 查询和语义化 RAG 检索
- **多格式文档支持**: PDF、PPT、Word、图片 OCR
- **智能分类**: BERT 模型自动判断问题类型，选择最优策略
- **流式响应**: 支持 SSE 流式输出
- **WebSocket 实时通信**: 前端实时交互

## Hospital 对接

本系统可作为医院智能问答的知识库引擎，支持：
- 医疗文档（PDF/Word）导入与向量化
- 医疗知识库问答检索
- 灵活对接医院信息系统（HIS）

## 快速开始

```bash
# 安装依赖
pip install -r requirments.txt

# 启动服务
python app.py

# 访问地址
# http://localhost:8000
# http://localhost:8000/docs (API 文档)
```

## 依赖环境

- Python 3.8+
- MySQL 数据库
- Redis 缓存
- 大模型 API (兼容 OpenAI API 格式)
