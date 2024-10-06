import googlemaps # pip install googlemaps (if needed)
import csv

class APIClass:
    """Class to interact with Google Maps API for calculating distances between various addresses and the headquarter."""

    def __init__(self, api_key, addresses):
        """
        Initializes the APIClass with the Google Maps API key and a dictionary of addresses.
        
        Args:
            api_key (str): The API key for accessing Google Maps.
            addresses (dict): A dictionary containing names as keys and corresponding addresses as values.
        """
        self.client = googlemaps.Client(key=api_key)
        self.addresses = addresses


    def get_hq_location(self, keyname='Adchieve HQ'):
        """
        Retrieves the geographical location of the headquarter from Google Maps API.
        
        Args:
            (optional) keyname (str): The keyname of the headquarter in the addresses dictionary.

        Returns:
            dict: A dictionary containing the latitude and longitude of the headquarters.
        """
        hq_address = self.addresses[keyname]
        del self.addresses[keyname]  # Remove the HQ address from the addresses list (needed for calculate_distances method)
        response = self.client.geocode(hq_address)
        return response[0]['geometry']['location']


    def calculate_distances(self, reference_address):
        """
        Calculates the distances from all addresses in self.addresses with respect to reference_address.
        
        Args:
            reference_address (dict): The geographical location of an address.
        
        Returns:
            list: A list of tuples containing distance, address key, and address.
        """
        distances = []
        ref_lat, ref_lng = reference_address['lat'], reference_address['lng']

        for key, address in self.addresses.items():
            response = self.client.geocode(address)
            if response:
                location = response[0]['geometry']['location']
                lat, lng = location['lat'], location['lng']
                # Calculate distance using (Haversine formula for distances on a sphere (earth))
                distance = ((lat - ref_lat) ** 2 + (lng - ref_lng) ** 2) ** 0.5 * 111.32  # rough distance in km
                distances.append((distance, key, address))

        return distances


    def save_distances_to_csv(self, distances):
        """
        Saves the calculated distances to a CSV file.
        
        Args:
            distances (list): A list of tuples containing distance, address key, and address.
        """
        with open('distances.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Sortnumber", "Distance", "Name", "Address"])
            for index, (distance, name, address) in enumerate(sorted(distances, key=lambda x: x[0]), start=1):
                writer.writerow([index, f"{distance:.2f} km", name, address])


    def print_distances(self, distances):
        """
        Prints the calculated distances to the console.
        
        Args:
            distances (list): A list of tuples containing distance, address key, and address.
        """
        for index, (distance, name, address) in enumerate(sorted(distances, key=lambda x: x[0]), start=1):
            print(f"{index}, \"{distance:.2f} km\", \"{name}\", \"{address}\"")
