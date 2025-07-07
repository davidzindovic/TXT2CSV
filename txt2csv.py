import os
import csv

def convert_txt_to_csv(root_dir):
    # Define paths
    txt_dir = os.path.join(root_dir, 'txt')
    csv_comma_dir = os.path.join(root_dir, 'csv')
    csv_semicolon_dir = os.path.join(root_dir, 'csv_semicolon')
    
    # Create output directories
    os.makedirs(csv_comma_dir, exist_ok=True)
    os.makedirs(csv_semicolon_dir, exist_ok=True)
    
    # Process each file
    for filename in os.listdir(txt_dir):
        if filename.endswith('.txt'):
            txt_path = os.path.join(txt_dir, filename)
            base_name = os.path.splitext(filename)[0]
            
            # Define output paths
            comma_csv_path = os.path.join(csv_comma_dir, f"{base_name}.csv")
            semicolon_csv_path = os.path.join(csv_semicolon_dir, f"{base_name}.csv")
            
            try:
                # Read input file
                with open(txt_path, 'r', encoding='utf-8') as txt_file:
                    rows = [line.strip().split() for line in txt_file if line.strip()]
                
                # Write comma CSV
                with open(comma_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
                    csv.writer(csv_file).writerows(rows)
                
                # Write semicolon CSV with Excel compatibility
                with open(semicolon_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
                    csv_file.write('\ufeff')  # UTF-8 BOM
                    #csv_file.write("sep=;\n")  # Excel delimiter directive
                    writer = csv.writer(csv_file, delimiter=';')
                    writer.writerows(rows)
                
                print(f"Successfully processed {filename}")
            
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))
    convert_txt_to_csv(root_directory)
    print("Conversion complete!")