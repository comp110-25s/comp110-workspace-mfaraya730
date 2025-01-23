"""Planning a Tea Party"""

__author__: str = "730449888"


def main_planner(guests: int) -> None:
    """Program Entrypoint"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """Gives Tea Cups per Person"""
    return people * 2


def treats(people: int) -> int:
    """Number of Treats Based on Number of Guests"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Total Cost of Tea Bags and Treats"""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
