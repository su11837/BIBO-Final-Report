from flask import Flask, render_template, jsonify, request
#為了開網頁
static_folder = r"C:\Users\shuping\Desktop\page\ststic"
template_folder = r"C:\Users\shuping\Desktop\page\templates"
app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
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
    return render_template('index.html', css_files=css_files, js_files=js_files)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='8080', debug=True)