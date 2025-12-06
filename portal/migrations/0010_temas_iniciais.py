from django.db import migrations

def criar_temas_iniciais(apps, schema_editor):
    Tema = apps.get_model('portal', 'Tema')
    temas = ['Esportes', 'Política', 'Economia', 'Tecnologia', 'Entretenimento', 'Mobilidade']
    
    for tema_nome in temas:
        Tema.objects.get_or_create(tema=tema_nome)
    print("Temas iniciais criados com sucesso!")

def remover_temas_iniciais(apps, schema_editor):
    Tema = apps.get_model('portal', 'Tema')
    temas = ['Esportes', 'Economia', 'Tecnologia', 'Entretenimento', 'Mobilidade']
    
    Tema.objects.filter(tema__in=temas).delete()
    print("Temas iniciais removidos!")

class Migration(migrations.Migration):
    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_temas_iniciais, remover_temas_iniciais),
    ]