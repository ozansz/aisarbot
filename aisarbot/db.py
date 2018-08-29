import peewee as pw

from aisarbot import settings

db = pw.SqliteDatabase(settings.DATABASE)

class BaseModel(pw.Model):
    class Meta:
        database = db

class User(BaseModel):
    # Telegram user id
    tid = pw.IntegerField(unique=True)
    first_name = pw.CharField(null=True)
    last_name = pw.CharField(null=True)
    username = pw.CharField(null=True)
    is_bot = pw.BooleanField(null=True)
    gender = pw.CharField(null=True)
    location = pw.CharField(null=True)
    int_gender = pw.CharField(null=True)
    int_age = pw.IntegerField(null=True)

def create_tables():
    with db:
        db.create_tables([User])

def create_user(tid):
    return User.create(tid=tid)

def create_user_if_not_exists(tid):
    try:
        user = User.get(User.tid == tid)
    except User.DoesNotExist:
        create_user(tid)
        return 1

    return 0

def update_user(tid, **kwargs):
    try:
        user = User.get(User.tid == tid)
    except User.DoesNotExist:
        create_user(tid)

    for arg in kwargs:
        if arg in User._meta.fields and arg != "tid":
            setattr(user, arg, kwargs[arg])

    return user.save()
