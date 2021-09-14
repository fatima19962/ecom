from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="edr",
                          email="fatemeh.afvaj1996@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="9301274130",
                          gender="Famale"
                          )
        user.set_password("fa4420587490")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
