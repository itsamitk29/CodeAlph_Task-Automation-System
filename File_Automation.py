import os
import shutil
import re
import requests


class TaskAutomation:

    def __init__(self):
        print("=" * 50)
        print("      TASK AUTOMATION SYSTEM")
        print("=" * 50)


    def move_image_files(self):

        source = input("Enter Source Folder Path: ")
        destination = input("Enter Destination Folder Path: ")

        if not os.path.exists(source):
            print("Source folder not found.")
            return

        if not os.path.exists(destination):
            os.makedirs(destination)

        count = 0

        for file in os.listdir(source):

            if file.lower().endswith((".jpg", ".jpeg", ".png")):

                source_file = os.path.join(source, file)
                destination_file = os.path.join(destination, file)

                shutil.move(source_file, destination_file)

                print(file, "moved successfully.")
                count += 1

        if count == 0:
            print("No JPG files found.")
        else:
            print(f"\nTotal {count} image file(s) moved successfully.")


    def extract_emails(self):

        input_file = input("Enter Input Text File: ")
        output_file = input("Enter Output File Name: ")

        if not os.path.exists(input_file):
            print("Input file not found.")
            return

        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        emails = re.findall(pattern, text)

        emails = list(set(emails))

        with open(output_file, "w", encoding="utf-8") as file:

            for email in emails:
                file.write(email + "\n")

        print(f"{len(emails)} email(s) saved in '{output_file}'")


    def scrape_title(self):

        url = input("Enter Website URL: ")
        output_file = input("Enter Output File Name: ")

        try:

            response = requests.get(url)

            if response.status_code == 200:

                match = re.search(
                    r"<title>(.*?)</title>",
                    response.text,
                    re.IGNORECASE | re.DOTALL
                )

                if match:

                    title = match.group(1).strip()

                    with open(output_file, "w", encoding="utf-8") as file:
                        file.write("Website : " + url + "\n")
                        file.write("Title : " + title)

                    print("Website title saved successfully.")

                else:
                    print("Title not found.")

            else:
                print("Unable to open website.")

        except:
            print("Internet connection or URL problem.")


    def menu(self):

        while True:

            print("\n" + "=" * 50)
            print("      TASK AUTOMATION SYSTEM")
            print("=" * 50)
            print("1. Move JPG or PNG or JPEG Files")
            print("2. Extract Email Addresses")
            print("3. Scrape Website Title")
            print("4. Exit")
            print("=" * 50)

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                print("\n--- Move JPG or PNG Files ---")
                self.move_image_files()

            elif choice == "2":
                print("\n--- Extract Email Addresses ---")
                self.extract_emails()

            elif choice == "3":
                print("\n--- Scrape Website Title ---")
                self.scrape_title()

            elif choice == "4":
                print("\nThank you for using Task Automation System.")
                break

            else:
                print("\nInvalid choice! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    obj = TaskAutomation()
    obj.menu()
