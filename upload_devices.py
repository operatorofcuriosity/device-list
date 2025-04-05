import os
import requests
import json
import subprocess
import base64

# 從環境變數讀取 GitHub Token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("❌ GITHUB_TOKEN 環境變數未設定！")

REPO_NAME = "operatorofcuriosity/device-list"
BRANCH_NAME = "main"

# 設定 git remote URL 使用 Token
remote_url = f"https://{GITHUB_TOKEN}:x-oauth-basic@github.com/{REPO_NAME}.git"

# GitHub API URL
GITHUB_API_URL = f"https://api.github.com/repos/{REPO_NAME}/contents/devices.json"

# 讀取 devices.json 並 Base64 編碼
with open("devices.json", "r", encoding="utf-8") as f:
    file_content = json.dumps(json.load(f))
encoded_content = base64.b64encode(file_content.encode("utf-8")).decode("utf-8")

# 準備上傳資料
data = {
    "message": "Update devices.json with new device list",
    "content": encoded_content,
    "branch": BRANCH_NAME
}
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# 上傳到 GitHub API
response = requests.put(GITHUB_API_URL, headers=headers, json=data)
if response.status_code == 201:
    print("✅ 檔案已成功上傳到 GitHub")
else:
    print(f"⚠️ 上傳失敗: {response.status_code}")
    print(response.json())

# Git push
try:
    subprocess.run(["git", "add", "devices.json"], check=True)
    subprocess.run(["git", "commit", "-m", "Update devices.json"], check=True)
    subprocess.run(["git", "push", remote_url, BRANCH_NAME], check=True)
    print("✅ Git push 成功")
except subprocess.CalledProcessError as e:
    print(f"⚠️ Git 操作失敗: {e}")
