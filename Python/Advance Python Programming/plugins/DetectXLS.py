def main(fileExtension):
    if fileExtension in {".xlsx", '.xls', '.xlx'}:
        return "Excel sheet file"
    else:
        return None