import yaml
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class AntiHumanAgent:
    def __init__(self, api_key, base_url):
        # 加载性格配置
        with open("config/personality.yaml", "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
            
        self.llm = ChatOpenAI(
            model="gpt-4o", 
            temperature=0.85, # 略高的温度让回答更有随机的“人味”
            api_key=api_key,
            base_url=base_url
        )
        
    def think_and_reply(self, message):
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.config['prompts']['system_instruction']),
            ("human", "{input}")
        ])
        
        # 构建处理链
        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"input": message})
