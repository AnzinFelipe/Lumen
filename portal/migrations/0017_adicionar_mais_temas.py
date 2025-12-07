from django.db import migrations

def criar_novos_temas(apps, schema_editor):
    Tema = apps.get_model('portal', 'Tema')
    novos_temas = [
        'Saúde',
        'Educação',
        'Cultura',
        'Climática Global',
        'Climática Local',
        'Política Global',
        'Política Local',
        'Receita',
        'Segurança',
        'Saúde e Bem-Estar',
        'Tecnologia',
        'Esportes',
        'Economia',
        'Entretenimento',
        'Mobilidade'
    ]
    
    for tema_nome in novos_temas:
        Tema.objects.get_or_create(tema=tema_nome)
    print("Novos temas criados com sucesso!")

def remover_novos_temas(apps, schema_editor):
    Tema = apps.get_model('portal', 'Tema')
    novos_temas = [
        'Saúde',
        'Educação',
        'Cultura',
        'Climática Global',
        'Climática Local',
        'Política Global',
        'Política Local',
        'Receita',
        'Segurança',
        'Saúde e Bem-Estar',
        'Tecnologia',
        'Esportes',
        'Economia',
        'Entretenimento',
        'Mobilidade'
    ]
    
    Tema.objects.filter(tema__in=novos_temas).delete()
    print("Novos temas removidos!")

class Migration(migrations.Migration):
    dependencies = [
        ('portal', '0010_temas_iniciais'),
    ]

    operations = [
        migrations.RunPython(criar_novos_temas, remover_novos_temas),
    ]