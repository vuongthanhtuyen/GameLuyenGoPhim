from flask import Blueprint, render_template, flash, redirect, url_for
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


@manageData_bl.route('/test', methods=['GET'])
def test():

    from DAL.readfile import mylist
    import json
    
    data = {"words": mylist()}


    # with open('./GUI/static/json/listWords.json', 'w') as file:
    #     # Bước 4: Sử dụng json.dump() để ghi dữ liệu
    #     json.dump(mylist(), file)
    with open('./GUI/static/json/listWords.json', 'w', encoding='utf-8') as file:
        # Bước 4: Sử dụng json.dump() để ghi dữ liệu với ensure_ascii=False
        json.dump(data, file, ensure_ascii=False, indent=4)



    # Mở file ở chế độ đọc
    with open('./GUI/static/json/listWords.json', 'r', encoding='utf-8') as file:
        # Sử dụng json.load() để đọc dữ liệu từ file và chuyển đổi nó thành danh sách
        loaded_list = json.load(file)
        
    words_list = data.get("words", [])

    # print("Danh sách đã được đọc từ file my_list.json:", loaded_list)
        
    return render_template('test.html', mylist = words_list) 





