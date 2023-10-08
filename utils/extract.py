""" This script copies the latest CSV file from the 'Downloads' folder to the 'datasets' folder."""
import os
import shutil


def copy_latest_csv_to_datasets():
    """
    the latest CSV file from the 'Downloads' folder to the 'datasets' folder is copied

    """
    current_directory = os.path.abspath(os.path.dirname(__file__))

    datasets_dir = os.path.join(current_directory, "..", "datasets")
    if not os.path.exists(datasets_dir):
        print(
            "Error: 'datasets' folder does not exist"
            + "Please make sure you are in the root directory of the clone repo."
        )
        return

    downloads_dir = os.path.expanduser("~/Downloads")
    csv_files = [f for f in os.listdir(downloads_dir) if f.endswith(".csv")]

    if not csv_files:
        print("Error: No CSV files found in the 'Downloads' folder.")
        return  # Exit from here

    latest_csv = max(
        csv_files, key=lambda x: os.path.getctime(os.path.join(downloads_dir, x))
    )

    # https://stackoverflow.com/questions/123198/how-to-copy-files
    shutil.copy(os.path.join(downloads_dir, latest_csv), datasets_dir)
    print(f"Successfully copied '{latest_csv}' to 'datasets' folder.")


# if __name__ == '__main__':
#     copy_latest_csv_to_datasets()
