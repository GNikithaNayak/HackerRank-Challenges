number_of_testcases = int(input())
for _ in range(number_of_testcases):
    number_of_elements_first_set = int(input())
    first_set = set(map(int, input().split()))
    number_of_elements_second_set = int(input())
    second_set = set(map(int, input().split()))
    print(first_set.issubset(second_set))
