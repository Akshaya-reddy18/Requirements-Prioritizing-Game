class Requirement:
    def __init__(self, name, business_value, complexity, risk):
        self.name = name
        self.business_value = business_value
        self.complexity = complexity
        self.risk = risk

    def __str__(self):
        return f"{self.name}: BV: {self.business_value}, C: {self.complexity}, R: {self.risk}"

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 10:  # Ensure the input is between 1 and 10
                return value
            else:
                print("Invalid input. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    requirements = []
    print("Welcome to the Requirements Prioritization Game!")

    while True:
        name = input("Enter the name of the requirement (or type 'done' to finish): ")
        if name.lower() == 'done':
            break

        business_value = get_input("Enter the business value (1-10): ")
        complexity = get_input("Enter the complexity (1-10): ")
        risk = get_input("Enter the risk (1-10): ")

        requirement = Requirement(name, business_value, complexity, risk)
        requirements.append(requirement)

    # Sort by business value (descending), complexity (ascending), and risk (ascending)
    requirements.sort(key=lambda x: (-x.business_value, x.complexity, x.risk))

    # Display the prioritized list of requirements
    print("\nPrioritized Requirements:")
    for req in requirements:
        print(req)

if __name__ == "__main__":
    main()
