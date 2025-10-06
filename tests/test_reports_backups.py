import os
from modules import report_generator, scheduler_tasks

def test_pdf_generation():
    path = report_generator.generate_daily_pdf_report()
    assert os.path.exists(path), "PDF-Bericht sollte erstellt werden."

def test_backup_creation_and_rotation():
    path = scheduler_tasks.create_backup_zip()
    assert os.path.exists(path), "Backup sollte erstellt werden."
    scheduler_tasks.rotate_backups(2)
    backups = [f for f in os.listdir("data/backups") if f.endswith(".zip")]
    assert len(backups) <= 2, "Es sollten maximal 2 Backups behalten werden."
