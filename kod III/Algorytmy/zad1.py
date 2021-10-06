from commons import SimpleStack
import sys

if len(sys.argv) == 1:
    print("argumentem wybierz który algorytm, 1 lub 2")
elif sys.argv[1] == "1":
    raw_str = input("podaj liczby")
    # wszystkie to floaty oddzielane kropkami lub przecinkami, liczby oddzielane ;
    nums = [float(x.replace(",", ".")) for x in raw_str.split(";")]

    def maksymalna(nums):
        """Zwraca maksymalną liczbę lub none"""
        max_num = None
        for x in nums:
            if max_num is None:
                max_num = x
            elif x > max_num:
                max_num = x
        return max_num

    print(maksymalna(nums))
else:
    operator_priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
        "(": 0,
        ")": 0,
        None: 0
    }
    operators = list(operator_priority.keys())
    def infix2onp(text: str):
        res = ""
        stack = SimpleStack()
        for x in text:
            if x == "(":
                stack.push(x)
            elif x == ")":
                while (item := stack.pop()) != "(":
                    res += item
            elif x not in operators:
                # argumenty
                res += x
            else:
                if ((stack_prio := operator_priority[stack.last()]) <
                    (new_prio := operator_priority[x])):
                    stack.push(x)
                else:
                    while new_prio <= stack_prio:
                        res += stack.pop()
                        stack_prio = operator_priority[stack.last()]
                    stack.push(x)
        # dopisz pozostałe
        while item := stack.pop():
            res += item
        return res

    def solve_onp(text: str):
        stack = SimpleStack()
        for x in text:
            if x not in operators:
                stack.push(x)
            else:
                second_arg = stack.pop()
                first_arg = stack.pop()
                stack.push(eval("{}{}{}".format(
                    first_arg,
                    x.replace("^", "**"),
                    second_arg
                )))
        return stack.pop()

    def onp2infix(text: str):
        stack = SimpleStack()
        for x in text:
            if x not in operators:
                stack.push(x)
            else:
                second_arg = stack.pop()
                first_arg = stack.pop()
                stack.push("({}{}{})".format(
                    first_arg,
                    x,
                    second_arg
                ))
        return stack.pop()
        
    #działanie = "4*(5-6/3+1)^2"
    działanie = input("podaj działanie")
    print(infix2onp(działanie))
    print(onp2infix(infix2onp(działanie)))
    print("czy zadziałało: ", solve_onp(infix2onp(działanie)) == solve_onp(infix2onp(onp2infix(infix2onp(działanie)))))





