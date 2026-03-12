from github import Github

def create_check_run(repo, head_sha, findings):
    g = Github("your_token")
    repo = g.get_repo(repo)
    check_run = repo.create_check_run(
        name="Advanced Bug Finder",
        head_sha=head_sha,
        status="completed",
        conclusion="failure" if findings else "success",
        output={
            "title": "Bug Scan Results",
            "summary": f"Found {len(findings)} issues",
            "annotations": [
                {
                    "path": f["file"],
                    "start_line": f.get("line", 1),
                    "end_line": f.get("line", 1),
                    "annotation_level": "failure" if f["severity"]=="critical" else "warning",
                    "message": f["message"]
                } for f in findings
            ]
        }
    )
    return check_run
