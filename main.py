import shutil
import os
from datetime import datetime
import subprocess

def create_daily_file():
    # 1. Define the source template
    source_file = 'archive/new_day_template.py'
    
    # 2. Check if the template exists before proceeding
    if not os.path.exists(source_file):
        print(f"Error: '{source_file}' not found.")
        return

    # 3. Get current date and format it
    # Format: YYYY-DD (e.g., 2025-07.py)
    today_str = datetime.now().strftime('%Y-%d')
    new_filename = f"{today_str}.py"

    # 4. Check if today's file already exists to prevent accidental overwrites
    if os.path.exists(new_filename):
        print(f"File '{new_filename}' already exists. Skipping copy.")
    else:
        try:
            # 5. Copy the file
            shutil.copy(source_file, new_filename)
            print(f"Success! Created '{new_filename}' from '{source_file}'.")
        except Exception as e:
            print(f"An error occurred while copying: {e}")

        try:
            # check=True will raise an error if the script fails (returns non-zero exit code)
            subprocess.run(["uv", "run", new_filename], check=True)
        except FileNotFoundError:
            print("Error: 'uv' command not found. Is uv installed and in your PATH?")
        except subprocess.CalledProcessError as e:
            print(f"Script execution failed with error code {e.returncode}")

if __name__ == "__main__":
    create_daily_file()