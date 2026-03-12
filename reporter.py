import json

def generate_report(results, format='json'):
    if format == 'json':
        return json.dumps(results, indent=2)
    elif format == 'sarif':
        # Basic SARIF conversion (simplified)
        sarif = {
            "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
            "version": "2.1.0",
            "runs": [{
                "tool": {"driver": {"name": "BugFinder"}},
                "results": []
            }]
        }
        for cat, items in results.items():
            for item in items:
                sarif["runs"][0]["results"].append({
                    "ruleId": cat,
                    "message": {"text": str(item)},
                    "locations": [{"physicalLocation": {"artifactLocation": {"uri": item.get('file', 'unknown')}}}]
                })
        return json.dumps(sarif, indent=2)
    else:
        return str(results)
