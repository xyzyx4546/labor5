# Runbook: Backup & Restore MedCloud-Connect

Stand: 2026-10-19 (nach CHG-1027)

## Ablauf
- Job `medcloud-backup` läuft täglich 02:00 UTC auf backup-01 (Identität: svc-medcloud).
- Exportiert die Tabellen patients, reports, users als CSV und schreibt dazu MANIFEST.sha256.
- Upload in zwei Buckets:
  - `medcloud-backup`: Lifecycle-Regel löscht Snapshots nach 7 Tagen (system:lifecycle, 04:00 UTC).
  - `medcloud-backup-worm`: Object Lock COMPLIANCE, 30 Tage. Löschen und Überschreiben sind in dieser Zeit für niemanden möglich.
- Protokoll: /var/log/medcloud-backup.log (siehe logs/backup-01_job.log).

## Restore
1. Snapshot-Ordner aus `medcloud-backup` herunterladen.
2. Integrität prüfen: `sha256sum -c MANIFEST.sha256`.
3. Tabellen mit `COPY ... FROM` einspielen.

Restore-Test: noch nicht durchgeführt (offener Punkt aus dem Audit, Nr. 20).
