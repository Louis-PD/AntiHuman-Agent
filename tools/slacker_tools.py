import time
import random

def anti_human_delay(text_content):
    """
    根据回复内容的长度，计算出一个合理的“摸鱼延迟”
    """
    # 模拟人类打字速度：每秒 2-4 个字
    typing_speed = len(text_content) * random.uniform(0.3, 0.8)
    
    # 核心：带薪摸鱼随机延迟 (60秒到300秒)
    slacking_time = random.uniform(60, 300) 
    
    total_wait = typing_speed + slacking_time
    
    print(f"--- [摸鱼日志] ---")
    print(f"生成回复字数: {len(text_content)}")
    print(f"预计进入‘带薪延迟’状态: {total_wait:.2f} 秒")
    
    time.sleep(total_wait)
