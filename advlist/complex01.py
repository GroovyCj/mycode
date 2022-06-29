#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)
    print(list1[1])
    # create a new list containing a single item
    list2 = ["juniper"]

    # extend list1 by list2 (combine both lists together into a single list)
    list1.extend(list2)

    # display list1, which now contains juniper
    print(list1)


main()

