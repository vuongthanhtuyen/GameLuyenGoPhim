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


@manageData_bl.route('/loadJsonWord', methods=['GET'])
def LoadJsonWord():

    from DAL.readfile import extract_text_from_pdf
    import json
    
    data = {"words": extract_text_from_pdf('./DAL/filePDF/TTHCMCK.pdf')}
    with open('./GUI/static/json/listWords.json', 'w', encoding='utf-8') as file:
        # Bước 4: Sử dụng json.dump() để ghi dữ liệu với ensure_ascii=False
        json.dump(data, file, ensure_ascii=False, indent=4)
        
    flash('Đã update jsonfile!',category='success')

    return redirect(url_for('home'))


@manageData_bl.route('/testLoadFile', methods=['GET'])
def TestLoadFile():

    return render_template('test.html')

