from datetime import datetime

def static_version(request):
    # إضافة توقيع زمني كنسخة (يمكن تغييره للتحديث حسب الحاجة)
    return {'static_version': int(datetime.now().timestamp())}
