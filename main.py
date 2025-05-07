# -*- coding: utf-8 -*-
"""
هذا الملف الرئيسي لبوت شرح الملزمة.
راح يحمل النموذج اللغوي ويعالج الملزمة ويجاوب على أسئلة المستخدم.
"""

from transformers import AutoTokenizer, AutoModelForCausalLM

# اسم النموذج اللي راح نستخدمه (يمكنك تغييره)
model_name = "aubmindlab/AraBERT2-base-L2"  # مثال: AraBERT. يمكنك استخدام نماذج أخرى تدعم اللغة العربية
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def load_and_process_melzma(file_path):
    """
    يحمل الملزمة من الملف وينظفها (يشيل الزوائد).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # هنا يمكنك تضيف خطوات إضافية لتنظيف النص إذا احتجت
    return text

def get_jawb(question, context, tokenizer, model):
    """
    ياخذ السؤال ونص الملزمة وينطي الجواب باستخدام النموذج اللغوي.
    """
    prompt = f"استنادًا إلى النص التالي: '{context}'، جاوب على السؤال التالي: '{question}'"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=200)  # يمكنك تعديل هذا الرقم
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # استخرج الجواب من النص المتولد (هذه الخطوة قد تحتاج إلى تحسين)
    return response.split("جاوب على السؤال التالي:")[1].strip()

if __name__ == "__main__":
    melzma_content = load_and_process_melzma("path/to/your/melzma.txt")  # حط مسار ملف الملزمة هنا
    while True:
        user_question = input("اسأل سؤالك (أو اكتب 'خروج' للخروج): ")
        if user_question.lower() == 'خروج':
            break
        jawb = get_jawb(user_question, melzma_content, tokenizer, model)
        print("جواب البوت:", jawb)