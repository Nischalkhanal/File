# Import the necessary module to work with URLs and make HTTP requests
from urllib import request

# The URL of the CSV file you want to download
file_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv'

# Function to fetch data from the given CSV URL and save it to a local file
def fetch_data(csv_url):
    # Open the URL and get the response from the server
    response = request.urlopen(csv_url)

    # Read the CSV data from the response
    csv_data = response.read()

    # Convert the CSV data from bytes to a string
    csv_str = str(csv_data)

    # Split the CSV data into lines using the newline character as the separator
    lines = csv_str.split('\\n')

    # Define the destination file where the CSV data will be saved
    dest_file = 'file.csv'

    # Open the destination file in write mode
    with open(dest_file, 'w') as file_writer:
        # Write each line of the CSV data to the file with a newline character
        for line in lines:
            file_writer.write(line + "\n")

# Call the function and provide the CSV URL to download and save the data
fetch_data(file_url)
