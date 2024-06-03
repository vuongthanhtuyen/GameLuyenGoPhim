# DTO/data_transfer.py

# Định nghĩa các đối tượng dữ liệu (DTO)
class UserDTO:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class ProjectDTO:
    def __init__(self, project_name):
        self.project_name = project_name
