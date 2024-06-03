# BLL/business_logic.py

class UserLogic:
    def validate_user(self, username, password):
        # Logic kiểm tra người dùng, ví dụ: kiểm tra tên đăng nhập và mật khẩu

        if len(username) < 3:
            return False, "Tên đăng nhập quá ngắn"
        if len(password) < 6:
            return False, "Mật khẩu quá ngắn"
        
        return True, "Đăng nhập thành công"

class ProjectLogic:
    def create_project(self, project_name):
        # Logic tạo dự án

        if len(project_name) < 5:
            return False, "Tên dự án quá ngắn"
        
        # Gọi các phương thức từ lớp DTO để thực hiện tạo dự án
        # ...

        return True, "Dự án đã được tạo thành công"
