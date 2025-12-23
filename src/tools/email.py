"""Email tool for sending findings via email."""


def send_email(
    recipient: str,
    subject: str,
    summary: str,
    findings: str = None,
):
    """
    Send an email to a recipient about the findings.
    
    Args:
        recipient: Email address of the recipient
        subject: Email subject line
        summary: Summary of the findings
        findings: Optional full findings content
    
    Returns:
        str: Success message
    """
    # Log what is passed
    print(f"[EMAIL TOOL] Sending email to: {recipient}")
    print(f"[EMAIL TOOL] Subject: {subject}")
    print(f"[EMAIL TOOL] Summary length: {len(summary)} characters")
    print(f"[EMAIL TOOL] Summary preview: {summary[:200]}...")
    if findings:
        print(f"[EMAIL TOOL] Full findings length: {len(findings)} characters")
    
    # Return dummy response
    return f"Mail sent successfully to {recipient}"

