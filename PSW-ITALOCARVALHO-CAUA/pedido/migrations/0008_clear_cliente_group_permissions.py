from django.db import migrations


def clear_cliente_permissions(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    group = Group.objects.filter(name="Cliente").first()
    if group:
        group.permissions.clear()


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("pedido", "0007_pedido_numero_pedido"),
    ]

    operations = [
        migrations.RunPython(clear_cliente_permissions, migrations.RunPython.noop),
    ]
