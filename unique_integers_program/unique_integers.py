import os
import sys
import time
import glob

class UniqueInt:
    def __init__(self):
        # Range for integers (-1023 to 1023)
        self.RANGE_MIN = -1023
        self.RANGE_MAX = 1023
        self.ARRAY_SIZE = self.RANGE_MAX - self.RANGE_MIN + 1
        self.seen_integers = [False] * self.ARRAY_SIZE
        
        # For tracking performance
        self.start_time = 0
        self.end_time = 0
    
    def value_to_index(self, value):
        """Convert integer value to array index"""
        return value - self.RANGE_MIN
    
    def index_to_value(self, index):
        """Convert array index to integer value"""
        return index + self.RANGE_MIN
    
    def parse_line(self, line):
        """Parse a line, returning a valid integer or None"""
        # Trim whitespace
        line = line.strip()
        
        # Skip empty lines
        if not line:
            return None
        
        # Check if the line contains only one integer
        parts = line.split()
        if len(parts) != 1:
            return None
        
        # Try to parse the integer
        try:
            num = int(parts[0])
            
            # Check if it's within range
            if num < self.RANGE_MIN or num > self.RANGE_MAX:
                return None
                
            return num
        except ValueError:
            # Not a valid integer
            return None
    
    def process_file(self, input_file_path, output_file_path):
        """Process a file to find unique integers and write them to output"""
        print(f"\nProcessing {input_file_path}...")
        
        # Reset the seen integers array
        self.seen_integers = [False] * self.ARRAY_SIZE
        
        # Track time and memory
        self.start_time = time.time()
        
        try:
            # Read input file
            with open(input_file_path, 'r') as file:
                for line in file:
                    num = self.parse_line(line)
                    if num is not None:
                        # Mark this integer as seen
                        self.seen_integers[self.value_to_index(num)] = True
            
            # Write unique integers to output file
            with open(output_file_path, 'w') as file:
                for i in range(self.ARRAY_SIZE):
                    if self.seen_integers[i]:
                        value = self.index_to_value(i)
                        file.write(f"{value}\n")
            
            self.end_time = time.time()
            processing_time = (self.end_time - self.start_time) * 1000  # Convert to ms
            
            print(f"✓ Completed successfully!")
            print(f"  Runtime: {processing_time:.2f} ms")
            
            return True, processing_time
            
        except Exception as e:
            print(f"✗ Error processing file: {e}")
            return False, 0

def create_folders():
    """Create necessary folders if they don't exist"""
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create paths for input and output folders
    input_folder = os.path.join(script_dir, "sample_inputs")
    output_folder = os.path.join(script_dir, "sample_results")
    
    # Create folders if they don't exist
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"Created input folder: {input_folder}")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")
    
    return input_folder, output_folder

def process_all_files(input_folder, output_folder):
    """Process all files in the input folder"""
    processor = UniqueInt()
    results = []
    
    # Get all files in the input folder
    input_files = glob.glob(os.path.join(input_folder, "*"))
    
    if not input_files:
        print(f"No files found in {input_folder}")
        return []
    
    print(f"Found {len(input_files)} files to process")
    
    for input_file in input_files:
        if os.path.isfile(input_file):
            # Get base filename for the output
            base_name = os.path.basename(input_file)
            output_file = os.path.join(output_folder, f"{base_name}_results.txt")
            
            # Process the file
            success, runtime = processor.process_file(input_file, output_file)
            
            if success:
                results.append((base_name, runtime))
    
    return results

def process_specific_file(input_file, output_folder):
    """Process a specific input file"""
    processor = UniqueInt()
    
    if not os.path.exists(input_file):
        print(f"Error: File not found: {input_file}")
        return False
    
    # Get base filename for the output
    base_name = os.path.basename(input_file)
    output_file = os.path.join(output_folder, f"{base_name}_results.txt")
    
    # Process the file
    success, _ = processor.process_file(input_file, output_file)
    return success

def print_help():
    """Print help information"""
    print("\nUnique Integers Processor - Help")
    print("================================")
    print("This program processes text files containing integers and outputs files")
    print("with unique integers sorted in ascending order.")
    print("\nUsage:")
    print("  python unique_integers_terminal.py [options]")
    print("\nOptions:")
    print("  -h, --help       Show this help message")
    print("  -a, --all        Process all files in the sample_inputs folder")
    print("  -f FILE, --file FILE  Process a specific file")
    print("\nExamples:")
    print("  python unique_integers_terminal.py --all")
    print("  python unique_integers_terminal.py --file sample_inputs/sample_input_01.txt")
    print("\nNote: If run without options, the program will enter interactive mode.")

def interactive_mode(input_folder, output_folder):
    """Run the program in interactive mode"""
    while True:
        print("\n===== Unique Integers Processor =====")
        print("1. Process all files in sample_inputs folder")
        print("2. Process a specific file")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            results = process_all_files(input_folder, output_folder)
            if results:
                print("\nSuccessfully processed files:")
                for name, runtime in results:
                    print(f"- {name} (Runtime: {runtime:.2f} ms)")
                print(f"\nResults saved in: {output_folder}")
            
        elif choice == '2':
            print(f"\nFiles in {input_folder}:")
            files = os.listdir(input_folder)
            for i, file in enumerate(files):
                print(f"{i+1}. {file}")
            
            if not files:
                print("No files found. Please add files to the sample_inputs folder.")
                continue
                
            file_choice = input("\nEnter the number of the file to process (or 'b' to go back): ")
            if file_choice.lower() == 'b':
                continue
                
            try:
                index = int(file_choice) - 1
                if 0 <= index < len(files):
                    file_path = os.path.join(input_folder, files[index])
                    process_specific_file(file_path, output_folder)
                else:
                    print("Invalid file number")
            except ValueError:
                print("Invalid input")
                
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    """Main function to handle command line arguments"""
    # Create necessary folders
    input_folder, output_folder = create_folders()
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help']:
            print_help()
        elif sys.argv[1] in ['-a', '--all']:
            results = process_all_files(input_folder, output_folder)
            if results:
                print("\nSuccessfully processed files:")
                for name, runtime in results:
                    print(f"- {name} (Runtime: {runtime:.2f} ms)")
                print(f"\nResults saved in: {output_folder}")
        elif sys.argv[1] in ['-f', '--file'] and len(sys.argv) > 2:
            file_path = sys.argv[2]
            process_specific_file(file_path, output_folder)
        else:
            print("Invalid option. Use --help to see available options.")
    else:
        # Enter interactive mode if no command line arguments
        interactive_mode(input_folder, output_folder)

if __name__ == "__main__":
    main()