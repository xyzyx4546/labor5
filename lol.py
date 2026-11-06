import json, re, pandas as pd

cloud = pd.read_json(
    "logs/cloud_audit.jsonl", lines=True, dtype={"sourceIP": str}
)
cloud["eventTime"] = pd.to_datetime(cloud.eventTime)
idp = pd.read_json("logs/idp_auth.jsonl", lines=True)

# Text-Logs zeilenweise lesen und bei Bedarf per Regex zerlegen
web = open("logs/web_access.log", encoding="utf-8").read().splitlines()

# Erst Überblick, dann Details
cloud.principal.value_counts().head(15)
cloud.groupby(["principal", "sourceIP"]).size().sort_values(ascending=False).head(20)
