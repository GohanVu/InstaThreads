import subprocess

# 1. Chạy lệnh RCC để tạo file resource.py
subprocess.run(["rcc", "-g", "python", "-o", "resource.py", "resource.qrc"], check=True)

# 2. Đọc file và thay thế 'PySide2' thành 'PyQt6'
with open("resource.py", "r", encoding="utf-8") as file:
    content = file.read()

content = content.replace("PySide2", "PyQt6")

with open("resource.py", "w", encoding="utf-8") as file:
    file.write(content)

# 3. In thông báo hoàn thành
print("Đã thay đổi 'PySide2' thành 'PyQt6' trong resource.py")
