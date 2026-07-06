from excel_manager import ExcelManager
from gemini_ai import GeminiAI
from report_generator import ReportGenerator


def main():

    excel = ExcelManager()

    print("=" * 50)
    print("      AI EXCEL REPORT ANALYZER")
    print("=" * 50)

    print("1. Create New Excel Sheet")
    print("2. Import Existing Excel Sheet")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        data = excel.create_new_sheet()

    elif choice == "2":

        data = excel.import_sheet()

    elif choice == "3":

        print("Goodbye!")
        return

    else:

        print("Invalid Choice")
        return

    stats = excel.calculate_statistics()

    excel.create_chart()

    ai = GeminiAI()

    print("\nGenerating AI Summary...\n")

    summary = ai.generate_summary(data, stats)

    report = ReportGenerator(
        excel.get_workbook(),
        excel.get_sheet()
    )

    report.generate_complete_report(
        data,
        summary
    )

    print("\nAI Summary\n")
    print(summary)

    chat = input("\nDo you want to ask questions? (Y/N): ")

    if chat.lower() == "y":
        ai.chat(data, stats)

    print("\nProject Finished Successfully.")


if __name__ == "__main__":
    main()
