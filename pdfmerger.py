#!/usr/bin/env python

import PyPDF2
import os

input_files = dict()
input_loc = os.getcwd()
output_file_name = input("Enter the name of the consolidated file: ")
merger = PyPDF2.PdfMerger()
position = 1

for file in os.listdir(input_loc):
    if file.endswith(".pdf"):
        input_files[file] = position
        position += 1

print(f"Current order: {input_files}")
while True:
    choice = input("\nRetain the order / Reorder / Delete: ").lower()

    if choice == "retain":
        print("\nRETAINING\n")
        break

    elif choice == "reorder":
        print("\nREORDERING\n")
        available_positions = [x for x in range(1, len(input_files.keys()) + 1)]
        print("Enter the new order: (1-based)")
        for i in input_files.keys():
            print(f"Available Positions: {available_positions}")
            pos = int(input(f"Enter a position for {i}: "))
            while True:
                if pos in available_positions:
                    input_files[i] = pos
                    available_positions.remove(pos)
                    break
                else:
                    pos = int(input(f"Invalid position. Enter the position for {i} again: "))    

        sorted_keys = sorted(input_files, key=lambda x: input_files[x])
        reordered_dict = {key: input_files[key] for key in sorted_keys}        
        input_files = reordered_dict

    elif choice == "delete":
        print("\nDELETING\n")
        pos = int(input("Choose the file's position you want to delete: "))
        available_positions = list(range(1, len(input_files.keys()) + 1))

        to_delete = []
        for i in input_files.keys():
            if input_files[i] == pos:
                to_delete.append(i)

        if not to_delete:
            print(f"No file found at position {pos}")
        else:
            for i in to_delete:
                input_files.pop(i)
            for i in input_files.keys():
                if input_files[i] > pos:
                    input_files[i] -= 1
    else:
        print("Invalid Choice.")

    print(f"\nCurrent order: {input_files}")

for file in input_files:
        input_file_path = os.path.abspath(file)
        merger.append(input_file_path)

output_file_path = f"{output_file_name}.pdf"
merger.write(output_file_path)
merger.close()

print(f"Consolidated PDF saved as: {output_file_path}")
