import json


def in_format(format_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            if format_type == "csv":
                lines = [f"{key},{value}" for key, value in data.items()]
                return "\n".join(lines)
            elif format_type == "xml":
                lines = [f"<{key}>{value}</{key}>" for key, value in data.items()]
                return "<report>\n" + "\n".join(lines) + "\n</report>"
            elif format_type == "json":
                return json.dumps(data, ensure_ascii=False, indent=2)
            else:
                return str(data)
        return wrapper
    return decorator


@in_format("csv")
def tax_authority_report():
    return {"company": "ABC LLC", "income": 100000, "tax": 18000}


@in_format("xml")
def pension_fund_report():
    return {"company": "ABC LLC", "employees": 50, "contributions": 25000}


@in_format("json")
def statistics_office_report():
    return {"company": "ABC LLC", "revenue": 500000, "profit": 120000, "employees": 50}


if __name__ == "__main__":
    print("Tax authority report (CSV):")
    print(tax_authority_report())

    print("\nPension fund report (XML):")
    print(pension_fund_report())

    print("\nStatistics office report (JSON):")
    print(statistics_office_report())
