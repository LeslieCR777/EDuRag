# -*- coding:utf-8-*-
# 导入标准库
import os
import sys
# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# print(f'current_dir--》{current_dir}')
# 获取core文件所在的目录的绝对路径
rag_qa_path = os.path.dirname(current_dir)
# 获取根目录文件所在的绝对位置
project_root = os.path.dirname(rag_qa_path)
sys.path.insert(0, project_root)
# 导入日志
from base import logger


class QueryClassifier:
    def __init__(self, model_path="bert_query_classifier"):
        # 使用规则分类，不需要加载BERT模型
        self.device = "cpu"
        logger.info(f"使用设备: {self.device}")
        # 专业咨询关键词（课程、学费、报名等IT学习相关）
        self.professional_keywords = [
            "课程", "学费", "报名", "培训", "学习", "班级", "学时", "老师",
            "就业", "大纲", "项目", "证书", "考试", "学制", "晚班", "周末班",
            "教学", "知识点", "章节", "入学", "费用", "退款", "老师",
            "校区", "学校", "机构", "学科", "专业", "知识", "内容",
        ]

    def load_model(self):
        # 不需要加载模型
        pass

    def predict_category(self, query):
        """基于关键词判断：专业咨询 vs 通用知识"""
        if not query:
            return "通用知识"
        for keyword in self.professional_keywords:
            if keyword in query:
                logger.info(f"查询包含关键词'{keyword}'，分类为专业咨询")
                return "专业咨询"
        logger.info("未匹配到专业关键词，分类为通用知识")
        return "通用知识"

    def save_model(self):
        pass
if __name__ == '__main__':
    query_classify = QueryClassifier()
    # data_file = '../classify_data/model_generic_5000.json'
    # query_classify.train_model(data_file)
    result = query_classify.predict_category(query="AI的课程大纲是什么")
    print(result)
