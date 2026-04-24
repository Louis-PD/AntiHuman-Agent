from fastapi import FastAPI, BackgroundTasks
from core.brain import AntiHumanAgent
from tools.slacker import anti_human_delay
import os

app = FastAPI()
# 初始化大脑（实际生产环境建议从环境变量读取 Key）
agent = AntiHumanAgent(api_key="YOUR_OPENAI_API_KEY", base_url="YOUR_BASE_URL")

def process_and_send(user_id, message):
    # 1. AI 思考回复
    reply = agent.think_and_reply(message)
    # 2. 执行摸鱼延迟
    anti_human_delay(reply)
    # 3. 这里调用飞书/钉钉的 API 发送消息
    print(f"已成功代发回复给用户 {user_id}: {reply}")

@app.post("/webhook")
async def handle_im_event(request: dict, background_tasks: BackgroundTasks):
    user_msg = request.get("content")
    user_id = request.get("user_id")
    
    # 放入后台任务执行，防止 Webhook 超时
    background_tasks.add_task(process_and_send, user_id, user_msg)
    
    return {"code": 0, "msg": "event_received"}
