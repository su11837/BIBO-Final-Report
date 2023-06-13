import openai
def get_open_ai_api_chat_response(prompt):
  openai.api_key = "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"
  #建立一個字典叫做user_prompt
  user_prompt = {}
  user_prompt['role'] = 'user'
  user_prompt['content'] = prompt
  #建立一個空列表叫做message
  messages = []
  messages.append({"role": "assistant", "content": "你是一位負責進行課程內容重點整理的助教"})
  messages.append(user_prompt)
  # 送出發送 API 請求到 Open AI，使用了GPT-3.5 Turbo 模型
  response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
  ai_answer = response["choices"][0]["message"]["content"].replace("\n", "<br>")
  print(ai_answer)
  # 把答案送回給呼叫這個方程的地方
  return ai_answer