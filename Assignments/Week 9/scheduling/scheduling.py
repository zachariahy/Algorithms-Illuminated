
WEIGHT = 0
LENGTH = 1

class Job:
    def __init__(self, weight: int, length: int):
        self.weight = weight
        self.length = length
        self.score = None
        self.completion_time = None

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
    # jobs = get_jobs_from_file("problem13.4test.txt")    # diff:68615, ratio:67247
    jobs = get_jobs_from_file("problem13.4.txt")    # diff:69119377652, ratio:67311454237

    # compute greedy diff or ratio score
    for job in jobs:
        job.score = job.weight - job.length
        # job.score = job.weight / job.length

    # create schedule
    schedule = sorted(jobs, key=lambda obj: (obj.score, obj.weight), reverse=True)

    # compute completion times
    time = 0
    for job in schedule:
        time += job.length
        job.completion_time = time

    # compute weighted sum of completion times
    weighted_sum = 0
    for job in schedule:
        weighted_sum += job.weight * job.completion_time

    print("weighted sum:", weighted_sum)
