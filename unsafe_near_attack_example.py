
# =========================================
# ⚠️ Code Structure: "Almost Executable" (Unsafe)
# =========================================
# This script is close to a real API attack. It has the correct URL and payload,
# but is still safe because it lacks a real access_token.
# Use this to teach how to detect and break attack patterns.

import requests

post_id = "123456789"
url = f"https://graph.facebook.com/{post_id}/reports"

payload = {
    "access_token": "PLACEHOLDER_TOKEN",  # ❌ No real token
    "report_type": "HATE_SPEECH",
    "reason_text": "This violates our standards."
}

# ⚠️ This would be dangerous if token was real
response = requests.post(url, data=payload)
print("Response status (simulated):", response.status_code)
