import PyPDF2
import random
import re
from typing import List

def extract_text_from_pdf(pdf_file: str) -> List[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            if content:  # Kiểm tra nếu nội dung không rỗng
                pdf_text.append(content)
                
    
        # Ghép tất cả các đoạn văn bản thành một chuỗi dài
        full_text = ' '.join(pdf_text)
        
        # Chuyển đổi chuỗi thành một danh sách các từ
        word_list = full_text.split()

        # Định nghĩa biểu thức chính quy để phát hiện ký tự đặc biệt, cho phép các ký tự tiếng Việt
        special_char_pattern = re.compile(r'[^a-zA-Z0-9ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸỳỵỷỹ]')
        
        # Lọc từ danh sách các từ, bỏ qua những từ có ký tự đặc biệt hoặc ít hơn 2 ký tự
        filtered_word_list = [word for word in word_list if len(word) >= 2 and not special_char_pattern.search(word)]

        # Sử dụng tập hợp để loại bỏ các từ trùng lặp
        unique_word_list = list(set(filtered_word_list))

        
        return unique_word_list

   

# thismy = extract_text_from_pdf('./DAL/filePDF/TTHCMCK.pdf')
# print(len(thismy))