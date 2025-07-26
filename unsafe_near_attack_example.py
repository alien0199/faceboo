
# ============================================================
# 🔥 CODE A: High-Risk Structure (Almost Executable Attack)
# ============================================================
# This code is close to a real-world abuse scenario.
# It uses real API URL and complete payload structure.
# Only the access_token is fake. If replaced, the attack would succeed.

import requests

post_id = "123456789"
url = f"https://graph.facebook.com/{post_id}/reports"

payload = {
    "access_token": "PLACEHOLDER_TOKEN",  # ❌ Replace this and it's dangerous
    "report_type": "HATE_SPEECH",
    "reason_text": "This violates our standards."
}

# ⚠️ Would send request to Facebook API if token were real
response = requests.post(url, data=payload)
print("Response status (simulated):", response.status_code)


# ============================================================
# ✅ CODE B: Safe Simulation Structure (Educational)
# ============================================================
# This version is completely safe. It simulates reporting
# without any real API, token, or network activity.

def simulate_report(post_id, user_id, reason):
    print(f"[SIMULATION] {user_id} would report post {post_id} for reason: {reason}")

for i in range(10):
    user = f"user_{i+1:02d}"
    simulate_report("POST_ID_XYZ", user, "SPAM")
