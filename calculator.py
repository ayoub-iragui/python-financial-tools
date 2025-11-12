# برنامج آلة حاسبة تفاعلية
num1_str = input("أدخل الرقم الأول: ")
num2_str = input("أدخل الرقم الثاني: ")

# الخطوة الحاسمة: تحويل النص إلى رقم صحيح (Integer) قبل الجمع
num1 = int(num1_str)
num2 = int(num2_str)

# إجراء عملية الجمع
sum_result = num1 + num2

# طباعة النتيجة النهائية
print("نتيجة جمع الرقمين هي:", sum_result)
