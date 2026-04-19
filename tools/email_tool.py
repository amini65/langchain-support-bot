from langchain.tools import tool
from config.settings import settings

@tool
def send_email_summary(conversation_summary: str) -> str:
    """This tool sends a conversation summary to the admin via email"""
    # در پروژه واقعی از SMTP استفاده کن
    print(f"EMAIL SENT TO: {settings.ADMIN_EMAIL}")
    print(f"SUBJECT: Customer Support Conversation Summary")
    print(f"CONTENT:\n{conversation_summary}")
    print(f"{'='*50}\n")

    return f"Summary successfully sent to {settings.ADMIN_EMAIL}"
