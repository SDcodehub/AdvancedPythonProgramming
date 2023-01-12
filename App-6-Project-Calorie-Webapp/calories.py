from temperature import Temperature

class Calories:
    """
    calories class contains info and methods related to
    calories
    Input:
        weight
        height
        age
        temperature.py
    Method:
        calculate()
    Output:
        outputs calories
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        return float(self.weight + self.height + self.age + self.temperature)


if __name__ == "__main__":
    temp = Temperature(country="India", city="Bengluru")
    cal= Calories(weight=50,height=5.41, age=30, temperature=temp.get())
    print(cal.calculate())