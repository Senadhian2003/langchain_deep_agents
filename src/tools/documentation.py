"""Documentation tool for creating markdown files."""


def document_findings(
    content: str,
    filename: str = "findings.md",
    output_dir: str = "./output",
):
    """
    Document findings and create a markdown file.
    
    Args:
        content: The content to document
        filename: Name of the markdown file to create
        output_dir: Directory where the file should be created
    
    Returns:
        str: Success message
    """
    # Log what is passed
    print(f"[DOCUMENTATION TOOL] Creating document: {filename}")
    print(f"[DOCUMENTATION TOOL] Output directory: {output_dir}")
    print(f"[DOCUMENTATION TOOL] Content length: {len(content)} characters")
    print(f"[DOCUMENTATION TOOL] Content preview: {content[:200]}...")
    
    # Return dummy response
    return f"Document created successfully: {output_dir}/{filename}"

