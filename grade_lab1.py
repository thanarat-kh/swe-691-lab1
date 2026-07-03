def calculate_grade(scores):
    # 1. ตรวจสอบกรณีลิสต์ว่าง เพื่อป้องกัน ZeroDivisionError
    if not scores:
        return "No Grade", 0
    
    # 2. ใช้ sum() เพื่อความรวดเร็วและอ่านง่าย (แทนการใช้ loop บวกทีละตัว)
    total = sum(scores)
    average = total / len(scores)
    
    # 3. การเช็คเงื่อนไขเกรด (คงเดิมไว้เพราะ logic ถูกต้องแล้ว)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# ตัวอย่างการใช้งาน
scores = [85, 92, 78, 88, 95]
grade, avg = calculate_grade(scores)
print(f"Average: {avg:.2f}, Grade: {grade}")

# ทดสอบกรณีลิสต์ว่าง (จะไม่เกิด Error แล้ว)
empty_scores = []
print(calculate_grade(empty_scores))
