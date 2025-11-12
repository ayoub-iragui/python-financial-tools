# برنامج حاسبة ضريبة القيمة المضافة (الآن مع اتخاذ القرارات)

VAT_RATE = 0.15 # قيمة الضريبة 15%
print("مرحبا بك في حاسبة ضريبة القيمة المضافة.")
print("---------------------------------------")

# 1. الحصول على سعر المنتج من المستخدم
price_str = input("أدخل سعر المنتج الأصلي: ")
original_price = float(price_str)

# 2. خطوة اتخاذ القرار!
if original_price < 50:
    # إذا كان السعر أقل من 50، يتخذ هذا القرار:
    print("هذا المنتج معفى من الضريبة (السعر أقل من 50).")
    total_price = original_price 
    vat_amount = 0
else:
    # وإلا (إذا كان 50 أو أكثر)، يتخذ هذا القرار:
    vat_amount = original_price * VAT_RATE
    total_price = original_price + vat_amount

# 3. طباعة النتائج النهائية
print("\n--- النتائج ---")
print("قيمة الضريبة المضافة هي:", vat_amount, "درهم/ريال")
print("الإجمالي النهائي هو:", total_price, "درهم/ريال")
