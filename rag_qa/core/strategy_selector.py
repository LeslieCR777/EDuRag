# -*-coding:utf-8-*-
# core/strategy_selector.py 源码
import sys, os
# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# print(f'current_dir--》{current_dir}')
# 获取core文件所在的目录的绝对路径
rag_qa_path = os.path.dirname(current_dir)
# print(f'rag_qa_path--》{rag_qa_path}')
sys.path.insert(0, rag_qa_path)
# 获取根目录文件所在的绝对位置
project_root = os.path.dirname(rag_qa_path)
sys.path.insert(0, project_root)
# 导入日志和配置
from base import logger, Config
import requests
import json


class StrategySelector:
    def __init__(self):
        # 获取策略选择提示模板
        self.strategy_prompt_template = self._get_strategy_prompt()
        self.config = Config()

    def call_ollama(self, prompt):
        # 调用本地 Ollama
        try:
            url = f"{self.config.OLLAMA_BASE_URL}/api/chat"
            payload = {
                "model": self.config.LLM_MODEL,
                "messages": [
                    {"role": "system", "content": "你是一个有用的助手。"},
                    {"role": "user", "content": prompt}
                ],
                "stream": False,
                "options": {"temperature": 0.1}
            }
            response = requests.post(url, json=payload, timeout=30)
            data = response.json()
            return data.get("message", {}).get("content", "直接检索")
        except Exception as e:
            logger.error(f"Ollama 调用失败: {e}")
            return "直接检索"

    def _get_strategy_prompt(self):
        template = """
你是一个智能助手，负责分析用户查询 {query}，并从以下四种检索增强策略中选择一个最适合的策略，直接返回策略名称，不需要解释过程。

以下是几种检索增强策略及其适用场景：

1.  **直接检索：**
    * 适用场景：查询意图明确，需要检索特定信息的问题。
2.  **假设问题检索（HyDE）：**
    * 适用场景：查询较为抽象，直接检索效果不佳的问题。
3.  **子查询检索：**
    * 适用场景：查询涉及多个实体或方面，需要分别检索不同信息的问题。
4.  **回溯问题检索：**
    * 适用场景：查询较为复杂，需要简化后才能有效检索的问题。

根据用户查询 "{query}"，直接返回最适合的策略名称，例如 "直接检索"。不要输出任何分析过程或其他内容。
"""
        return template
    #   定义方法，选择检索策略
    def select_strategy(self, query):
        strategy = self.call_ollama(self.strategy_prompt_template.format(query=query)).strip()
        # print(f'strategy--》{strategy}')
        logger.info(f"为查询 '{query}' 选择的检索策略：{strategy}")
        return strategy

if __name__ == '__main__':
    ss = StrategySelector()
    # print(f'ss.clinet--->{ss.client}')
    # result = ss.call_dashscope(prompt="你是谁")
    # print(f'result--》{result}')
    ss.select_strategy(query="Mysql数据库能不能支持100w个样本的插入")