from datetime import datetime

def generate_report(results):
    date= datetime.now().strftime("%Y-%m-%d")
    report= f"#Daily Research Report\n\n"
    report += f"Date: {date}\n\n"

    for item in results:
        report += (
            f"## {item['title']}\n\n"

        )
        report+= item['analysis']
        report += "\n\n--\n\n"
    return report