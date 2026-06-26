from .generator_utils import create_workbook, save_workbook

def generate_company():

    companies = [
        ["NS001","Nova Manufacturing","India","Manufacturing","INR"],
        ["NS002","Nova Retail","India","Retail","INR"],
        ["NS003","Nova Digital","India","Digital","INR"],
        ["NS004","Nova Services","India","Services","INR"],
        ["NS005","Nova Logistics","UAE","Logistics","AED"],
        ["NS006","Nova Healthcare","Singapore","Healthcare","SGD"],
        ["NS007","Nova Energy","USA","Energy","USD"],
        ["NS008","Nova Foods","UK","Food","GBP"],
        ["NS009","Nova Finance","India","Finance","INR"],
        ["NS010","Nova International","Germany","International","EUR"],
    ]

    wb, ws = create_workbook("Company")

    ws.append([
        "CompanyCode",
        "CompanyName",
        "Country",
        "BusinessUnit",
        "Currency"
    ])

    for company in companies:
        ws.append(company)

    save_workbook(
        wb,
        "Data/Master/Company.xlsx"
    )
