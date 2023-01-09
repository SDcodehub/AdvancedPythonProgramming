class Temperature:
    """
    Temperature class

    Input:
        Country
        City
    Method:
        get
    Output:
        temperature
    """

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):
        return 23

if __name__ == "__main__":
    temp = Temperature(country="India", city="Bengluru")
    print(temp.get())