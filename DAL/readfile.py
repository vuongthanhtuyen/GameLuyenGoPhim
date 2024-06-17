import PyPDF2
import random
import re
from typing import List

def extract_text_from_pdf(pdf_file: str, num_pages: int = None) -> List[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        pdf_text = []

        total_pages = len(reader.pages)
        pages_to_load = min(num_pages, total_pages) if num_pages is not None else total_pages

        for page_number in range(pages_to_load):
            page = reader.pages[page_number]
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

def random_sample_words(word_list: List[str], sample_size: int) -> List[str]:
    return random.sample(word_list, sample_size)

if __name__ == '__main__':
    word_array = extract_text_from_pdf('./DAL/filePDF/QTBH.pdf', num_pages=20)  # Load 20 trang đầu
    sample_size = min(100, len(word_array))  # Đảm bảo không lấy mẫu nhiều hơn số từ có sẵn
    random_words = random_sample_words(word_array, sample_size)
    print(random_words)  # In ra danh sách các từ ngẫu nhiên
