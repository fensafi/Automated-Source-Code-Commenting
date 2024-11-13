def insert_comments(source_code, comments):
    # Logic to add comments to code
    final_code = source_code
    for item, comment in comments.items():
        # Insert comment before function or class
        final_code = final_code.replace(f"def {item}", f"# {comment}\ndef {item}")
    return final_code
