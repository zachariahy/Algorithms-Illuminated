
WEIGHT = 0
LENGTH = 1

class Job:
    def __init__(self, weight: int, length: int):
        self.weight = weight
        self.length = length
        self.diff_score = None
        self.ratio_score = None

def get_jobs_from_file(filepath):
    jobs_list = []
    with open(filepath, 'r') as file:
        for line in file:
            line = line.split()
            if len(line) > 1:
                job_item = Job(int(line[WEIGHT]), int(line[LENGTH]))
                jobs_list.append(job_item)
    return jobs_list

if __name__ == "__main__":
    # jobs = get_jobs_from_file("problem13.4test.txt")    # [68615, 67247]
    jobs = get_jobs_from_file("problem13.4.txt")    # [69119377652, 67311454237]

    # compute greedy diff and ratio scores
    for job in jobs:
        job.diff_score = job.weight - job.length
        job.ratio_score = job.weight / job.length

    # create schedules
    diff_schedule = sorted(jobs, key=lambda obj: (obj.diff_score, obj.weight), reverse=True)
    ratio_schedule = sorted(jobs, key=lambda obj: (obj.ratio_score, obj.weight), reverse=True)

    # compute completion times and weighted sum of completion times
    weighted_sums = []
    for schedule in [diff_schedule, ratio_schedule]:
        completion_time = 0
        weighted_sum = 0
        for job in schedule:
            completion_time += job.length
            weighted_sum += job.weight * completion_time
        weighted_sums.append(weighted_sum)

    print(weighted_sums)
