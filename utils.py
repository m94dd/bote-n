# -*- coding: utf-8 -*-
"""
هذا الملف يحتوي على أدوات مساعدة (دوال) للبوت.
"""

def load_and_process_melzma(file_path):
    """
    يحمل الملزمة من الملف وينظفها (يشيل الزوائد).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # هنا يمكنك تضيف خطوات إضافية لتنظيف النص إذا احتجت
    return text
