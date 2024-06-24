from flask import Blueprint, render_template, flash, redirect, url_for, Response
from DAL.seedData import SeedData
manageData_bl = Blueprint('manageData', __name__,template_folder='../GUI/templates/')



@manageData_bl.route('/manageData', methods=['GET'])
def manageData():
    from DTO.models.Level_db  import Level_db
    levels = Level_db.query.all()
    return render_template('manageData.html', levels=levels) # trả về bảng level, truy cập vào: http://127.0.0.1:5000/manageDa

@manageData_bl.route('/seedData', methods=['GET'])
def seedData():
    SeedData()
    flash('SEED DATA thành công!',category='success')

    return redirect(url_for('home'))


# import requests
# from bs4 import BeautifulSoup
# import nltk
# import json
# @manageData_bl.route('/loadJsonWord', methods=['GET'])
# def LoadJsonWord():
#     # Đảm bảo tải xuống các tài nguyên cần thiết của NLTK
#     nltk.download('punkt')

#     # Hàm để lấy nội dung từ một URL
#     def fetch_web_content(url):
#         response = requests.get(url)
#         response.raise_for_status()  # Đảm bảo yêu cầu thành công
#         return response.text

#     # Hàm để lọc và lấy các từ thuần túy từ HTML content
#     def extract_pure_words_from_html(html_content):
#         soup = BeautifulSoup(html_content, 'html.parser')

#         # Lấy toàn bộ văn bản từ trang web
#         text = soup.get_text()

#         # Tokenize văn bản
#         tokens = nltk.word_tokenize(text)

#         # Lọc các từ thuần túy (chỉ chứa ký tự chữ cái)
#         words = [w for w in tokens if w.isalpha()]

#         return words

#     # URL của trang web bạn muốn lấy nội dung
#     url = 'https://www.vinmec.com/vi/tin-tuc/thong-tin-suc-khoe/dinh-duong/rau-muong-co-tac-dung-gi/'

#     # Lấy nội dung từ trang web
#     html_content = fetch_web_content(url)

#     # Lấy các từ thuần túy từ nội dung HTML
#     words = extract_pure_words_from_html(html_content)

#     # Tạo cấu trúc JSON
#     output = {
#         "words": words
#     }

#     # Chuyển đổi cấu trúc JSON thành chuỗi với ensure_ascii=False
#     json_data = json.dumps(output, ensure_ascii=False)

#     # Trả về JSON response
#     return Response(json_data, content_type='application/json; charset=utf-8')

@manageData_bl.route('/test', methods=['GET'])
def test():
    from DAL.readfile import extract_text_from_pdf
    import json
    
    data = {"words": extract_text_from_pdf('./DAL/filePDF/TTHCMCK.pdf')}
    with open('./GUI/static/json/listWords.json', 'w', encoding='utf-8') as file:
        # Bước 4: Sử dụng json.dump() để ghi dữ liệu với ensure_ascii=False
        json.dump(data, file, ensure_ascii=False, indent=4)
        
    flash('Đã update jsonfile!',category='success')

    return redirect(url_for('home'))

