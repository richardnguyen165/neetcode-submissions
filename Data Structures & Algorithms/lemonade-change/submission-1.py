class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        all_bills_record = {
            5: 0,
            10: 0,
            20: 0
        }

        for bill in bills:
            print(all_bills_record)
            if bill == 5:
                all_bills_record[5] += 1
            elif bill == 10:
                all_bills_record[10] += 1
                if all_bills_record[5] == 0:
                    return False
                all_bills_record[5] -= 1
            else:
                all_bills_record[20] += 1
                # First give back 10 5, then 5 5 5 

                if all_bills_record[10] > 0 and all_bills_record[5] > 0:
                    all_bills_record[10] -= 1
                    all_bills_record[5] -= 1
                elif all_bills_record[10] == 0 and all_bills_record[5] >= 3:
                    all_bills_record[5] -= 3
                else:
                    return False
        
        return True