def collect_input():
    return input("Enter your inputs: ")


class FrequentApp:

    @staticmethod
    def most_frequent(lst):
        element_count = {}

        for element in lst:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1

        most_frequent_elements = []
        highest_count = 0

        for element, count in element_count.items():
            if count > highest_count:
                most_frequent_elements = [element]
                highest_count = count
            elif count == highest_count:
                most_frequent_elements.append(element)

        return most_frequent_elements


if __name__ == "__main__":
    input_list = collect_input().split()
    result = FrequentApp.most_frequent(input_list)
    print("Most frequent element(s):", result)
