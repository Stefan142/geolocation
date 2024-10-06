from helper import APIClass

# Code will not run if API key is not provided in line 10, so for testers: please do this.

def main():
    """
    Main function to execute the distance calculation process.
    It initializes the API class, retrieves distances, saves to CSV, and prints them.
    """
    api_key = 'Your Own Key'  # Replace with your own API key, (deleted mine because of linkage to credit card)

    addresses = {
        'Adchieve HQ': "Sint Janssingel 92, 5211 DA 's-Hertogenbosch, The Netherlands",  # Adchieve HQ
        'Eastern Enterprise B.V.': "Deldenerstraat 70, 7551AH Hengelo, The Netherlands",  # Eastern Enterprise B.V.
        'Eastern Enterprise': "Plot No 45/46 Main Road Surat, Gujarat, 394210 India",  # Eastern Enterprise (note: adjusted the provided address.)
        'Adchieve Rotterdam': "Weena 505, 3013 AL Rotterdam, The Netherlands",  # Adchieve Rotterdam
        'Sherlock Holmes': "221B Baker St., London, United Kingdom",  # Sherlock Holmes
        'The White House': "1600 Pennsylvania Avenue, Washington, D.C., USA",  # The White House
        'The Empire State Building': "350 Fifth Avenue, New York City, NY 10118",  # Empire State Building
        'The Pope': "Saint Martha House, 00120 Citta del Vaticano, Vatican City",  # The Pope
        'Neverland': "5225 Figueroa Mountain Road, Los Olivos, Calif. 93441, USA"  # Neverland
    }

    calculator = APIClass(api_key, addresses)

    hq_location = calculator.get_hq_location()
    distances = calculator.calculate_distances(hq_location)

    calculator.save_distances_to_csv(distances)
    # calculator.print_distances(distances) # Uncomment this line to print the distances to the console


if __name__ == "__main__":
    main()