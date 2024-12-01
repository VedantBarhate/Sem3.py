# Design a program to find the maximum profit you can make by
# scheduling jobs within their deadlines,
# considering their respective profits.

class Job:
    def __init__(self, job_id, profit, deadline):
        self.job_id = job_id
        self.profit = profit
        self.deadline = deadline

def job_scheduling(jobs, n):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs)

    slots = [-1] * max_deadline
    total_profit = 0

    for job in jobs:
        for j in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if slots[j] == -1:
                slots[j] = job.job_id
                total_profit += job.profit
                break

    return total_profit, slots

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    jobs = [
        Job('A', 100, 2),
        Job('B', 19, 1),
        Job('C', 27, 2),
        Job('D', 25, 1),
        Job('E', 15, 3)
    ]

    n = len(jobs)
    max_profit, job_sequence = job_scheduling(jobs, n)

    print(f"Maximum Profit: {max_profit}")
    print(f"Job sequence: {job_sequence}")
