#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def split_name(full_name):
    """
    Splits a full name into given name and surname.
    Assumes the last word is the surname, and the rest is the given name.

    Args:
        full_name (str): The full name to split.

    Returns:
        tuple: (given_name, surname)
    """
    parts = full_name.strip().split()
    if not parts:
        return "", ""
    surname = parts[-1]
    given_name = " ".join(parts[:-1]) if len(parts) > 1 else ""
    return given_name, surname


def convert_record(record_lines):
    """
    Converts a list of lines representing a single record into a
    tilde-separated string with fields: Full Name~Given Name~Surname~[remaining lines].

    Args:
        record_lines (list): A list of strings for the record.

    Returns:
        str: The converted record or None if empty.
    """
    if not record_lines:
        return None

    # Get full name from first non-empty line
    full_name = next((line.strip() for line in record_lines if line.strip()), "")
    if not full_name:
        return None

    given_name, surname = split_name(full_name)

    # Collect remaining non-empty lines, excluding the first non-empty line
    remaining_lines = [line.strip() for line in record_lines if line.strip() and line.strip() != full_name]

    # Combine all fields: Full Name~Given Name~Surname~remaining lines
    return "~".join([full_name, given_name, surname] + remaining_lines)


def main():
    # Initialize Tkinter root (hidden)
    root = tk.Tk()
    root.withdraw()

    # Prompt for input file
    input_file_name = filedialog.askopenfilename(
        title="Select Input File",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not input_file_name:
        messagebox.showerror("Error", "No input file selected. Exiting.")
        return

    # Prompt for output file, default to .csv
    output_file_name = filedialog.asksaveasfilename(
        title="Select Output File",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if not output_file_name:
        messagebox.showerror("Error", "No output file selected. Exiting.")
        return

    # Check input file existence
    if not os.path.exists(input_file_name):
        messagebox.showerror("Error", f"The input file '{input_file_name}' was not found.")
        return

    try:
        with open(input_file_name, 'r', encoding='utf-8') as infile, open(output_file_name, 'w',
                                                                          encoding='utf-8') as outfile:
            # Write header
            outfile.write("Full Name~Given Name~Surname~Type~Census~Other~Location~Birth Year~Where Born\n")

            current_record_lines = []
            for line in infile:
                line = line.strip()
                if line == "||":
                    # End of record
                    if current_record_lines:
                        converted_record = convert_record(current_record_lines)
                        if converted_record:
                            outfile.write(converted_record + "\n")
                    current_record_lines = []
                elif line:
                    current_record_lines.append(line)

            # Process last record
            if current_record_lines:
                converted_record = convert_record(current_record_lines)
                if converted_record:
                    outfile.write(converted_record + "\n")

        messagebox.showinfo("Success", f"Conversion complete! Output saved to '{output_file_name}'.")
    except Exception as e:
        messagebox.showerror("Error", f"Error during processing: {e}")


if __name__ == "__main__":
    main()
