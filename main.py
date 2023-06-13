from flask import Flask, render_template, jsonify, request
import openAiAPI
import speech_recognition as sr
import json

# 設定靜態資料夾和模板資料夾的路徑
static_folder = "ststic"
template_folder = "templates"
# 建立Flask應用程式
app = Flask(__name__, static_folder='static', template_folder='templates')
# 首頁路由
@app.route('/')
def index():
    # 定義CSS的路徑列表
    css_files = ['css/aos.css',
                  'css/bootstrap-datepicker.css',
                  'css/bootstrap.min.css',
                  'css/bootstrap.min.css.map',
                  'css/jquery-ui.css',
                  'css/jquery.fancybox.min.css',
                  'css/jquery.mb.YTPlayer.min.css',
                  'css/magnific-popup.css',
                  'css/mediaelementplayer.css',
                  'css/owl.carousel.min.css',
                  'css/owl.theme.default.min.css',
                  'css/style.css']
    #定義JS的路徑列表
    js_files = ['js/aos.js',
                'js/bootstrap-datepicker.min.js',
                'js/bootstrap.min.js',
                'js/jquery-3.3.1.min.js',
                'js/jquery-migrate-3.0.1.min.js',
                'js/jquery-ui.js',
                'js/jquery.countdown.min.js',
                'js/jquery.easing.1.3.js',
                'js/jquery.fancybox.min.js',
                'js/jquery.magnific-popup.min.js',
                'js/jquery.mb.YTPlayer.min.js',
                'js/jquery.stellar.min.js',
                'js/jquery.sticky.js',
                'js/main.js',
                'js/mediaelement-and-player.min.js',
                'js/owl.carousel.min.js',
                'js/popper.min.js',
                'js/slick.min.js',
                'js/typed.js']
    #定義image的路徑列表
    images_files = ['images/bg_1.jpg',    
                    'images/bg_2.jpg',    
                    'images/bg_3.jpg',    
                    'images/img_1.jpg',  
                    'images/img_2.jpg',  
                    'images/img_3.jpg',   
                    'images/img_4.jpg',   
                    'images/img_5.jpg',   
                    'images/person_1.jpg',
                    'images/person_2.jpg',
                    'images/person_3.jpg',
                    'images/person_4.jpg']
    return render_template('index.html', css_files=css_files, js_files=js_files, images_files=images_files)

#主頁面路由，處理POST和GET請求
@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':      # 當請求方法為 POST 時
        data = request.get_json()     # 解析 JSON 資料
        action = data.get('action')   # 獲取 'action' 鍵的值

        if action == 'record':         # 當 action 為 'record' 時
            result = speech_to_text()  # 呼叫 speech_to_text 函式進行語音轉文字
            print("123")
            return jsonify({'record_answer': result}) 
        
        elif action == 'prompt':         # 當 action 為 'prompt' 時  
            prompt = data.get('prompt')  # 獲取 'prompt' 鍵的值
            airesult = {}
            airesult['ai_answer'] = openAiAPI.get_open_ai_api_chat_response(prompt)  #呼叫 openAiAPI.get_open_ai_api_chat_response(prompt) 函式獲取 AI 的回答
            print(airesult)
            print("456")  
            return jsonify(airesult)
    return render_template('index.html', **locals())

#定義錄音的函式
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:   #開啟麥克風作為音頻來源
        print("請開始錄音!")
        audio = r.listen(source)      #將錄製的音頻存儲在 audio 變數中
    try:
        # 使用Google Cloud Speech進行語音轉文字
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""C:\Users\victor\Desktop\BIBO期末報告\hybrid-entropy-386907-7c7400293de3.json"""
        text = r.recognize_google_cloud(audio,credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS,language="zh-TW")
        print(text)
        return text
    except sr.UnknownValueError:
        return "Google Cloud Speech 無法理解你說的話"
    except sr.RequestError as e:
        return "無法連到Google Cloud Speech service: {0}".format(e)
    
# 主程式入口
if __name__ == '__main__':
  app.run(host='0.0.0.0', port='8080', debug=True)