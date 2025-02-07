def find(ordered_list, element_to_find):
    start_index = 0
    end_index = len(ordered_list) - 1

    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        middle_element = ordered_list[middle_index]

        if middle_element == element_to_find:
            return True
        elif middle_element < element_to_find:
            start_index = middle_index + 1  # Fix: Move start forward
        else:
            end_index = middle_index - 1  # Fix: Move end backward

    return False  # If not found, return False

if __name__ == "__main__":
    l = list(map(int, input("Enter a list of number: ")))
    x = int(input("Enter a number to put in list: "))
    print(find(l, x))
